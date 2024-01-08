import os
import pyrebase
import json
from rabbitmq_utils import RabbitMQConsumer

# DATABASE
FIREBASE_CONFIG = {
    "apiKey": os.environ.get('API_KEY'),
    "authDomain": os.environ.get('AUTH_DOMAIN'),
    "databaseURL": os.environ.get('DATABASE_URL'),
    "projectId": os.environ.get('PROJECT_ID'),
    "storageBucket": os.environ.get('STORAGE_BUCKET'),
    "messagingSenderId": os.environ.get('MESSAGING_SENDER_ID'),
    "appId": os.environ.get('APP_ID'),
    "measurementId": os.environ.get('MEASUREMENT_ID')
}
firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
authe = firebase.auth()
FIREBASE_DB = firebase.database()


def callback_logic(ch, method, properties, body):
    # Getting message
    response = json.loads(body.decode())
    
    # Getting meta
    job_id = response['metadata']['request_id']
    
    # Getting data
    status = response['data'].get('status')
    data = {
        'progress': response['data'].get('progress', '0 %'),
    }
    if status:
        data['status'] = status
    
    FIREBASE_DB.child('jobs').child(job_id).update(data)
    
    # ACKNOWLEDGE WORK IS DONE
    ch.basic_ack(delivery_tag=method.delivery_tag)
    return None


if __name__ == "__main__":
    # INFORMATION
    host = os.environ.get('MQ_HOST', '127.0.0.1')
    port = os.environ.get('MQ_PORT', '9020')
    virtual_host = os.environ.get('MQ_VIRTUAL_HOST', '/')
    username = os.environ.get('MQ_USERNAME', 'guest')
    password = os.environ.get('MQ_PASSWORD', 'guest')
    exchange = os.environ.get('MQ_EXCHANGE', 'ai_exchange')
    routing_key = None
    queue_name = 'logs'
    
    # RECEIVING
    consumer = RabbitMQConsumer(host, port, virtual_host, username, password, queue_name, routing_key, exchange, callback_fun=callback_logic)
    consumer.receiveMessage()
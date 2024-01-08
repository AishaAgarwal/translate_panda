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
    status_code = response['metadata']['status_code']
    message = response['metadata']['message']
    
    # Getting status
    if status_code == 500:
        status = 'ai_error'
        processed_file_path = None
    else:
        status = 'completed'
        processed_file_path = response['data']['processed_file_path']
    
    # Making result
    data = {
        'status': status,
        'ai_status_code': status_code,
        'ai_message': message,
        'processed_file_path': processed_file_path
    }
    
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
    queue_name = 'result'
    
    # RECEIVING
    consumer = RabbitMQConsumer(host, port, virtual_host, username, password, queue_name, routing_key, exchange, callback_fun=callback_logic)
    consumer.receiveMessage()
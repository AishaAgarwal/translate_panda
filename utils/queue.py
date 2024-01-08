import json
import os
from rabbitmq_utils import RabbitMQProducer

def send_message_on_ai_queue(message, priority):
    """Sending message on ai queue."""
    message = json.dumps(message)
    producer = RabbitMQProducer(
        os.environ.get('MQ_HOST'),
        os.environ.get('MQ_PORT'),
        os.environ.get('MQ_VIRTUAL_HOST'),
        os.environ.get('MQ_USERNAME'),
        os.environ.get('MQ_PASSWORD'),
        os.environ.get('MQ_EXCHANGE')
    )
    
    if priority > 1:
        routing_key = 'paid_key'
    else:
        routing_key = 'free_key'
    is_sent = producer.sendMessage(message, routing_key, priority=priority)
    return is_sent
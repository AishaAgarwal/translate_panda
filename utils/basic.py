from datetime import datetime
import uuid

def get_datetime():
    return str(datetime.now())


def get_uuid():
    return str(uuid.uuid4())
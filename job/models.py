from django.conf import settings

def add_job(job_id, data):
    settings.FIREBASE_DB.child('jobs').child(job_id).update(data)
    return None

def filter_job(username):
    try:
        data = settings.FIREBASE_DB.child('jobs').order_by_child('created_by').equal_to(username).get().val()
    except:
        data = []
    return data

def get_language_lookup():
    """Getting list of language lookup."""
    data = settings.FIREBASE_DB.child('lu_target_language').get().val()
    if data is None:
        data = []
    return data
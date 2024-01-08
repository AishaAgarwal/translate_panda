from django.conf import settings

def get_plan_lookup():
    """Getting list of plan lookup."""
    data = settings.FIREBASE_DB.child('lu_plan').get().val()
    if data is None:
        data = []
    return data

def update_plan(username, plan):
    """Updating plan for user."""
    try:
        settings.FIREBASE_DB.child('user_plan').child(username).update({'plan': plan})
    except:
        pass
    return None

def get_plan_detail(plan):
    """Getting plan detail on the base of plan name."""
    try:
        data = settings.FIREBASE_DB.child('lu_plan').child(plan).get().val()
    except:
        data = None
    return data
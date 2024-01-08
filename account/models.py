from django.conf import settings
from django.contrib.auth.models import User

from .serializers import UserSerializer
from utils import get_datetime

def register_user(username, email):
    try:
        user = User.objects.filter(username=username, email=email)
        user_seralizer = UserSerializer(user.first())
        user_data = user_seralizer.data
        user_data['token'] = None
        user_data['plan'] = 'free'
        settings.FIREBASE_DB.child('users').child(username).update(user_data)
    except:
        pass
    return None

def login_user(username, token):
    try:
        last_login = get_datetime()
        settings.FIREBASE_DB.child('users').child(username).update({'token': token, 'last_login': last_login})
    except:
        pass
    return None

def logout_user(username):
    try:
        last_logout = get_datetime()
        settings.FIREBASE_DB.child('users').child(username).update({'token': None, 'last_logout': last_logout})
    except:
        pass
    return None

def get_user_plan(username):
    """Getting user plan on the base of username."""
    try:
        data = settings.FIREBASE_DB.child('user_plan').child(username).get().val()
        if data is None:
            data = 'free'
        else:
            data = data['plan']
    except:
        data = 'free'
    return data
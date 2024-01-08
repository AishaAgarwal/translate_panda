from .settings import *
import pyrebase


# Application definition
INSTALLED_APPS.append('rest_framework')
INSTALLED_APPS.append('rest_framework.authtoken')
INSTALLED_APPS.append('account.apps.AccountConfig')
INSTALLED_APPS.append('job.apps.JobConfig')
INSTALLED_APPS.append('plan.apps.PlanConfig')


# Middleware
MIDDLEWARE.append('corsheaders.middleware.CorsMiddleware')


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
AUTH = firebase.auth()
FIREBASE_DB = firebase.database()

# Static file configuration
STATIC_ROOT =  os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'custom_static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'
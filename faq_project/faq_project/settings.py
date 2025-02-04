INSTALLED_APPS = [
    ...,
    'ckeditor',
]
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
        'height': 300,
        'width': 800,
    },
}
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Adjust based on your Redis setup
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# settings.py

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'yourdomain.com']



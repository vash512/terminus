#configuraciones locales

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@k3-99c%n+9$lyi(%do_!&ruajjed*3&j0&h(e^$r3c%v6g0bt'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'terminus_db',
        'USER': 'belen_ter',
        'PASSWORD': 'belen_passwd',
        'HOST': 'localhost',
    }
}



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#clave mandrill
API_KEY = 'Db9t7n5kJHIrJLw5wXyuJg'
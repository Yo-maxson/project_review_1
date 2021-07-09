import os
from datetime import timedelta


basedir = os.path.abspath(os.path.dirname(__file__))# вычисление имени директории

WEATHER_DEFAULT_CITY = "Moscow,Russia"
WEATHER_API_KEY = "f1f5ed30798042f385a191623210406"
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = "SFSFOEdf;ljge;49flkdfkldf3fw321fghlop"

REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False
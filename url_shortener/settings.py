import os

SQLALCHEMY_DATABASE_URI = 'postgres://tvppxeowqauplt:b4242d2188123f573a997c5dc3c2872af6155b48b2e4bebcf994e8cc85929e0d@ec2-54-75-229-28.eu-west-1.compute.amazonaws.com:5432/de22lv24t3u0rh'
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
SECRET_KEY = os.environ.get('SECRET_KEY')
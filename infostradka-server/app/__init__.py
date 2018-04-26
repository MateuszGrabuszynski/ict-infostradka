from flask import Flask, request, redirect, url_for, Session
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/screenshots'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'gif'])

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
sess = Session()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes
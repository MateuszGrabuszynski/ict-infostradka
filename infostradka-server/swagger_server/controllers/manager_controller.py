import connexion
import six

from swagger_server.models.rotator import Rotator  # noqa: E501
from swagger_server import util
from swagger_server.config import MONGO_HOST, MONGO_PORT, FILES_DIR

#own
from flask import render_template, redirect
from pymongo import MongoClient
import hashlib, os


#1-left,2-right,3-news
def db_replace(rotator,body):
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client.infostradka
    if rotator == 1:
        db.left.remove()
        db.left.insert(body)
    if rotator == 2:
        db.right.remove()
        db.right.insert(body)
    if rotator == 3:
        db.news.remove()
        db.news.insert(body)


def allowed_file(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def get_manager():  # noqa: E501
    """Returns display

     # noqa: E501


    :rtype: List[Rotator]
    """
    return render_template("manager.html")


def get_displays_list():
    pass


def get_displays_content():
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client.infostradka

    left = db.left.find({}, {"since": 1, "until": 1, "duration": 1, "type": 1, "content": 1, "_id": 0})
    leftdb = []
    for d1 in left:
       leftdb.append(d1)

    files = db.files.find({}, {"name": 1, "hash": 1, "_id": 0})
    filesdb = []
    for f1 in files:
       filesdb.append(f1)

    return render_template("main_content.html", elements=leftdb, files=filesdb)


def update_displays_content(body):
    db_replace(1,body)


def get_right_content():
    pass


def update_right_content(body):
    db_replace(2,body)


def get_news_bar():
    pass


def update_news_bar(body):
    db_replace(3,body)

def get_file_manager():
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client.infostradka

    files = db.files.find({}, {"type": 1, "name": 1, "hash": 1, "_id": 0})
    filesdb = []
    for f1 in files:
        filesdb.append(f1)
    
    return render_template("files.html", files=filesdb)


def post_file(file):
    ALLOWED_EXTENSIONS = set(['html', 'htm', 'png', 'jpg', 'jpeg', 'gif'])

    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client.infostradka
#    bytename = file.filename.encode()+file.read()
    hash = hashlib.sha256(file.filename.encode()+file.read()).hexdigest()

    print(file.read())

#    print(os.getcwd())
#    print(file.filename)
    # check if the post request has the file part
  #  if 'file' not in request.files:
  #      flash('No file part')
  #      return redirect(request.url)
  #  file = request.files['file']

    if file.filename == '':
        return redirect("/v1/manager/files?err=emptyfilename")
    if file and allowed_file(file.filename, ALLOWED_EXTENSIONS):
        ftype = file.filename.split('.')[1].lower()
        if ftype == 'htm':
            ftype = 'html'
        elif ftype == 'jpg':
            ftype = 'jpeg'
        db.files.insert({"type": ftype, "name": file.filename, "hash": hash})
        fullpath = os.path.join(os.getcwd(), FILES_DIR, hash)
        file.save(fullpath)
        print('file saved as:' + fullpath)
#        file.save(fullpath)

        return redirect("/v1/manager/files")

def delete_file(hash):
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client.infostradka

    os.remove(os.path.join(os.getcwd(), FILES_DIR, hash))
    db.files.remove({"hash": hash})
    pass

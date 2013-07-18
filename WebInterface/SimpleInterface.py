# ------------------------------------------------------
#
#   SimpleInterface.py
#   By: Fred Stakem
#   Created: 6.4.13
#
# ------------------------------------------------------


# Libs
from flask import request as f_request
from flask import redirect as f_redirect
from flask import url_for as f_url_for
from flask import Flask
import requests
import sqlalchemy as sql
from werkzeug import secure_filename
import os
import subprocess, signal
import multiprocessing as mp
import time
import uuid

# User defined
from Database import db_session, init_db
from Log import Log
from LogData import LogData

# Create the app
app = Flask(__name__)
upload_folder = '../upload'
app.config['UPLOAD_FOLDER'] = upload_folder
sqlite_db = upload_folder + '/log_files.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
def findEvents():
    pass
                      
@app.route('/a', methods=['POST'])
def createLogType():
    print 'Received POST for /a'
    log_name = f_request.form.get('name') 
    log_id = unicode(uuid.uuid1().urn.split(':')[-1])
    
    log = Log(name=log_name, metadata_loc='None', user_handle=log_id)
    db_session.add(log)
    try:
       db_session.commit()
    except Exception as e:
       print repr(e)
       db_session.flush()
    
    return log_id

@app.route('/b')
def addMetadataToLog():
    print 'B'
    
    return ''

@app.route('/c', methods=['POST'])
def storeLogData():
    print 'Received POST for /c'
    log_type_handle = f_request.form.get('handle') 
    log = Log.query.filter(Log.user_handle == log_type_handle).first()
    print 'Found log type for handle %s: %s'  % (log_type_handle, str(log))
    
    file = f_request.files.get('log data')
    print 'Uploaded file: %s' % (file) 
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    # Create db entry
    print 'Storing information into database...'
    log_data_id = unicode(uuid.uuid1().urn.split(':')[-1])
    log_data = LogData(log_loc=upload_folder, user_handle=log_data_id)
    log.data.append(log_data)
    db_session.add(log)
    
    try:
       db_session.commit()
    except Exception as e:
       print repr(e)
       db_session.flush()
    
    return log_data_id

@app.route('/d', methods=['POST'])
def findEventsInLog():
    print 'Received POST for /d'
    log_handle = f_request.form.get('handle') 
    log_data = LogData.query.filter(LogData.user_handle == log_handle).first()
    print 'Found log for handle %s: %s'  % (log_handle, str(log_data))
    
    file = f_request.files.get('event data')
    print 'Uploaded file: %s' % (file) 
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
    # Find events
    
    return ''

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    print 'Starting test...'
    
    print 'Getting rid of previously uploaded files...'
    for the_file in os.listdir(upload_folder):
        file_path = os.path.join(upload_folder, the_file)
        try:
            file_type = file_path.rsplit('.', 1)[1]
            if os.path.isfile(file_path):
                print 'Deleting file: %s' % (file_path)
                os.unlink(file_path)
        except Exception, e:
            print e
            
    print 'Creating new database for test...'
    init_db()
        
    print 'Starting server...'
    app.threaded = True
    p = mp.Process(target=app.run)
    p.start()
    time.sleep(1)
    
    print 'Testing server...'
    server_address = '127.0.0.1:5000'
    
    print 'Creating log type...'
    response = requests.post('http://' + server_address + '/a', data={'name': 'test log'})
    log_type_handle = response.content
    print 'Handle to log type: %s' % (log_type_handle)
    
    print 'Sending data file to server...'
    file_name = 'android_log_1.txt'
    file_path = '../data/' + file_name
    response = requests.post('http://' + server_address + '/c', data={'handle': log_type_handle}, files={'log data': open(file_path, 'rb')})
    log_handle = response.content
    print 'Handle to log: %s' % (log_handle)
    
    print 'Sending event file to server...'
    file_name = 'android_event_1.txt'
    file_path = '../events/' + file_name
    response = requests.post('http://' + server_address + '/d', data={'handle': log_handle}, files={'event data': open(file_path, 'rb')})
    log_handle = response.content
    # Response ->
    
    print 'Finished test.'
    p = subprocess.Popen(['killall', 'Python'], stdout=subprocess.PIPE)
    
    
    
    
    
    
    
    
    
    
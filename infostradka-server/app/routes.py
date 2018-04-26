from app import app
from flask import render_template, jsonify, request, redirect, flash
import os
from werkzeug.utils import secure_filename


#checker if file ext. is allowed here
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def www():
	return render_template("index.html")
	
@app.route('/api')
def api():
	JSON = {"left":[{"since":"2018-05-10 22:00","until":"2019-04-10 22:00","duration":23,"type":"video","content":{"source":"http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_normal.mp4","subtitles":""}},{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":12,"type":"video","content":{"source":"https://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_1mb.mp4"}},{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":15,"type":"video","content":{"source":"https://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_5mb.mp4"}}],"right":[{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":3,"source":"https://c1cleantechnicacom-wpengine.netdna-ssl.com/files/2018/02/Wind-Power-Birds.jpg"}],"news":[{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":4,"title":"Aaa, kotki dwa","content":"...szarobure obydwa czy coś tam jakoś tam coś.<br><br>BARDZO DUŻO TEKSTU TUTAJ...","important":0},{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":8,"title":"News2","content":"Lill news numero due","important":1}]}
	return jsonify(JSON)
	
@app.route('/manager')
def manager():
	return render_template("manager.html")
	
@app.route('/manager/upload', methods=['POST', 'GET'])
def upload():
	if request.method == 'POST':
		#check if the request has file
		if 'file' not in request.files:
			flash('No file')
			return redirect(request.url)
		file = request.files['file']
		#when no filename
		if file.filename == '':
			flash('No filename')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('uploaded_file', filename=filename))
	else:
		return '''<html><h1>uploaded successfully!</h1></html>'''
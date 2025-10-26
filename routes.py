import flask
from flask import Blueprint, request, send_file
from db import find_object_by_name
from logs import log
from algorithm import home
from storememe import store_meme_image
bp = Blueprint('main', __name__)

# ISIS = Internet Service Interaction Success
# ISIF = Internet Service Interaction Failure
# PORN = Persistent Object Request Noticed
# BIN = Bad Interaction Noted
# LADEN = Label Access Denial Encryption Noted  





@bp.route('/sendmeme')
def send_meme():
	log("ISIS : Meme requested", "blue")
	# Accept either `meme` or `name` as query param for compatibility with clients
	req_meme = request.args.get('meme') or request.args.get('name') or 'dog'
	req_meme = str(req_meme)
	log(f"ISIS : Meme requested - {req_meme}", "blue")
	meme_obj = find_object_by_name(req_meme)
	if meme_obj:
		return send_file(meme_obj['path'], mimetype='image/jpeg')
	else:
		log(f"ISIF : Meme not found - {req_meme}", "red")
		return "Meme not found", 404




@bp.route('/home')
def home_route():
	return home()

 
@bp.route('/hello')
def hello():
	log("ISIS : /hello accessed", "green")
	return "Hello from routes.py!"


@bp.route('/uploadmeme', methods=['POST'])
def storememe():
    if 'image' not in request.files or 'name' not in request.form:
        log("BIN : Missing image or name in request", "red")
        return {"status": "error", "message": "Missing image or name"}, 400

    image_file = request.files['image']
    image_name = request.form['name']
    image_category = request.form['category']
    if image_file.filename == '' or image_name.strip() == '':
        log("BIN : Empty image filename or name", "red")
        return {"status": "error", "message": "Empty image filename or name"}, 400
    image_data = image_file.read()
    result = store_meme_image(image_data, image_name, image_category, original_filename=image_file.filename)
    return result

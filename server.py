from flask import Flask, send_from_directory, request, jsonify, send_file
import random
from flask.helpers import make_response
import qrcode
import qr

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route('/qr_codes/<file_name>')
def get_image(file_name):
    full_path = f'./qr_codes/{file_name}'
    return send_file(full_path,mimetype="image")

@app.route('/get_qr_codes/<img_name>')
def get_images(img_name):
    full_path = f'./qr_codes/{img_name}'
    return send_file(full_path, mimetype='image')


@app.route("/generate_qr",methods=['POST'])
def create_qr():
        name = request.json
        actual_name = name['name']
        qr.create_qr_code(name)
        image = f'/qr_codes/{actual_name}.png'

        return_obj = jsonify({'image':image})
        resp = make_response(return_obj, 200)
        return resp
        
@app.route("/scan/qr_code")
def scan_qr_code():
    re_obj = jsonify({'feature':'esperate'})
    resp = make_response(re_obj, 200)
    return resp
    #qr.open_cam()

if __name__ == "__main__":
    app.run(debug=True)

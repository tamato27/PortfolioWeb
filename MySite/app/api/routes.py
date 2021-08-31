from flask import Blueprint, render_template, jsonify, request, send_file
from flask import current_app as app

import os
import hashlib

from .utils import check_valid_client, validate_client, qr_vcard


api = Blueprint('api', __name__)


@api.route('/')
def home():
    """ API Home Page """
    return render_template('api.html')


@api.route('/keygen')
def gen_api_key():
    """ Generate a new API key on reload """

    api_key = hashlib.sha256(os.urandom(32)).hexdigest()  # preferred
    api_key2 = os.urandom(16)

    return render_template('api-gen.html', key1=api_key, key2=api_key2)


@api.route('/qr', methods=['GET', 'POST'])
def generate_qr():
    """ QR Code Generator """

    if request.method == "POST":
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')
        email = f"{firstname.lower()}.{lastname.lower()}@rsa.co.za"

        return jsonify(Email_address=email)

    return jsonify(response={"success": "Successfully Sent the data."})  # true when Get request


@api.route('/get_image', methods=['GET', 'POST'])
def get_image_from_get():
    """ Renders a image from url """

    I_UPLOAD_FOLDER = "static/site_img"

    if request.args.get('type') == '1':
        filename = "ok.gif"
    else:
        filename = "error.gif"

    # path = url_for('static', filename='site_img/')
    path2 = os.path.join(app.root_path, I_UPLOAD_FOLDER, filename)

    return send_file(path2, mimetype='image/gif', as_attachment=False)
    # return send_from_directory(path2, filename)


@api.route('/json-data', methods=['POST'])
def json_data():
    """
    returns formatted string from posted json data
    and also builds the email address
    """

    data = request.get_json()

    username = None
    surname = None
    mobile_phone = None
    job_title = None
    department = None
    business_unit = None
    domain = "@rsa.co.za"
    email = None

    if data:
        if 'UserName' in data:
            username = data['UserName']

        if 'Surname' in data:
            surname = data['Surname']

        if 'mobilePhone' in data:
            mobile_phone = data['mobilePhone']

        if 'JobTitle' in data:
            job_title = data['JobTitle']

        if 'Department' in data:
            department = data['Department']

        if 'Business unit' in data:
            business_unit = data['Business unit']

        email = f"{username}.{surname}{domain}"

    return f'''
               The Username value is: {username}
               The Surname value is: {surname}
               The Mobile Phone value is: {mobile_phone}
               The Job Title value is: {job_title}
               The Department value is: {department}
               The Business Unit value is: {business_unit}
               The email value is: {email}
               '''


@api.route('/json-example', methods=['POST'])
def json_example():
    """ returns formatted string from posted json data """

    request_json_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_json_data:
        if 'language' in request_json_data:
            language = request_json_data['language']

        if 'framework' in request_json_data:
            framework = request_json_data['framework']

        if 'version_info' in request_json_data:
            if 'python' in request_json_data['version_info']:
                python_version = request_json_data['version_info']['python']

        if 'examples' in request_json_data:
            if (type(request_json_data['examples']) == list) and (len(request_json_data['examples']) > 0):
                example = request_json_data['examples'][0]

        if 'boolean_test' in request_json_data:
            boolean_test = request_json_data['boolean_test']

    return '''
               The language value is: {}
               The framework value is: {}
               The Python version is: {}
               The item at index 0 in the example list is: {}
               The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


@api.route('/nandis-json', methods=['POST'])
def nandis():
    """ returns only email from posted json data """

    request_json_data = request.get_json()

    username = None
    surname = None
    mobile_phone = None
    job_title = None
    department = None
    business_unit = None
    domain = "@rsa.co.za"

    if request_json_data:
        if 'UserName' in request_json_data:
            username = request_json_data['UserName']

        if 'Surname' in request_json_data:
            surname = request_json_data['Surname']

        if 'mobilePhone' in request_json_data:
            mobile_phone = request_json_data['mobilePhone']

        if 'JobTitle' in request_json_data:
            job_title = request_json_data['JobTitle']

        if 'Department' in request_json_data:
            department = request_json_data['Department']

        if 'Business unit' in request_json_data:
            business_unit = request_json_data['Business unit']

        email = f"{username}.{surname}{domain}"

        return jsonify(
            mail=email)  # true when Get request


@api.route('/nandis-json-v2', methods=['POST'])
def nandis_v2():
    """ returns only email from posted json data working for RSA"""

    request_json_data = request.get_json()

    output = check_valid_client(request_json_data)

    return jsonify(output)


@api.route('/client-vcard-qr-v1', methods=['POST'])
def qr_client():
    """ Generate a qrcode for clients """

    data = request.get_json()
    validated_client = validate_client(data)

    if validated_client:
        # return jsonify(response={"success": "You will recieve your vcard QR Code."})  # true when Get requeststatus=200, "Your Vcard QR Code will be generated")
        qr = qr_vcard(data)
        return jsonify(qr)

    else:
        return jsonify("You are not allowed to generate qr codes")










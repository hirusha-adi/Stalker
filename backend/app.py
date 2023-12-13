from flask import Flask
from flask import request
from flasgger import Swagger

from modules import PhoneNumberLookup

api = Flask(__name__)
swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/"
}

swagger = Swagger(api, config=swagger_config)

@api.route('/phone_num', methods=['POST'])
def phone_number_information():

    phone_number = request.form.get('PHONE_NUMBER')  

    if phone_number:
        obj = PhoneNumberLookup(phone_number)
        result = obj.run()
        return result
    else:
        return "Phone number not provided in the request.", 400

from flask import Flask
from flask import jsonify
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

@api.route('/phone_num')
def phone_number_information():

    obj = PhoneNumberLookup("+94713395547")
    result = obj.run()
    # print(result)
    return result

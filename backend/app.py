from flask import Flask
from flask import request
from flasgger import Swagger

from modules import PhoneNumberLookup
from modules import AccountLookup

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

api.config['SWAGGER'] = {
    'title': 'Phone Number Information API',
    'uiversion': 3,
}

swagger = Swagger(api, config=swagger_config)

@api.route('/phone_num', methods=['POST'])
def phone_number_information():
    """
    Endpoint to get information about a phone number.

    ---
    parameters:
      - name: PHONE_NUMBER
        in: formData
        type: string
        required: true
        description: The phone number to look up.

    responses:
      200:
        description: Successful response
        schema:
          type: object
          properties:
            status:
              type: object
              properties:
                error:
                  type: boolean
                error_desc:
                  type: array
                  items:
                    type: string
                show_information:
                  type: boolean
                show_scanner_googlesearch:
                  type: boolean
            information:
              type: object
              properties:
                raw_local:
                  type: string
                local:
                  type: string
                e164:
                  type: string
                international:
                  type: string
                country:
                  type: string
            scanner_googlesearch:
              type: object
              properties:
                social_media:
                  type: array
                  items:
                    type: string
                disposable_providers:
                  type: array
                  items:
                    type: string
                reputation:
                  type: array
                  items:
                    type: string
                individuals:
                  type: array
                  items:
                    type: string
                general:
                  type: array
                  items:
                    type: string
      400:
        description: Phone number not provided in the request.
    """
    phone_number = request.form.get('PHONE_NUMBER')  

    if phone_number:
        obj = PhoneNumberLookup(phone_number)
        result = obj.run()
        return result
    else:
        return "Phone number not provided in the request.", 400

@api.route('/account_lookup', methods=['POST'])
def account_lookup():
    """
    Endpoint to perform an account lookup based on the provided username.

    ---
    parameters:
      - name: USERNAME
        in: formData
        type: string
        required: true
        description: The username to look up.

    responses:
      200:
        description: Successful response
        schema:
          type: object
          properties:
            status:
              type: object
              properties:
                error:
                  type: boolean
                error_desc:
                  type: array
                  items:
                    type: string
                show_accounts_custom:
                  type: boolean
                total_accounts:
                  type: integer
            found_accounts:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  username:
                    type: string
                  name:
                    type: string
                  url_main:
                    type: string
                  url_user:
                    type: string
                  exists:
                    type: string
                  http_status:
                    type: string
                  response_time_s:
                    type: string
      400:
        description: Username not provided in the request.
    """
    
    username = request.form.get('USERNAME')

    if username:
        obj = AccountLookup(username=username)
        result = obj.run()
        return result
    else:
        return "Username not provided in the request.", 400

if __name__ == "__main__":
    api.run(port=5001, debug=True)
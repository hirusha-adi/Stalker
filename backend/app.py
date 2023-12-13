from flask import Flask
from flasgger import Swagger


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

    """
    phoneinfogaData = {
    status: {
      error: false,
      error_desc: "",
      show_information: true,
      show_GoogleDorks: true,
    },
    information: {
      rawLocal: "0713395547",
      local: "071 339 5547",
      e164: "+94713395547",
      international: "94713395547",
      country: "LK",
    },
    googleDorks: {
      socialMedia: [
        { id: 1, url: "" },
        { id: 2, url: "" },
      ],
      disposableProviders: [
        { id: 1, url: "" },
        { id: 2, url: "" },
      ],
      reputation: [
        { id: 2, lastName: "Lannister", firstName: "Cersei", age: 42 },
        { id: 3, lastName: "Lannister", firstName: "Cersei", age: 42 },
      ],
      individuals: [
        { id: 4, lastName: "Hirusha", firstName: "Jon", age: 35 },
        { id: 5, lastName: "Hirusha", firstName: "Jon", age: 35 },
      ],
      general: [
        { id: 8, lastName: "Stark", firstName: "Arya", age: 16 },
        { id: 9, lastName: "Stark", firstName: "Arya", age: 16 },
      ],
    },
  };

    """
    final_data = {
        'status': {
        'error': False,
        'error_desc': "",
        'show_information': True,
        'show_GoogleDorks': True,
      },
      'information': {
        'rawLocal': "0713395547",
        'local': "071 339 5547",
        'e164': "+94713395547",
        'international': "94713395547",
        'country': "LK",
      },
    }

    return final_data

if __name__ == "__main__":
  from modules import PhoneNumberLookup
  obj = PhoneNumberLookup.test("+94713395547")
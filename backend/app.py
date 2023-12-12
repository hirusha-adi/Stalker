from flask import Flask
from flasgger import Swagger


api = Flask(__name__)
swagger = Swagger(api, template_file='swagger_template.yml', url='/')


@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body

from flask import Flask
from route import api

def create_app():
    
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/senic_api')
    return app

if __name__ == '__main__':
    app = create_app()
    api.run(debug=True)

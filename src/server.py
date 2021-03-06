from flask import Flask
from webapp.views import webapp
from api.views import api
import sys

app = Flask(__name__)
app.register_blueprint(webapp)
app.register_blueprint(api)

DEFAULT_PORT = 5000

if __name__ == '__main__':
    app.debug = True
    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT
    app.run(host='0.0.0.0', port=port)

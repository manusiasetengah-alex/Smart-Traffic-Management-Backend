from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from config import Config as C
from models import db
from routes import routes as api
from auth import routes as auth, jwt
from datafeed import data_event

app = Flask(__name__)
app.config.from_object(C)

CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

db.init_app(app)
jwt.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth)    
app.register_blueprint(api)

data_event(socketio=socketio)

@app.route('/')
def index():
    return "Selamat datang pengunjung, awokwok"

if __name__ == "__main__":
    socketio.run(app, debug=False, port=5000)

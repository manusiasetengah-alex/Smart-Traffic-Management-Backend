from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

from config import Config as C
from models import db
from routes import routes as api

app = Flask(__name__)
app.config.from_object(C)

CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

db.init_app(app)

with app.app_context():
    db.create_all()
    
app.register_blueprint(api)
@app.route('/')
def index():
    return "Selamat datang pengunjung, awokwok"

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000)
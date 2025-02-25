from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# model 
class User():
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    passkey = db.Column(db.String(128), nullable=False)
    
    def todict(self):
        return {
            'id': self.id,
            'email': self.email,
            'passkey': self.passkey
        }

class Region():
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    passkey = db.Column(db.String(128), nullable=False)
    
    def todict(self):
        return {
            'id': self.id,
            'location': self.location,
            'passkey': self.passkey
        }

class GuardPost():
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    
    def todict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Crowded():
    id = db.Column(db.Integer, primary_key=True)
    time_detect = db.Column(db.String(255), nullable=False)
    vehicle_number = db.Column(db.Integer, nullable=False)
    
    def todict(self):
        return {
            'id': self.id,
            'time_detect': self.time_detect,
            'vehicle_number': self.vehicle_number
        }

# automatically create all the table when the server is up
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000)
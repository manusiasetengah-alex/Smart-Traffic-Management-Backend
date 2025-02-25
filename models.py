from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    passkey = db.Column(db.String(128), nullable=False)
    
    def todict(self):
        return {
            'id': self.id,
            'email': self.email,
            'passkey': self.passkey
        }
        
    def check_password(self, password):
        return self.passkey == password

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    passkey = db.Column(db.String(128), nullable=False)
    
    def todict(self):
        return {
            'id': self.id,
            'location': self.location,
            'passkey': self.passkey
        }

class GuardPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    
    def todict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Crowded(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_detect = db.Column(db.String(255), nullable=False)
    vehicle_number = db.Column(db.Integer, nullable=False)
    
    def todict(self):
        return {
            'id': self.id,
            'time_detect': self.time_detect,
            'vehicle_number': self.vehicle_number
        }

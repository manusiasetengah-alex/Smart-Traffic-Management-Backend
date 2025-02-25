from flask import Blueprint, request, jsonify
from models import db, User, Region, GuardPost, Crowded
from message_template import MESSAGE as message

routes = Blueprint('routes', __name__)

# ================== USER ==================
@routes.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(email=data['email'], passkey=data['passkey'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.todict()), 201

@routes.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.todict() for user in users]), 200

@routes.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify(message[404]), 404
    
    return jsonify(user.todict()), 200

@routes.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    
    user = User.query.get(id)
    
    if user is None:
        return jsonify(message[404]), 404
    
    data = request.get_json()
    user.email = data['email']
    user.passkey = data['passkey']
    db.session.commit()
    return jsonify(user.todict()), 200

@routes.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify(message[404]), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify(message[204]), 204
# ================== USER ==================

# ================== REGION ==================
@routes.route('/region', methods=['POST'])
def create_region():
    data = request.get_json()
    region = Region(location=data['location'], passkey=data['passkey'])
    db.session.add(region)
    db.session.commit()
    return jsonify(region.todict()), 201

@routes.route('/region', methods=['GET'])
def get_regions():
    regions = Region.query.all()
    return jsonify([region.todict() for region in regions]), 200

@routes.route('/region/<int:id>', methods=['GET'])
def get_region(id):
    region = Region.query.get(id)
    if region is None:
        return jsonify(message[404]), 404
    
    return jsonify(region.todict()), 200

@routes.route('/region/<int:id>', methods=['PUT'])
def update_region(id):
    
    region = Region.query.get(id)
    
    if region is None:
        return jsonify(message[404]), 404
    
    data = request.get_json()
    region.location = data['location']
    region.passkey = data['passkey']
    db.session.commit()
    return jsonify(region.todict()), 200

@routes.route('/region/<int:id>', methods=['DELETE'])
def delete_region(id):
    region = Region.query.get(id)
    if region is None:
        return jsonify(message[404]), 404
    
    db.session.delete(region)
    db.session.commit()
    return jsonify(message[204]), 204
# ================== REGION ==================


# ================== CROWDED ==================

@routes.route('/crowded', methods=['POST'])
def create_crowded():
    data = request.get_json()
    crowded = Crowded(time_detect=data['time_detect'], vehicle_number=data['vehicle_number'])
    db.session.add(crowded)
    db.session.commit()
    return jsonify(crowded.todict()), 201

@routes.route('/crowded', methods=['GET'])
def get_crowdeds():
    crowdeds = Crowded.query.all()
    return jsonify([crowded.todict() for crowded in crowdeds]), 200

@routes.route('/crowded/<int:id>', methods=['GET'])
def get_crowded(id):
    crowded = Crowded.query.get(id)
    if crowded is None:
        return jsonify(message[404]), 404
    
    return jsonify(crowded.todict()), 200

@routes.route('/crowded/<int:id>', methods=['PUT'])
def update_crowded(id):
    
    crowded = Crowded.query.get(id)
    
    if crowded is None:
        return jsonify(message[404]), 404
    
    data = request.get_json()
    crowded.time_detect = data['time_detect']
    crowded.vehicle_number = data['vehicle_number']
    db.session.commit()
    return jsonify(crowded.todict()), 200

@routes.route('/crowded/<int:id>', methods=['DELETE'])
def delete_crowded(id):
    crowded = Crowded.query.get(id)
    if crowded is None:
        return jsonify(message[404]), 404
    
    db.session.delete(crowded)
    db.session.commit()
    return jsonify(message[204]), 204

# ================== CROWDED ==================



# ================== GUARDPOST ==================

@routes.route('/guardpost', methods=['POST'])
def create_guardpost():
    data = request.get_json()
    guardpost = GuardPost(name=data['name'])
    db.session.add(guardpost)
    db.session.commit()
    return jsonify(guardpost.todict()), 201

@routes.route('/guardpost', methods=['GET'])
def get_guardposts():
    guardposts = GuardPost.query.all()
    return jsonify([guardpost.todict() for guardpost in guardposts]), 200

@routes.route('/guardpost/<int:id>', methods=['GET'])
def get_guardpost(id):
    guardpost = GuardPost.query.get(id)
    if guardpost is None:
        return jsonify(message[404]), 404
    
    return jsonify(guardpost.todict()), 200

@routes.route('/guardpost/<int:id>', methods=['PUT'])
def update_guardpost(id):
    
    guardpost = GuardPost.query.get(id)
    
    if guardpost is None:
        return jsonify(message[404]), 404
    
    data = request.get_json()
    guardpost.name = data['name']
    db.session.commit()
    return jsonify(guardpost.todict()), 200

@routes.route('/guardpost/<int:id>', methods=['DELETE'])
def delete_guardpost(id):
    guardpost = GuardPost.query.get(id)
    if guardpost is None:
        return jsonify(message[404]), 404
    
    db.session.delete(guardpost)
    db.session.commit()
    return jsonify(message[204]), 204

# ================== GUARDPOST ==================
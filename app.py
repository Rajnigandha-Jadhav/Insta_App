from flask import Flask, request, jsonify
from models.user_model import User
from database.database import db
from bson.json_util import loads, dumps
from werkzeug.security import generate_password_hash
from bson import ObjectId
from validations.validation import UserSchema 
user_schema = UserSchema()

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
      
      try:
           
          user_data = request.json
          if not user_data:
            return "Please provide some data", 400
          person_data = user_schema.load(user_data)

          hashed_password = generate_password_hash(person_data.password)
          user = User(name=person_data.name, email=person_data.email, password=hashed_password,followers=person_data.followers)
          insert_data = vars(user)

          db.users.insert_one(insert_data)
          resp = jsonify('Profile added successfully') 
          resp.status_code = 200
          return resp

      except Exception as e:
          return str(e), 500




@app.route('/all-users/<pageNumber>', methods=['GET'])
def get_all_users(pageNumber):
    try:
        
        PAGE_SIZE = 10
        pageNumber = int(pageNumber) or 1
        skip = (pageNumber - 1) * PAGE_SIZE
        users = db.users.find().skip(skip).limit(PAGE_SIZE)
        user_list = []
        for user in users:
            print(user)
            user_dict = {}
            user_dict['name'] = user['name']
            user_dict['email'] = user['email']
            user_dict['password'] = user['password']
            user_dict['follwers'] = user['followers']



            user_list.append(user_dict)
        resp = jsonify(user_list)
        resp.status_code = 200
        return resp
    except Exception as e:
        return str(e), 500
    




@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = db.users.find_one({'_id': ObjectId(user_id)})
        if not user:
            return jsonify({'error': 'user not found'}), 404
        
        user_dict = {}
        user_dict['name'] = user['name']
        user_dict['email'] = user['email']
        user_dict['password'] = user['password']
        user_dict['followers'] = user['followers']

        resp = jsonify(user_dict)
        resp.status_code = 200
        return resp
    
    except Exception as e:
        return str(e), 500






from bson import ObjectId

@app.route('/add-follower/<user_id>', methods=['PUT'])
def add_follower(user_id):
    try:
        follower = request.json.get('follower')
        if not follower:
            return jsonify({'error': 'follower name not provided'}), 400
        
        db.users.update_one(
            {'_id': ObjectId(user_id)},
            {'$addToSet': {'followers': follower}}
        )

        return jsonify({'message': 'follower added successfully'}), 200
    
    except Exception as e:
        return str(e), 500




@app.route('/followers/<user_id>', methods=['GET'])
def get_followers(user_id):
    try:
        user = db.users.find_one({'_id': ObjectId(user_id)})
        if not user:
            return jsonify({'error': 'user not found'}), 404
        
        followers = user.get('followers', [])
        return jsonify({'followers': followers}), 200
    
    except Exception as e:
        return str(e), 500





if __name__ == '__main__':
    app.run(debug=True)








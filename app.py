from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

users = [
    {'name':'chucky','id':'1'},
    {'name':'mike','id':'2'},
    {'name':'hilda','id':'3'},
    {'name':'jax','id':'4'}
]

blogs = {
    'chucky':[
        {'title':'how to get away with murder',
        'body':'This is how i got away'
        },
        {'title':'Tempor excepteur aute voluptate ea pariatur eiusmod exercitation.',
        'body':'''Deserunt ullamco elit laboris ullamco ea laboris. Anim sit occaecat qui esse occaecat irure pariatur nulla ad excepteur enim. Elit ipsum sunt esse esse est ad ipsum nulla.'''
        },
    ],
    'mike':[
        {'title':'how I got rich selling people courses on how to be rich',
        'body':'Tempor occaecat est laborum in amet. Magna occaecat Lorem nulla officia ullamco cupidatat dolore fugiat est ea laborum. Aliquip aliquip veniam Lorem ipsum nostrud deserunt officia irure est voluptate do aliquip. Id ea sit labore eiusmod exercitation cillum sit irure tempor anim quis. Mollit culpa sit nisi qui magna excepteur Lorem ipsum magna. Elit deserunt culpa tempor dolore ea aliquip.'
        },
        {'title':'Tempor excepteur aute voluptate ea pariatur eiusmod exercitation.',
        'body':'''Deserunt ullamco elit laboris ullamco ea laboris. Anim sit occaecat qui esse occaecat irure pariatur nulla ad excepteur enim. Elit ipsum sunt esse esse est ad ipsum nulla.'''
        },
    ]
}

class getUsers(Resource):
    def get(self,user_id):
        return {'hello': 'users all users'}
    
    def put(self,user_id):
        return {'users': 'updating the user'}

    def post(self):
        return {'users': 'creating a user'}

    def delete(self,user_id):
        return {'users': 'deleting a user'}

class userBlogs(Resource): 
    def get(self):
        return {'users': blogs}

    def put(self,blog_id):
        return {'users': blogs}

    def post(self):
        return {'users': blogs}

    def delete(self,blog_id):
        return {'users': blogs}

class home(Resource):
    def get(self):
        return {'users':users}

api.add_resource(getUsers, '/users')
api.add_resource(userBlogs, '/user-blogs')
api.add_resource(home, '/')

if __name__ == '__main__':
    app.run(debug=True)
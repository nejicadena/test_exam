from resources.example_resource import CreateComent
from resources.user import User,UserRegister
from resources.ex import UserList,CommetsList, PostList

def initialize_routes(api):
    api.add_resource(User, '/login')
    api.add_resource(UserRegister, '/signup')
    api.add_resource(UserList, '/user_list')
    api.add_resource(CommetsList, '/comment_list')
    api.add_resource(PostList, '/post_list')
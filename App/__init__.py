from flask import Flask
''' 包内初始化app，加载路由'''

#from App.views import init_route
#from App.views import blue
from App.views import init_view


def create_app():
    app = Flask(__name__)
    #init_route(app)
    init_view(app)
    return app

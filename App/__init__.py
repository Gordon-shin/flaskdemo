from flask import Flask

from App.ext import init_ext
from App.settings import envs

''' 包内初始化app，加载路由'''

#from App.views import init_route
#from App.views import blue
from App.views import init_view
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)


    #url全格式  数据库+驱动：//用户名：密码@主机：端口/具体哪个库
   # app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///sqlite.db"
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(envs.get("develop"))
    init_ext(app)
    init_view(app)
    return app

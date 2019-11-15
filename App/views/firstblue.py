from flask import Blueprint

from App.models import *
'''模型（bean）导入'''

blue = Blueprint('blue',__name__)
@blue.route('/',)
def index():
    return '我是蓝图的主页'

@blue.route('/h')
def h1():
    return '<h1>hi<h1>'

@blue.route('/createdb/')
def create_db():
    db.create_all()
    return  '创建成功'

@blue.route('/adduser')
def add_user():
    user = User()
    user.username = 'tom'


    db.session.add(user)
    db.session.commit()
    return '添加成功'

@blue.route('/update')
def update_database():
   pass

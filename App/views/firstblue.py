from flask import Blueprint
blue = Blueprint('blue',__name__,)
@blue.route('/')
def index():
    return '我是蓝图的主页'

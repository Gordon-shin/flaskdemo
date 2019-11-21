from flask_sqlalchemy import SQLAlchemy
'''flask中拓展控制'''
db = SQLAlchemy()

def init_ext(app):
	'''传入app'''
	db.init_app(app=app)#后加载

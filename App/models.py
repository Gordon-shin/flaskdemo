from App.ext import db
'''ORM object relative mapping 控制'''
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username =db.Column(db.String(16))
	def save(self):
		db.session.add(self)
		db.session.commit()

class Classes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	class_name = db.Column(db.String(255))
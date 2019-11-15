# def init_route(app):  # 传递参数来导入
#     @app.route('/')
#     def hello_world():
#         return 'Hello World!'
#view
from .firstblue import blue
def init_view(app):
    app.register_blueprint(blue)


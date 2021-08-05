# flask_web/app.py
from flask import Flask, render_template, request, jsonify, Response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()

app = Flask(__name__)

app.config.from_object("config.Config")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api = Api(app)

db.init_app(app)

csrf = CSRFProtect(app)

with app.app_context():
    import routes.todo
    import routes.weather
    import routes.blog
    import routes.api.blog
    from models.models import User, Article, Category, UserInfo
    from forms.forms import LoginForm, RegistrationForm

    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
import os
from app import app, api, db
from flask import render_template, request, Response, redirect, url_for, flash
from config import Config, articles
from flask_restful import Resource, Api
from models.models import Article, User, UserInfo
from forms.forms import RegistrationForm, LoginForm


@app.route('/', methods=["GET"])
def homepage():
    articles = Article.query.all()
    return render_template('cars/index.html', config=Config, articles=articles)


@app.route('/article/<string:slug>')
def article_details(slug):
    article = Article.query.filter_by(slug=slug).first()
    return render_template('cars/details.html', article=article)


@app.route('/article/create')
def article_create():
    return render_template('cars/article_create.html')


@app.route('/article/store', methods=["POST"])
def article_store():
    data = request.form
    img = request.files['img']
    if img:
        img.save(os.path.join(Config.UPLOAD_PATH, img.filename))
        path = "/" + Config.UPLOAD_PATH + img.filename

    article = Article(
        title=data.get('title'),
        slug=data.get('slug'),
        author_id=1,
        description=data.get('description'),
        short_description=data.get('short_description'),
        img=path
    )

    db.session.add(article)
    db.session.commit()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        new_register = UserInfo(login=request.form.login, password=request.form.password)
        db.session.add(new_register)
        db.session.commit()
        flash('Thanks for registration')
        return redirect(url_for('login'))
    return render_template('cars/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('cars/login.html', form=form)

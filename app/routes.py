from flask import Flask, render_template, request, redirect, url_for
from app import app
from app.forms import *
from app.models import *
from app import db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/przedmioty')
def showBooks():
   przedmioty = Przedmiot.query.all()
   return render_template("przedmioty.html", przedmioty=przedmioty)

@app.route('/przedmioty/add/',methods=['GET','POST'])
def addBook():
    form = PrzedmiotForm()
    if form.validate_on_submit():
        przedmiot = Przedmiot(nazwa=form.nazwa.data, ects=form.ects.data)
        db.session.add(przedmiot)
        db.session.commit()
        return redirect(url_for('showBooks'))
    else:
       return render_template('addPrzedmiot.html', form=form)

@app.route("/przedmioty/<int:przedmiot_id>/edit/", methods = ['GET', 'POST'])
def editPrzedmiot(przedmiot_id):
    form = PrzedmiotForm()
    editedPrzedmiot = db.session.query(Przedmiot).filter_by(id=przedmiot_id).one()
    if request.method == 'POST':
        editedPrzedmiot.nazwa=request.form['nazwa']
        editedPrzedmiot.ects=request.form['ects']
        db.session.add(editedPrzedmiot)
        db.session.commit()
        return redirect(url_for('showBooks'))
    else:
       return render_template('editPrzedmiot.html', przedmiot = editedPrzedmiot, form=form)

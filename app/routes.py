from flask import Flask, render_template, request, redirect, url_for
from app import app
from app.forms import *
from app.models import *
from app import db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/przedmioty')
def showPrzedmioty():
   przedmioty = Przedmiot.query.all()
   return render_template("przedmioty.html", przedmioty=przedmioty)

@app.route('/przedmioty/add/',methods=['GET','POST'])
def addPrzedmiot():
    form = PrzedmiotForm()
    if form.validate_on_submit():
        przedmiot = Przedmiot(nazwa=form.nazwa.data, ects=form.ects.data)
        db.session.add(przedmiot)
        db.session.commit()
        return redirect(url_for('showPrzedmioty'))
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
        return redirect(url_for('showPrzedmioty'))
    else:
       return render_template('editPrzedmiot.html', przedmiot = editedPrzedmiot, form=form)

@app.route('/books/<int:przedmiot_id>/delete/', methods = ['GET','POST'])
def deletePrzedmiot(przedmiot_id):
    przedmiotToDelete = db.session.query(Przedmiot).filter_by(id=przedmiot_id).one()
    db.session.delete(przedmiotToDelete)
    db.session.commit()
    return redirect(url_for('showPrzedmioty'))
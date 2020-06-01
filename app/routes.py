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

@app.route('/przedmioty/<int:przedmiot_id>/delete/', methods = ['GET','POST'])
def deletePrzedmiot(przedmiot_id):
    przedmiotToDelete = db.session.query(Przedmiot).filter_by(id=przedmiot_id).one()
    db.session.delete(przedmiotToDelete)
    db.session.commit()
    return redirect(url_for('showPrzedmioty'))


@app.route('/sale')
def showSale():
   sale = Sala.query.all()
   return render_template("sale.html", sale=sale)

@app.route('/sale/add/',methods=['GET','POST'])
def addSala():
    form = SalaForm()
    if form.validate_on_submit():
        sala = Sala(nr=form.nr.data, miejsca=form.miejsca.data)
        db.session.add(sala)
        db.session.commit()
        return redirect(url_for('showSale'))
    else:
       return render_template('addSala.html', form=form)

@app.route("/sale/<int:sala_id>/edit/", methods = ['GET', 'POST'])
def editSala(sala_id):
    form = SalaForm()
    editedSala = db.session.query(Sala).filter_by(id=sala_id).one()
    if request.method == 'POST':
        editedSala.nr=request.form['nr']
        editedSala.miejsca=request.form['miejsca']
        db.session.add(editedSala)
        db.session.commit()
        return redirect(url_for('showSale'))
    else:
       return render_template('editSala.html', sala = editedSala, form=form)

@app.route('/sale/<int:sala_id>/delete/', methods = ['GET','POST'])
def deleteSala(sala_id):
    salaToDelete = db.session.query(Sala).filter_by(id=sala_id).one()
    db.session.delete(salaToDelete)
    db.session.commit()
    return redirect(url_for('showSale'))



@app.route('/tytuly')
def showTytuly():
   tytuly = Tytul.query.all()
   return render_template("tytuly.html", tytuly=tytuly)

@app.route('/tytuly/add/',methods=['GET','POST'])
def addTytul():
    form = TytulForm()
    if form.validate_on_submit():
        tytul = Tytul(tytulnauk=form.tytulnauk.data)
        db.session.add(tytul)
        db.session.commit()
        return redirect(url_for('showTytuly'))
    else:
       return render_template('addTytul.html', form=form)

@app.route("/tytuly/<int:tytul_id>/edit/", methods = ['GET', 'POST'])
def editTytul(tytul_id):
    form = TytulForm()
    editedTytul = db.session.query(Tytul).filter_by(id=tytul_id).one()
    if request.method == 'POST':
        editedTytul.tytulnauk=request.form['tytulnauk']
        db.session.add(editedTytul)
        db.session.commit()
        return redirect(url_for('showTytuly'))
    else:
       return render_template('editTytul.html', tytul = editedTytul, form=form)

@app.route('/tytuly/<int:tytul_id>/delete/', methods = ['GET','POST'])
def deleteTytul(tytul_id):
    tytulToDelete = db.session.query(Tytul).filter_by(id=tytul_id).one()
    db.session.delete(tytulToDelete)
    db.session.commit()
    return redirect(url_for('showTytuly'))




@app.route('/prowadzacy')
def showProwadzacy():
   prowadzacy = Prowadzacy.query.all()
   return render_template("prowadzacy.html", prowadzacy=prowadzacy)

@app.route('/prowadzacy/add/',methods=['GET','POST'])
def addProwadzacy():
    form = ProwadzacyForm()
    if form.is_submitted():
        tytul = db.session.query(Tytul).filter_by(tytulnauk=form.tytul.data).one()
        prowadzacy = Prowadzacy(imie=form.imie.data, nazwisko=form.nazwisko.data, tytul=tytul)
        db.session.add(prowadzacy)
        db.session.commit()
        return redirect(url_for('showProwadzacy'))
    else:
       return render_template('addProwadzacy.html', form=form)

@app.route("/prowadzacy/<int:prowadzacy_id>/edit/", methods = ['GET', 'POST'])
def editProwadzacy(prowadzacy_id):
    form = ProwadzacyForm()
    editedProwadzacy = db.session.query(Prowadzacy).filter_by(id=prowadzacy_id).one()
    if request.method == 'POST':
        tytul = db.session.query(Tytul).filter_by(tytulnauk=request.form['tytul']).one()
        editedProwadzacy.imie=request.form['imie']
        editedProwadzacy.nazwisko=request.form['nazwisko']
        editedProwadzacy.tytul=tytul
        db.session.add(editedProwadzacy)
        db.session.commit()
        return redirect(url_for('showProwadzacy'))
    else:
       return render_template('editProwadzacy.html', prowadzacy = editedProwadzacy, form=form)

@app.route('/prowadzacy/<int:prowadzacy_id>/delete/', methods = ['GET','POST'])
def deleteProwadzacy(prowadzacy_id):
    prowadzacyToDelete = db.session.query(Prowadzacy).filter_by(id=prowadzacy_id).one()
    db.session.delete(prowadzacyToDelete)
    db.session.commit()
    return redirect(url_for('showProwadzacy'))
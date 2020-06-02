@app.route('/zajecia')                      #TODO tutaj pozmieniac zeby dzialalo ORAZ dodac 3 templatki     inna tabela z kluczem obcym to prowadzacy
def showzajecia():
   zajecia = zajecia.query.all()
   return render_template("zajecia.html", zajecia=zajecia)

@app.route('/zajecia/add/',methods=['GET','POST'])
def addzajecia():
    form = zajeciaForm()
    if form.is_submitted():
        prowadzacy = db.session.query(Prowadzacy).filter_by(tytulnauk=form.tytul.data).one()  #prowadzacy wybierany wg nazwiska ale nizej dodawany do db jest caly obiekt
        tytul = db.session.query(Przedmiot).filter_by(nazwa=form.nazwa.data).one()  #przedmiot wg nazwy
        tytul = db.session.query(Sala).filter_by(nr=form.nr.data).one()  #sala wg numeru
        zajecia = Zajecie(prowadzacy=prowadzacy, przedmiot=przedmiot, sala=sala, dzien=form.dzien.data, godzina=form.godzina.data)  #TODO regex na godzine validate
        db.session.add(zajecia)
        db.session.commit()
        return redirect(url_for('showZajecia'))
    else:
       return render_template('addZajecia.html', form=form)

@app.route("/zajecia/<int:zajecia_id>/edit/", methods = ['GET', 'POST'])
def editZajecia(zajecia_id):
    form = ZajecieForm()
    editedZajecia = db.session.query(Zajecie).filter_by(id=zajecia_id).one()
    if request.method == 'POST':
        prowadzacy = db.session.query(Prowadzacy).filter_by(nazwisko=request.form['prowadzacy']).one()  #prowadzacy wybierany wg nazwiska ale nizej dodawany do db jest caly obiekt
        przedmiot = db.session.query(Przedmiot).filter_by(nazwa=request.form['przedmiot']).one()  #przedmiot wg nazwy
        sala = db.session.query(Sala).filter_by(nr=request.form['sala']).one()  #sala wg numeru
        editedZajecia.dzien=request.form['dzien']
        editedZajecia.godzina=request.form['godzina']
        editedZajecia.prowadzacy=prowadzacy
        editedZajecia.przedmiot=przedmiot
        editedZajecia.sala=sala
        db.session.add(editedZajecia)
        db.session.commit()
        return redirect(url_for('showZajecia'))
    else:
       return render_template('editZajecia.html', zajecia = editedZajecia, form=form)

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


@app.route('/zajecia/<int:zajecia_id>/delete/', methods = ['GET','POST'])
def deleteZajecia(zajecia_id):
    zajeciaToDelete = db.session.query(Zajecie).filter_by(id=zajecia_id).one()
    db.session.delete(zajeciaToDelete)
    db.session.commit()
    return redirect(url_for('showZajecia'))
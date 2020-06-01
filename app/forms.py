from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
from app.models import Tytul, Prowadzacy, Przedmiot, Sala

class PrzedmiotForm(FlaskForm):
    nazwa = StringField('Nazwa', validators=[DataRequired()])
    ects = StringField('Ects', validators=[DataRequired()])
    submit = SubmitField('Dodaj')
    
class SalaForm(FlaskForm):
    nr = StringField('Nr', validators=[DataRequired()])
    miejsca = StringField('Ilosc miejsc', validators=[DataRequired()])
    submit = SubmitField('Dodaj')

class TytulForm(FlaskForm):
    tytulnauk = StringField('Nazwa', validators=[DataRequired()])
    submit = SubmitField('Dodaj')    

class ProwadzacyForm(FlaskForm):
    imie = StringField('Imie', validators=[DataRequired()])
    nazwisko = StringField('Nazwisko', validators=[DataRequired()])
    tytul = SelectField('Tytul naukowy', choices = [(t.tytulnauk) for t in Tytul.query.order_by('tytulnauk')])
    submit = SubmitField('Dodaj')

class ZajecieForm(FlaskForm):
    prowadzacy = SelectField('Prowadzacy', choices = [(p.nazwisko) for p in Prowadzacy.query.order_by('nazwisko')])
    przedmiot = SelectField('Przedmiot', choices = [(p.nazwa) for p in Przedmiot.query.order_by('nazwa')])
    sala = SelectField('Sala', choices = [(s.nr) for s in Sala.query.order_by('nr')])
    dzien = SelectField('Dzien tygodnia', choices = [('poniedzialek'),('wtorek'),('sroda'),('czwartek'),('piatek')])
    godzina = StringField('Godzina', validators=[DataRequired()])
    submit = SubmitField('Dodaj')
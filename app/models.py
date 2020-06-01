from datetime import datetime
from app import db

class Przedmiot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(120), index=True, unique=True)
    ects = db.Column(db.String(64), index=True, unique=False)
    zajecia = db.relationship('Zajecie', backref='przedmiot', lazy='dynamic')

    def __repr__(self):
        return '<Przedmiot {}>'.format(self.nazwa)

class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nr = db.Column(db.String(64), index=True, unique=True)
    miejsca = db.Column(db.String(64), index=True, unique=False)
    zajecia = db.relationship('Zajecie', backref='sala', lazy='dynamic')

    def __repr__(self):
        return '<Sala {}>'.format(self.nr)

class Prowadzacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imie = db.Column(db.String(64), index=True, unique=False) 
    nazwisko = db.Column(db.String(64), index=True, unique=False)
    tytul_id = db.Column(db.Integer, db.ForeignKey('tytul.id'),nullable=False)
    zajecia = db.relationship('Zajecie', backref='prowadzacy', lazy='dynamic')

    def __repr__(self):
        return '<Prowadzacy {}>'.format(self.nazwisko)

class Tytul(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tytulnauk = db.Column(db.String(64), index=True, unique=True) 
    prowadzacy = db.relationship('Prowadzacy', backref='tytul', lazy='dynamic')

    def __repr__(self):
        return '<Tytul {}>'.format(self.tytulnauk)

class Zajecie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dzien = db.Column(db.String(64))
    godzina = db.Column(db.String(32))
    prowadzacy_id = db.Column(db.Integer, db.ForeignKey('prowadzacy.id'))
    przedmiot_id = db.Column(db.Integer, db.ForeignKey('przedmiot.id'))
    sala_id = db.Column(db.Integer, db.ForeignKey('sala.id'))

    def __repr__(self):
        return '<Zajecia {}>'.format(self.dzien)
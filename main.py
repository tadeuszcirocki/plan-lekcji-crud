from app import app, db
from app.models import Prowadzacy, Tytul, Zajecie, Przedmiot, Sala

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Prowadzacy': Prowadzacy, 'Tytul': Tytul, 'Zajecie': Zajecie, 'Przedmiot': Przedmiot, 'Sala': Sala}
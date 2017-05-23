"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, g, flash
from FlaskWebProject3 import app

import sqlite3

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


pyt1 = {
   'question' : 'Plec:',
   'fields'   : ['Kobieta', 'Mezczyzna']
}

pyt2 = {
   'question' : 'Wiek:',
   'fields'   : [n for n in range(18,120)]
}

pyt3 = {
   'question' : 'Waga w kilogramach:',
   'fields'   : [n for n in range(40,200)]
}

pyt4 = {
   'question' : 'Wzrost w centymetrach:',
   'fields'   : [n for n in range(130,230)]
}

pyt5 = {
   'question' : 'Czy w przeszlosci przebyl Pan/Pani zawal?',
   'fields'   : ['Tak', 'Nie']
}

pyt6 = {
   'question' : 'Czy zdiagnozowano u Pana/Pani nadcisnienie?',
   'fields'   : ['Tak', 'Nie']
}

pyt7 = {
   'question' : 'Czy zdiagnozowano u Pana/Pani chorobe wiencowa?',
   'fields'   : ['Tak', 'Nie']
}


pyt8 = {
   'question' : 'Czy zdiagnozowano u Pana/Pani cukrzyce?',
   'fields'   : ['Tak', 'Nie']
}

pyt9 = {
   'question' : 'Czy zdiagnozowano u Pana/Pani zwiekszony poziom cholesterolu?',
   'fields'   : ['Tak', 'Nie']
}

pyt10 = {
   'question' : 'Czy pali Pan/Pani papierosy?',
   'fields'   : ['Tak', 'Nie']
}

pyt11 = {
   'question' : 'Czy uprawia Pan/Pani regularnie jakis sport (min. 3 razy w tygodniu po 30 min)?',
   'fields'   : ['Tak', 'Nie']
}

pyt12 = {
   'question' : 'Czy czesto spozywa Pan/Pani smazowne potrawy, slodycze?',
   'fields'   : ['Tak', 'Nie']
}

pyt13 = {
   'question' : 'Czy czesto jest Pan/Pani narazony na stres?',
   'fields'   : ['Tak', 'Nie']
}

pyt14 = {
   'question' : 'Czy w Pana/Pani rodzine wystepowaly zawaly serca?',
   'fields'   : ['Tak', 'Nie']
}

odpowiedzi = {
   'tak' : 12,
   'nie'   : 33
}
DATABASE = 'database.db'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

filename = 'data.txt'

@app.route('/')
def root():
    return render_template('poll.html', pyt1=pyt1, pyt2=pyt2, pyt3=pyt3, pyt4=pyt4, pyt5=pyt5, pyt6=pyt6, pyt7=pyt7, pyt8=pyt8, pyt9=pyt9, pyt10=pyt10, pyt11=pyt11, pyt12=pyt12, pyt13=pyt13, pyt14=pyt14)
 
def convert(response):
    if response =='Tak':
        return 1
    elif response =='Nie':
        return 0
    else:
        raise
def convert_gender(response):
    if response =='Kobieta':
        return 1
    elif response =='Mezczyzna': 
        return 0
    else:
        raise



def add_polls():
    db = get_db()
    db.execute("insert into Dane (Plec,Wiek,Waga,Wzrost,PrzebytyZawal,Nadcisnienie,ChorobaWiencowa,Cukrzyca,PodwyzszonyCholesterol,Palenie,RegularnySport,NiewlasciwaDieta,Stres,ZawalySercaWRodzinie) values ('%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d')" % 
        (convert_gender(request.args.get('field')), 
        int(request.args.get('field2')),
        int(request.args.get('field3')), 
        int(request.args.get('field4')),
        convert(request.args.get('field5')),
        convert(request.args.get('field6')), 
        convert(request.args.get('field7')), 
        convert(request.args.get('field8')),
        convert(request.args.get('field9')),
        convert(request.args.get('field10')),
        convert(request.args.get('field11')), 
        convert(request.args.get('field12')), 
        convert(request.args.get('field13')), 
        convert(request.args.get('field14'))))
    db.commit()
    flash('New entry was successfully posted')

@app.route('/poll')
def poll():
    add_polls()
 
    return render_template('thankyou.html', data=pyt1)



@app.route('/results')
def results():
    return render_template('results.html', data=pyt1, votes=odpowiedzi)



if __name__ == "__main__":
    app.run(debug=True)


@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

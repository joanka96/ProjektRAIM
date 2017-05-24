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


plec = {
   'question' : 'Plec:',
   'fields'   : ['Kobieta', 'Mezczyzna']
}

wiek = {
   'question' : 'Wiek:',
   'fields'   : [n for n in range(18,105)]
}

waga = {
   'question' : 'Waga w kilogramach:',
   'fields'   : [n for n in range(40,200)]
}

wzrost = {
   'question' : 'Wzrost w centymetrach:',
   'fields'   : [n for n in range(130,230)]
}

przebytyZawal = {
   'question' : 'Czy w przeszlosci przebyl Pan/Pani zawal?',
   'fields'   : ['Tak', 'Nie']
}

nadcisnienie = {
   'question' : 'Czy zdiagnozowano u Pana/Pani nadcisnienie?',
   'fields'   : ['Tak', 'Nie']
}

chorobaWiencowa = {
   'question' : 'Czy zdiagnozowano u Pana/Pani chorobe wiencowa?',
   'fields'   : ['Tak', 'Nie']
}


cukrzyca = {
   'question' : 'Czy zdiagnozowano u Pana/Pani cukrzyce?',
   'fields'   : ['Tak', 'Nie']
}

cholesterol = {
   'question' : 'Czy zdiagnozowano u Pana/Pani zwiekszony poziom cholesterolu?',
   'fields'   : ['Tak', 'Nie']
}

palenie= {
   'question' : 'Czy pali Pan/Pani papierosy?',
   'fields'   : ['Tak', 'Nie']
}

sport = {
   'question' : 'Ile razy w tygodniu uprawia Pan/Pani jakis sport (min. 30 min)?',
   'fields'   : ['0', '1', '2', '3', '4 i wiecej']
}

dieta = {
   'question' : 'Czy czesto spozywa Pan/Pani smazowne potrawy, slodycze?',
   'fields'   : ['Tak', 'Nie']
}

stres = {
   'question' : 'Czy czesto jest Pan/Pani narazony na stres?',
   'fields'   : ['Tak', 'Nie']
}

historia = {
   'question' : 'Czy w Pana/Pani biologicznej rodzine (rodzice, dziadkowie, rodznstwo, dzieci) wystepowaly zawaly serca?',
   'fields'   : ['Tak', 'Nie', 'Nie wiem']
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
    return render_template('poll.html', pyt1=plec, pyt2=wiek, pyt3=waga, pyt4=wzrost, pyt5=przebytyZawal, pyt6=nadcisnienie, pyt7=chorobaWiencowa, pyt8=cukrzyca, pyt9=cholesterol, pyt10=palenie, pyt11=sport, pyt12=dieta, pyt13=stres, pyt14=historia)
 
def convert(response):
    if response =='Tak':
        return 1
    elif response =='Nie':
        return 0
    elif response =='Nie wiem':
        return 2
    elif response =='0':
        return 0
    elif response =='1':
        return 1
    elif response =='2':
        return 2
    elif response =='3':
        return 3
    elif response =='4 i wiecej':
        return 4
    else:
        raise
def convert_gender(response):
    if response =='Kobieta':
        return 0
    elif response =='Mezczyzna': 
        return 1
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
 
    return render_template('thankyou.html', data=wiek)



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

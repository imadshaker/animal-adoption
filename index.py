# Copyright 2023 <Imad Bouarfa, BOUI24039303>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, request, redirect, url_for
from flask import render_template
from flask import g
from database import Database

app = Flask(__name__, static_url_path="", static_folder="static")


@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Récupérer les données du formulaire
    nom = request.form['nom']
    espece = request.form['espece']
    race = request.form['race']
    age = request.form['age']
    description = request.form['description']
    email = request.form['email']
    recuperation = request.form['recuperation']
    ville = request.form['ville']
    code_postal = request.form['code']

    db = get_db()
    try:
        animal_id = db.add_animal(nom, espece, race, age, description, email, recuperation, ville, code_postal)
        # Rediriger vers la page de l'animal après l'ajout
        return redirect(url_for('animal_page', animal_id=animal_id))
    except Exception as e:
        error_message = str(e)
        return redirect(url_for('error', message=error_message))

@app.route('/error')
def error():
    message = request.args.get('message')
    return render_template('error.html', message=message)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()

@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/')
def index():
    db = get_db()
    random_animals = db.get_random_animaux()
    return render_template('index.html', animals=random_animals)


@app.route('/animaux')
def show_animals():
    db = get_db()
    animals = db.get_animaux()
    return render_template('index.html', animals=animals)

def show_animals():
    db = get_db()
    animals = db.get_animaux()
    return render_template('index.html', animals=animals)

@app.route('/animal/<int:animal_id>')
def animal_page(animal_id):
    db = get_db()
    animal = db.get_animal(animal_id)
    if animal is None:
        # Gérer le cas où l'animal n'est pas trouvé
        return "Animal non trouvé", 404
    return render_template('animal_page.html', animal=animal)

@app.route('/rechercher')
def rechercher_animaux():
    terme_de_recherche = request.args.get('q')

    if not terme_de_recherche:
        # Si le terme de recherche est vide, renvoyez un message approprié ou redirigez l'utilisateur
        return "Veuillez saisir un terme de recherche."

    db = get_db()
    animaux_recherches = db.rechercher_animaux(terme_de_recherche)

    if not animaux_recherches:
        # Si la liste des résultats est vide, indiquez que rien n'a été trouvé
        return "Aucun animal trouvé pour votre recherche : " + terme_de_recherche

    return render_template('resultats_recherche.html', animaux=animaux_recherches)


if __name__ == "__main__":
    app.run(debug=True)
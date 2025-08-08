from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import ollama
import json
# https://ollama.com/blog/structured-outputs
# from ollama import chat 
# from pydantic import BaseModel

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"], methods=["GET", "POST", "OPTIONS"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Dev/eval-mns-NUNGE/cocktails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# class CocktailClass(BaseModel):
#     name: str
#     ingredients: str
#     description: str
#     music: str

class Cocktail(db.Model):
    __tablename__ = "cocktails"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    music = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Cocktail {self.name}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients,
            "description": self.description,
            "music": self.music,
            "created_at": self.created_at
        }
    

def load_cocktails():
    return db.session.query(Cocktail).order_by(Cocktail.name.asc()).all()

def save_cocktail(cocktail):
    db.session.add(cocktail)
    db.session.commit()

@app.route('/cocktails/<int:id>')
def get_cocktail(id):
    cocktail = db.session.get_one(Cocktail, { "id": id })

    return jsonify(cocktail)

@app.route('/cocktails')
def get_all_cocktails():
    cocktails = Cocktail.query.order_by(Cocktail.name.asc()).all()

    return jsonify([ c.to_dict() for c in cocktails])

@app.route('/cocktails/new', methods=['POST', 'OPTIONS'])
def create_cocktail():
    if request.method == 'POST':
        data = request.get_json()
        context = data.get('context') if data else ""

        prompt = f"""
                Tu es un barman. Tu dois inventer un cocktail en suivant les consignes suivantes :

                # Consignes
                - Utilise ce contexte : {context}
                - Tu dois inventer un nom à ce cocktail
                - Tu dois lister les ingrédients
                - Tu dois proposer une musique à écouter pendant la dégustation du cocktail avec son titre et son interprète
                - Tu dois décrire ce cocktail et inventé une petite histoire en quelques lignes
                - Tu dois retourner le tout sous forme d'un objet Cocktail décrit ci-après:

                ## Structure objet Cocktail
                - name: le nom inventé
                - ingredients: les ingrédients
                - description: la petite histoire que tu as créé
                - music: une ambiance musicale que tu auras choisi pour déguster ce cocktail

                # Donnée de retour :
                - Générez une réponse formatée comme un dictionnaire Python avec les clés 'name', 'decription', 'ingredients', et 'music', qui sont toutes des chaines de caractères.
                    Exemple de format attendu: {{"name": "Nom du cocktail", "ingredients": "liste des ingrédients", "description":"description du cocktail ou petite histoire", "music": "musique que l'on peut écouter pour manger spécifiquement ce cocktail" }}
                - ne retourne rien d'autre que cet objet JSON en chaine de caractère, sans préciser le type avec les ```
        
            """
        
        response = ollama.generate(
            model='gemma3:4b',
            prompt=prompt
        )
        
        try:
            jsonstr = response.get('response')

            response = json.loads(jsonstr.replace("```json", "").replace("```", ""))

            cocktail = Cocktail(
                name=response.get('name'),
                description=response.get('description'),
                ingredients=response.get('ingredients'),
                music=response.get('music')
            )

            save_cocktail(cocktail)

            return jsonify({ 'status' : '200', 'message': 'New cocktail created' })
        except Exception as e:
            return jsonify({ 'status': '500', 'error': 'Unable to create cocktail', "error": e})

    return jsonify({ 'status': 401, 'error': 'Unauthorized' })


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
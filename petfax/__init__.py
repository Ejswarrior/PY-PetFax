from flask import Flask
from flask import (Blueprints, render_template )

def create_app():
    app = Flask(__name__)
    
    
    import json

    pets = json.load(open('pets.json'))
    print pets

    @app.route('/')
    def hello():
        return render_template('index.html', pets=pets)

    from . import pet
    app.register_blueprint(pet.bp)

    return app
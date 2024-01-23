#!/usr/bin/env python3

from flask import Flask, make_response,render_template
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal=Animal.query.get(id)
    animal_data={
        'name':animal.name,
        'species':animal.species,
        'zookeeper':animal.zookeeper.name if animal.zookeeper else None,
        'enclosure':animal.enclosure.environment if animal.enclosure else None
    }
    response=make_response(render_template(+'animal.html',animal_data=animal_data))

    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper=Zookeeper.query.get(id)
    zookeeper_data = {
        'name': zookeeper.name,
        'birthday': zookeeper.birthday,
        'animals': [animal.name for animal in zookeeper.animals]
    }
    response=make_response(render_template('zookeeper.html', zookeeper_data=zookeeper_data))
    response.headers['Content-Type'] = 'text/html'

    return response
    
@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure=Enclosure.query.get(id)
    enclosure_data={
        'environment': enclosure.environment,
        'open_to_visitors': enclosure.open_to_visitors,
        'animals': [animal.name for animal in enclosure.animals]
    }
    response=make_response(render_template('enclosure.html',enclosure_data=enclosure_data))
    response.headers['Content-Type']='text/html'

    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)

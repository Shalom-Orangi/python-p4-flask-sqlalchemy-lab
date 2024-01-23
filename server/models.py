from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    birthday=db.Column(db.Date,nullable=False)

    #relationship
    animals=db.relationship('Animal',backref='zookeeper')
    def __repr__(self):
        return f'<Animal{self.name},{self.birthday}>'
    
class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment=db.column(db.String(255),nullable=False)
    open_to_visitors=db.Column(db.Boolean,default=True)

    #relationship
    animals=db.relationship('Animal',backref='enclosure')

    def __repr__(self):
        return f'<{self.environment},{self.open_to_visitors}>'
    
class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    species=db.Column(db.String)

    #foreign keys
    zookeeper_id=db.Column(db.Integer,db.ForeignKey('zookeepers.id'))
    enclosure_id=db.Column(db.Integer,db.ForeignKey('enclosures.id'))

    #relationships
    enclosures=db.relationship('Enclosure',backref='animal')
    zookeepers=db.relationship('Zookeeper',backref='animal')

    def __repr__(self):
        return f'<Animal{self.name},{self.species},{self.zookeeper_id},{self.enclosure_id}>'

from server import db

association_table = db.Table('projects',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    projects = db.relationship('Project', secondary=association_table)



class Project(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.Integer, primary_key=True)

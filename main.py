from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
class customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'(self.id, self.name, self.age)'

def create_db():
    with app.app_context():
        db.create_all()



@app.route("/")
def home():
    return "Hello World!"
if __name__ == '__main__':
    create_db()
    app.run(debug=True)
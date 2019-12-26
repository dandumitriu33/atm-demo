from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atm.db'
db = SQLAlchemy(app)


class Atm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer, nullable=False)
    card_type = db.Column(db.String, default='')
    card_pin = db.Column(db.Integer, nullable=False)
    holder_name = db.Column(db.String, default='')
    bank_name = db.Column(db.String, default='')
    account_name = db.Column(db.String, default='')
    account_number = db.Column(db.String, default='')
    balance = db.Column(db.Float, default=0)
    currency = db.Column(db.String, default='')
    failed_pin_attempts = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Card %r>' % self.id


def get_card_info(card_id):
    result = Atm.query.filter_by(card_id=card_id).first()
    return result


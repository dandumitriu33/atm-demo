from flask import Flask, render_template, request, redirect, url_for
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

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        entry_card = request.form['card']
        entry_card_type = request.form['card-type']
        entry_card_pin = request.form['card-pin']
        entry_holder_name = request.form['holder-name']
        entry_bank_name = request.form['bank-name']
        entry_account_name = request.form['account-name']
        entry_account_number = request.form['account-number']
        entry_balance = request.form['balance']
        entry_currency = request.form['currency']
        new_entry = Atm(card_id=entry_card,
                        card_type=entry_card_type,
                        card_pin=entry_card_pin,
                        holder_name=entry_holder_name,
                        bank_name=entry_bank_name,
                        account_name=entry_account_name,
                        account_number=entry_account_number,
                        balance=entry_balance,
                        currency=entry_currency)
        try:
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for('admin'))
        except:
            return 'There was an issue adding the card.'

    else:
        # cards = Atm.query.order_by(Atm.card_id).all() # also add cards=cards in return and jinja
        return render_template('admin.html')


if __name__ == "__main__":
    app.run(debug=True)

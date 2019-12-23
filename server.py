from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.orm.exc

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
        return '<Task %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_card = request.form['card-number']
        try:
            result = Atm.query.order_by(Atm.card_id).filter(Atm.card_id == user_card)
            # todo if type result == none raise value error + Value Error page
            # tried several ways, could not find a valid one

            for item in result:
                inserted_card_id = item.card_id
            return redirect(url_for('enter_pin', card_id=inserted_card_id))
        except sqlalchemy.orm.exc.NoResultFound:
            return 'Card does not exist.'
        except:
            return render_template('invalid-card.html')
    else:
        return render_template('index.html')


@app.route('/invalid-card')
def invalid_card():
    return render_template('invalid-card.html')


@app.route('/<card_id>/enter-pin', methods=['GET', 'POST'])
def enter_pin(card_id):
    if request.method == 'GET':
        return render_template('enter-pin.html',
                               card_id=card_id)
    elif request.method == 'POST':
        card_id = int(request.form['card-id'])
        user_entered_pin = int(request.form['user-pin'])
        inserted_card_pin = 0
        result = Atm.query.order_by(Atm.card_id).filter(Atm.card_id == card_id)
        for item in result:
            inserted_card_pin = item.card_pin
        if user_entered_pin == inserted_card_pin:
            # todo clear db of failed attempts
            return redirect(url_for('options', card_id=card_id))
        else:
            # todo if failed attempts < 2
            # add to db +1 failed attempts
            # elif failed attempts >= 2
            # block card
            return render_template('invalid-pin.html', card_id=card_id)


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


@app.route('/<card_id>/options', methods=['GET', 'POST'])
def options(card_id):
    if request.method == 'POST':
        return 'under construction'
    else:
        return render_template('options.html',
                               card_id=card_id)


@app.route('/<card_id>/options/withdraw')
def withdraw(card_id):
    return render_template('withdraw.html',
                           card_id=card_id)


@app.route('/<card_id>/options/balance')
def balance(card_id):
    result = Atm.query.order_by(Atm.card_id).filter(Atm.card_id == card_id)
    for item in result:
        balance = item.balance
        currency = item.currency
    return render_template('balance.html',
                           card_id=card_id,
                           balance=balance,
                           currency=currency)


@app.route('/<card_id>/options/details')
def details(card_id):
    result = Atm.query.order_by(Atm.card_id).filter(Atm.card_id == card_id)
    for item in result:
        holder = item.holder_name
        type = item.card_type
        bank_name = item.bank_name
        bank_account = item.account_number
    return render_template('details.html',
                           card_id=card_id,
                           holder=holder,
                           type=type,
                           bank_name=bank_name,
                           bank_account=bank_account)


if __name__ == "__main__":
    app.run(debug=True)

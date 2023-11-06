from modules import sherlock_account
from utils.init import initializse
from database.handle import *
from flask import Flask, render_template, jsonify

app = Flask(__name__)


initializse()
db_init()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/actions/add/user')
def actions_add_user():
    return


@app.route('/get/sherlock')
def get_sherlock_username():
    # data = sherlock_account.getSherlock(username='hirushaadi')
    # sherlock_account.showSherlock(data=data)
    data = sherlock_account.returnSherlock(uname='hirushaadi')
    return jsonify(data)


if __name__ == "__main__":
    app.run('0.0.0.0', port=8090, debug=True)

from flask import Flask, render_template, url_for, request, g, abort, flash, url_for, redirect
from FDataBase import FDataBase
import sqlite3
import os


DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = "fdgfh78@#5?>gfhf89dx,v06k"

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path,'flsite.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


dbase = None
@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)

#устанавливаю соединение
@app.route("/", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        res = dbase.addUser(request.form['FullName'], request.form['Login'], request.form['Password'])
        if res:
            flash("Вы успешно зарегистрированы", "success")
            return redirect(url_for('Login'))
        else:
            flash("Ошибка при добавлении в БД", "error")
    else:
        flash("Неверно заполнены поля", "error")

    return render_template('add_users.html', menu = dbase.getMenu(), title="Регистрация")

#разрываю соединение
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run(debug=True)
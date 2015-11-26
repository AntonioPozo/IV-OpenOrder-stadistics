# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, escape, session, flash
from wtforms import Form, BooleanField, TextField, PasswordField, validators
import shelve
import sys
import logging

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

class RegistrationForm(Form):
	username = TextField('Nombre de Usuario', [validators.Length(min=4, max=25)])
	email = TextField('Dirección de email', [validators.Length(min=6, max=35)])
	password = PasswordField('Contraseña', [validators.Required(),validators.EqualTo('confirm', message='La contraseña debe coincidir con la repetición')])
	confirm = PasswordField('Repite la contraseña')
	accept_tos = BooleanField('Acepto las condiciones', [validators.Required()])

class LoginForm(Form):
	username = TextField('Usuario', [validators.Length(min=4, max=25)])
	password = PasswordField('Contraseña', [validators.Length(min=1, max=25)])

def addUser(nombre, email, passwd):
	usuarios = shelve.open('usuariosBD', 'c') # abrir la base de datos
	usuarios[str(nombre)]= {'pass':str(passwd)}
	usuarios.close()

def testLogin(nombre, passwd):
	usuarios = shelve.open('usuariosBD','r')
	user = usuarios.has_key(str(nombre))
	if user: # se ha encontrado el usuario
		u = usuarios.get(str(nombre))
		pswd = u.get('pass')
		if pswd == passwd:
			return True
	usuarios.close()
	return False;

@app.route('/', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		if testLogin(form.username.data, form.password.data):
			session['username'] = form.username.data
	return render_template('content.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
	# remove the username from the session if it's there
	session.pop('username', None)
	return redirect(url_for('login'))


@app.route('/registrate', methods=['GET', 'POST'])
def registro():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		addUser(form.username.data, form.email.data, form.password.data)
		session['username'] = form.username.data
		return render_template('content.html', form=form)
	# el registro no ha tenido éxito
	return render_template('registrate.html', form=form)







app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.debug = True	
    app.run(host='0.0.0.0')  


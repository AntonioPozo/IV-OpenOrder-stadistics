# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, escape, session, flash
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from pymongo import MongoClient

import sys




reload(sys)
sys.setdefaultencoding('utf-8')




app = Flask(__name__)

# session["historial"][2] = ""
# session["historial"][1] = ""
# session["historial"][0] = ""

def getCurrentUsername():
	return session['username']
def getCurrentEmail():
	return session['email']

def getCurrentPass():
	return session['pass']

def getCurrentEmail():
	return session['email']

def setSession(user, email, passwd):
	session["username"] = user
	session["email"] = email
	session["pass"] = passwd 

class RegistrationForm(Form):
	username = TextField('Nombre de Usuario', [validators.Length(min=4, max=25)])
	email = TextField('Dirección de email', [validators.Regexp('(\w+)@\w+(.\w+)+', message="El correo introducido no es correcto")])
	password = PasswordField('Contraseña', [validators.Required(),validators.EqualTo('confirm', message='La contraseña debe coincidir con la repetición')])
	confirm = PasswordField('Repite la contraseña')
	accept_tos = BooleanField('Acepto las condiciones', [validators.Required()])

class ModifyForm(Form):
	# username = TextField('Cambiar el Nombre de Usuario', [validators.Length(min=4, max=25)], default= session['username'])
	username = TextField('Cambiar el Nombre de Usuario', [validators.Length(min=4, max=25)], default=getCurrentUsername)
	email = TextField('Cambiar la Dirección de email', [validators.Length(min=6, max=35)], default=getCurrentEmail)
	password = PasswordField('Nueva Contraseña', [validators.Required(),validators.EqualTo('confirm', message='La contraseña debe coincidir con la repetición')], default=getCurrentPass)
	confirm = PasswordField('Repite la contraseña nueva', default=getCurrentPass)

class LoginForm(Form):
	username = TextField('Usuario', [validators.Length(min=4, max=25)])
	password = PasswordField('Contraseña', [validators.Length(min=1, max=25)])



def addUser(nombre, email, passwd):
	mongoClient = MongoClient('localhost',27017)
	db = mongoClient.UsuariosDAI
	collection = db.UsuariosDAI
	collection.insert({'nombre' : nombre, 'email' : email, 'pass' : passwd})
	
def modifyUser(newname, newemail, newpasswd):
	mongoClient = MongoClient('localhost',27017)
	db = mongoClient.UsuariosDAI
	collection = db.UsuariosDAI
	users = collection.find()
	collection.update({"nombre" : session['username']}, {"nombre" : newname, "email" : newemail, "pass" : newpasswd})
	# testear si esa operación ha tenido éxito o no
	session["username"] = newname
	session["email"] = newemail

# def testLogin(nombre, passwd):
# 	mongoClient = MongoClient('localhost',27017)
# 	db = mongoClient.UsuariosDAI
# 	collection = db.UsuariosDAI
# 	users = collection.find()
# 	for useri in users:
# 		if useri['nombre']==nombre and useri['pass']==passwd:
# 			setSession(useri['nombre'], useri['email'], useri['pass'])
# 			return True
# 	return False;

def testSingin(nombre, passwd):
	mongoClient = MongoClient('localhost',27017)
	db = mongoClient.UsuariosDAI
	collection = db.UsuariosDAI
	user = collection.find({"nombre" : nombre, "pass": passwd})
	# EL IF DE ABAJO COMPARA COSAS ABSURDAS, PORQUE SI LO HA ENCONTRADO ES QUE EXISTE Y POR TANTO NO TENGO QUE VOLVER A COMPARAR TODO
	# LO QUE PASA ES QUE NO SE PUEDE HACER IF USER RETURN TRUE ELSE RETURN FALSE
	if user[0]["nombre"]==nombre and user[0]["pass"]==passwd:
		setSession(user[0]["nombre"], user[0]["email"], user[0]["pass"])
		return True
	return False

def setHistorial(pagina):
	session["historial3"] = session.get("historial2")
	session["historial2"] = session.get("historial1")
	session["historial1"] = pagina 

@app.route('/', methods=['GET', 'POST'])
def login():
	setHistorial("content.html")
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		if testSingin(form.username.data, form.password.data):
			setSession(form.username.data, getCurrentEmail(), form.password.data)
			# session['email'] = form.email.data ESTO NO VALE, HACER LA CONSULTA
	return render_template('content.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
	# remove the username from the session if it's there
	session.pop('username', None)
	return redirect(url_for('login'))



@app.route('/registrate', methods=['GET', 'POST'])
def registro():
	setHistorial("registrate.html")
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		addUser(form.username.data, form.email.data, form.password.data)
		if testSingin(form.username.data, form.password.data):
			session['username'] = form.username.data
			session['email'] = form.email.data
		return render_template('content.html', form=form)
	# else:
	# 	algo ha ido mal con la base de datos
	# datos mal introducidos
	return render_template('registrate.html', form=form)


@app.route('/modifica', methods=['GET', 'POST'])
def modifica():
	setHistorial("modifica.html")
	form = ModifyForm(request.form)
	modifyUser(form.username.data, form.email.data, form.password.data)
	return render_template('modifica.html', form=form)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.debug = True	
    app.run(host='0.0.0.0')  


    # print("fuera")
	# sys.stdout.flush()


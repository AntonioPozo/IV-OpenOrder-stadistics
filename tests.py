
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
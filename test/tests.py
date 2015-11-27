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
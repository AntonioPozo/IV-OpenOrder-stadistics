# def testSingin(nombre, passwd):
# 	mongoClient = MongoClient('localhost',27017)
# 	db = mongoClient.UsuariosDAI
# 	collection = db.UsuariosDAI
# 	user = collection.find({"nombre" : nombre, "pass": passwd})
# 	# EL IF DE ABAJO COMPARA COSAS ABSURDAS, PORQUE SI LO HA ENCONTRADO ES QUE EXISTE Y POR TANTO NO TENGO QUE VOLVER A COMPARAR TODO
# 	# LO QUE PASA ES QUE NO SE PUEDE HACER IF USER RETURN TRUE ELSE RETURN FALSE
# 	if user[0]["nombre"]==nombre and user[0]["pass"]==passwd:
# 		setSession(user[0]["nombre"], user[0]["email"], user[0]["pass"])
# 		return True
# 	return False









import unittest
import os
# import webGestion
from HTMLParser import HTMLParser
import tempfile
from html5lib.sanitizer import HTMLSanitizerMixin

eti_html = 0
img = 0

class ComprobarEtiquetas(HTMLParser):
    def handle_starttag(self, tag, attrs):
		global eti_html
		global img
		if tag=='html':
			eti_html = 1
		if tag=='img':
			img = 1
	
# class TestMethods(unittest.TestCase):
# 	def setUp(self):
# 		self.db_fd, webGestion.app.config['DATABASE'] = tempfile.mkstemp()
# 		webGestion.app.config['TESTING'] = True
#         	self.app = webGestion.app.test_client()

#     	def tearDown(self):
#         	os.close(self.db_fd)
#         	os.unlink(webGestion.app.config['DATABASE'])
		
# 	def test_imagen(self):
# 		global img
# 		img = 0
# 		parser = ComprobarEtiquetas()
# 		archi_index= self.app.get('/index.html')
# 		assert 'html' in archi_index.data
	
# 	def test_htmlindex(self):
# 		global eti_html
# 		eti_html = 0
# 		parser = ComprobarEtiquetas()
# 		archi_index= self.app.get('/index.html')
# 		assert 'div' in archi_index.data

# 	def test_usuario(self):
# 		global img
# 		img = 0
# 		parser = ComprobarEtiquetas()
# 		archi_index= self.app.get('/index.html')
# 		assert 'h1' in archi_index.data

if __name__ == '__main__':
    unittest.main()
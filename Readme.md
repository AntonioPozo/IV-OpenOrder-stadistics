#OpenOrder
[![Build Status](https://travis-ci.org/AntonioPozo/Proyecto_IV-OpenOrder.svg?branch=master)](https://travis-ci.org/#)
[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://openorderstadistics.herokuapp.com)

###Integrantes del proyecto conjunto
- Jose Ignacio Recuerda Cambil
- **Antonio Miguel Pozo Cámara**
- Ignacio Romero Cabrerizo

##Descripción
Proyecto para la gestión de pedidos de pequeña a mediana empresa mediante una aplicación cliente-servidor. El servidor hará de intermediario entre 2 clientes (comercio y usuario) con notificaciones push. El usuario podrá realizar un pedido directamente a través de la aplicación y el comercio será notificado, agilizando el proceso de comunicación entre ambas partes. Se cuenta también con un sistema de gestión de estadísticas para informar a los locales que lo soliciten.

##Descripción del repositorio
Este repositorio alojará todo lo relativo a la parte de estadísticas de pedidos. Localización de clientes, locales y pedidos. Pevisionamiento de carga para los locales que lo soliciten. Información en tiempo real sobre los locales más demandados e información sobre tiempo de entrega de pedido. 
Se utilizará una licencia de Microsoft Azure proporcionada por el profesor de la asignatura.

##Documentación
Enlace para encontrar la descripción e información del proyecto (en construcción).

##Introducción a la aplicación
El proyecto se encuentra en un punto inicial, con forme vaya avanzando su desarrollo se dará la necesidad de utilizar distintas herramientas, las cuales se citarán **aquí**.
No obstante, ya se están utilizando las herramientas que proporciona la plataforma de informática en la nube Microsoft Azure. El servicio tendrá una base de datos interna en la que almacenar los datos obtenidos y una interfaz web a la que tendrán acceso los usuarios que lo soliciten. Para el alojamiento de la base de datos se utilizará OpenShift.

##Participación en el certamen de proyectos de libres de la UGR
Este proyecto se ha inscrito en el certamen de proyectos libres de la UGR.


##Herramienta de construcción: Makefile


```
clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;
	
install:
	sudo apt-get update 
	sudo apt-get install -y libmysqlclient-dev
	sudo apt-get install -y python-dev
	sudo apt-get install -y python-pip
	sudo apt-get install -y pymongo
	sudo pip install --upgrade pip
	sudo pip install -r requirements.txt

test: 
	python -m unittest test
	
run:
	python app.py runserver 0.0.0.0:8000
	
heroku:
	wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   # descargar herramienta heroku CLI
	heroku login
	heroku create
	git add .
	git commit -m "despliegue en heroku"
	git push heroku master
	heroku ps:scale web=1
	heroku open
```



##Sistema de pruebas

Ejecutamos los test con el comando python -m unittest test

```
import unittest
import app
from flask import Flask, render_template

def fun(x):
    return x + 1

class TestCode(unittest.TestCase):
    def test_code(self):
        # self.test_app = app.test_client()
        
        #Test demo
        self.assertEqual(fun(3), 4)

        #Test Response is 200 OK
        #response = self.test_app.get('/register', follow_redirects=True)
        #self.assertEqual(response.status, "200 OK")

        # Test logging out
        # logout = self.test_app.get('/logout', follow_redirects=True)
        #assert 'You were logged out' in logout.data







# def testSingin(nombre, passwd):
#   mongoClient = MongoClient('localhost',27017)
#   db = mongoClient.UsuariosDAI
#   collection = db.UsuariosDAI
#   user = collection.find({"nombre" : nombre, "pass": passwd})
#   # EL IF DE ABAJO COMPARA COSAS ABSURDAS, PORQUE SI LO HA ENCONTRADO ES QUE EXISTE Y POR TANTO NO TENGO QUE VOLVER A COMPARAR TODO
#   # LO QUE PASA ES QUE NO SE PUEDE HACER IF USER RETURN TRUE ELSE RETURN FALSE
#   if user[0]["nombre"]==nombre and user[0]["pass"]==passwd:
#       setSession(user[0]["nombre"], user[0]["email"], user[0]["pass"])
#       return True
#   return False


if __name__ == '__main__':
    unittest.main()

```

Ejecutamos unittest:
![ejecución de unittest](http://s2.subirimagenes.com/imagen/previo/thump_9493632unittest.png)


Herramienta para ejecutar los test de forma automática. sólo tenemos que teclear make test (en la captura del apartado Herramientas de construcción se puede observar la orden que ejecuta)


##Integración contínua
Para la integración contínua he utilizado [Travis](https://travis-ci.org). A continuación una captura del sistema de integración contínua funcionando:


![integración contínua travis](http://s2.subirimagenes.com/imagen/previo/thump_9493002traviscitestanddeoyy.png)



##Despliegue en un PaaS: Heroku

Para el despliegue de la aplicación se va a usar HEROKU como PaaS (Platform as a Service), debido a su gran integración con GitHub. Además permite el despliegue de aplicaciones de forma gratuita, a pesar de tener algunas restricciones, será suficiente para nuestro proyecto. 

Añadimos al repositorio el fichero [Procfile](https://github.com/AntonioPozo/Proyecto_IV-OpenOrder/blob/master/Procfile)

```
web: gunicorn app:app --log-file=-

```
y el fichero [requirements.txt](https://github.com/AntonioPozo/Proyecto_IV-OpenOrder/blob/master/requirements.txt)

```
Flask==0.10.1
gunicorn==19.4.1
html5lib==0.999
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
pyinotify==0.9.4
pymongo==3.1.1
pyOpenSSL==0.14
requests==2.2.1
six==1.5.2
urllib3==1.7.1
virtualenv==13.1.2
Werkzeug==0.10.4
WTForms==2.0.2
wheel==0.24.0
yolk==0.4.3

```
En el repositorio del proyecto ejecutamos las siguientes órdenes:

1.  heroku create
2.  git push heroku master
3.  heroku ps:scale web=1
4.  heroku open

Con esto la aplicación queda desplegada en [Heroku](http://openorderstadistics.herokuapp.com)

**NOTA: Estoy teniendo bastantes problemas a la hora de desplegar la base de datos tanto en Heroku como en Openshift. De ahí la simpleza de los test. Cuando consiga enlazar se cambiarán los test.**


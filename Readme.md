#OpenOrder
[![Build Status](https://travis-ci.org/AntonioPozo/Proyecto_IV-OpenOrder.svg?branch=master)](https://travis-ci.org/AntonioPozo/Proyecto_IV-OpenOrder)
[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://stadisticsopenorder.herokuapp.com)

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
No obstante, ya se están utilizando las herramientas que proporciona la plataforma de informática en la nube Microsoft Azure. El servicio tendrá una base de datos interna (MySQL) en la que almacenar los datos obtenidos y una interfaz web a la que tendrán acceso los usuarios que lo soliciten.

##Participación en el certamen de proyectos de libres de la UGR
Este proyecto se ha inscrito en el certamen de proyectos libres de la UGR.


##Herramienta de construcción: Makefile


##Sistema de pruebas

Instalamos mocha con: npm install -g mocha. Creamos un directorio en el que vamos a alojar los tests, y dentro de este, el fichero test.js que tiene el siguiente contenido:

```
var assert = require("assert");
miweb = require(__dirname+"/../app.js");

describe('Miweb', function(){
    describe('Comentar', function(){
        it('Debe cargar el programa', function(){
            assert(miweb, "Cargado");
        });
    });
});
```

Ejecutamos mocha:

![haciendo test](http://s2.subirimagenes.com/imagen/previo/thump_9485866test.png)

**Nota:** en los [ejercicios del tema 2](https://github.com/AntonioPozo/IV-2015-16/blob/master/ejercicios/AntonioPozo/Tema2.md) se detalla el proceso de instalación de nvm. 

Herramienta para ejecutar los test de forma automática. sólo tenemos que teclear make test:
![makefile](http://s2.subirimagenes.com/imagen/previo/thump_9486182makefile.png)


##Integración contínua
Para la integración contínua he utilizado las herramientas que nos ofrece Microsot Azure para ello. A continuación una captura del sistema de integración contínua funcionando:

![integración contínua azure](http://s2.subirimagenes.com/imagen/previo/thump_9485832imementacioncontinua.png)

También se está haciendo uso de Travis. A continuación una captura del funcionamiento:
![integración contínua travis](http://s2.subirimagenes.com/imagen/previo/thump_9485902travis.png)

Éste sistema informa mediante correo electrónico el resultado de los test:

![correo confirmación](http://s2.subirimagenes.com/imagen/previo/thump_9485904correo.png)



##Despliegue en un PaaS: Heroku

Para el despliegue de la aplicación se va a usar HEROKU como PaaS (Platform as a Service), debido a su gran integración con GitHub y la facilidad de uso. Además permite el despliegue de aplicaciones de forma gratuita, a pesar de tener algunas restricciones, será suficiente para nuestro proyecto.

Añadimos al repositorio el fichero [Procfile](https://github.com/AntonioPozo/Proyecto_IV-OpenOrder/blob/master/Procfile)

```
web: node.js

```
y el fichero [requirements.txt](https://github.com/AntonioPozo/Proyecto_IV-OpenOrder/blob/master/requirements.txt)

```
pip freeze > requirements.txt

```
En el repositorio del proyecto ejecutamos las siguientes órdenes:

1.  heroku create
2.  git push heroku master
3.  heroku ps:scale web=1
4.  heroku open
Con esto la aplicación queda desplegada en [Heroku](http://stadisticsopenorder.herokuapp.com)


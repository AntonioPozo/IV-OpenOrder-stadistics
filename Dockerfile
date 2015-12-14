FROM ubuntu:latest

#Autor
MAINTAINER Antonio Miguel Pozo Cámara <antoniopozo26@gmail.com> 

#Actualizar los repositorios
RUN sudo apt-get -y update

#Instalar la herramienta GIT
RUN sudo apt-get install -y git

#Descargamos el proyecto
RUN sudo git clone https://github.com/AntonioPozo/IV-OpenOrder-stadistics.git

#Instalamos python3
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y build-dep python-imaging --fix-missing
RUN sudo apt-get -y install libffi-dev
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo easy_install Pillow
RUN sudo pip install --upgrade pip
RUN sudo apt-get -y install python2.7
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

#Instalar las dependencias
RUN cd IV-OpenOrder-stadistics && pip install -r requirements.txt

FROM ubuntu:latest

#Autor
MAINTAINER Antonio Miguel Pozo Cámara <antoniopozo26@gmail.com> 

#Actualizar sistema
RUN sudo apt-get -y update

#Instalar git y herramientas necesarias
RUN sudo apt-get install -y git
RUN sudo apt-get install -y build-essential
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install libpq-dev

#Clonar repositorio
RUN sudo git clone https://github.com/AntonioPozo/IV-OpenOrder-stadistics.git

#Instalar requerimientos necesarios
RUN cd IV-OpenOrder-stadistics && git pull
RUN cd IV-OpenOrder-stadistics && make install
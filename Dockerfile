FROM ubuntu:latest

#Autor
MAINTAINER Antonio Miguel Pozo Cámara <antoniopozo26@gmail.com> 

#Actualizar sistema
RUN sudo apt-get -y update

RUN apt-get install -y git  #Primero de todo instalamos git
RUN cd /home && git clone https://github.com/AntonioPozo/IV-OpenOrder-stadistics.git

RUN sudo apt-get -y install python2.7
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install build-essential

#Instalar requerimientos necesarios
RUN cd IV-OpenOrder-stadistics && git pull
RUN cd IV-OpenOrder-stadistics && make install


CMD cd /home/ && python app.py


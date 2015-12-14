#Makefile

clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;
	
install:
	sudo apt-get update 
	sudo apt-get install -y libmysqlclient-dev
	sudo apt-get install -y python-dev
	sudo apt-get install -y python-pip
	sudo apt-get install -y pymongo
	sudo apt-get install -y python-mysqldb
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

docker:
	sudo apt-get update
    sudo apt-get install -y docker.io
    sudo docker pull apozo/iv-openorder-stadistics
    sudo docker run -t -i apozo/iv-openorder-stadistics /bin/bash

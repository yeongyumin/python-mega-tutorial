source ./bin/activate

pip3 freeze > requirements.txt

docker-compose up --build

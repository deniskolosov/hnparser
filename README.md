Run locally:
`
git clone https://github.com/deniskolosov/hnparser.git
cd hnparser
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
`
Check running app on localhost:8000

Run in Docker:
`docker-compose up`
Check running app on localhost:1337

Tests:
`docker-compose exec web python manage.py test`


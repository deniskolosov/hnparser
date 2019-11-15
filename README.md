#### Periodic parser for Hacker News frontpage
Run locally:

```
git clone https://github.com/deniskolosov/hnparser.git
cd hnparser
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
Check running app on localhost:8000

Run in Docker:
```
mv .env.docker.example .env.docker
docker-compose up -d
```
Create superuser
```
docker-compose exec web python manage.py createsuperuser
```
Go to admin `localhost:1337/admin` and create periodic task for fetching news.ycombinator.com
When task is complete, check API `localhost:1337/posts`

Check working api deployed:
http://212.71.235.219:1337/posts/


Tests:
```
docker-compose exec web python manage.py test
```


# Flask-App-with-PostgreSQL-DB

This Website is build on the Python Flask with PostgreSQL Database. Data Insertion and Fetching.

**If you are Using libraries then run the pip freeze command**

pip freeze > requirements.txt

Create runtime.txt and write your python version i.e python-3.7.10

echo web: gunicorn app:app > Procfile   #creating procfile

Create an account on heroku  and also download the heroku cli

##Write Following commands in pycharm/vscode
1. heroku login
2. heroku create "project name"
3. heroku addons:create heroku-postgresql:hobby-dev --app "project name"       
4. git init
5. git add . 
6. git commit -m "first commit"
7. heroku git:remote -a "project name"
8. git push heroku master
9. heroku run python
10. from app import db 
10. 5 db.create_all()



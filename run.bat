@echo off
title Terminal for Web RPG
cd C:\Users\Anthony\Desktop\Game Dev Projects\a game of space\Flask-App-with-PostgreSQL-DB
heroku run python
from app import db
db.create_all()
@echo on
cmd /k
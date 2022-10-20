@echo off
title Terminal for Web RPG
cd C:\Users\Anthony\Desktop\Game Dev Projects\a game of space\Flask-App-with-PostgreSQL-DB
set Flask_app=app.py
set flask_debug=0
set DATABASE_URL=postgresql-trapezoidal-88628
python app.py
@echo on
cmd /k
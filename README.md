# Welome to Our Library Repo
This repo is a basic library inventory system for cataloging a personal library of books.  
I built it to keep track of my personal library, so I could access the titles I own when I'm out acquiring more books.  

## Tech Stack
- Python
- Django
- Vanilla JS
- SQLite

Essentially, a very simple app meant to service very few people. It is designed as more of a pet project and is not very scalable. 

## Model
There is only one database table called Book. Book has:
 - title : string
 - author_first : string
 - author_last : string
 - fiction : boolean
 - condition : text choice (NEW = 'N', VERY_GOOD = 'VG', GOOD = 'G', USED = 'U', NEEDS_REPAIR = 'NR')
 - assunta_read : boolean (True if Assunta has read it)
 - lucian_read : boolean (True if Lucian has read it)

## To Build
After cloning the repo and making sure you have the right apps installed (see Tech Stack), to build this project you need only run `python manage.py runserver`

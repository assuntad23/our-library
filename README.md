# Welome to Our Library Repo
This repo is a basic library inventory system for cataloging a personal library of books.  
I built it to keep track of my personal library, so I could access the titles I own when I'm out acquiring more books.  

## Tech Stack
- Python
- Django
- Vanilla JS
- SQLite

Essentially, a very simple app meant to service very few people. It is designed as more of a pet project and is not very scalable. 

## Potential Improvements
 - Endpoint to search by author
 - Endpoint to update a book (in particular who's read it, but also account for any errors, replacement purchases)
 - Updating the Database to a production level DB
 - Using a modern JS framework (preferably Vue or React)
 - Creating a login page (beyond the built-in Django admin login)
 - Better Error Handling, especially on the frontend
 - Add a Data page with book count, unique author count, how many books each of us read, anything else interesting

## Model
There is only one database table called Book. Book has:
 - title : string
 - author_first : string
 - author_last : string
 - fiction : boolean
 - condition : text choice (NEW = 'N', VERY_GOOD = 'VG', GOOD = 'G', USED = 'U', NEEDS_REPAIR = 'NR')
 - assunta_read : boolean (True if Assunta has read it)
 - lucian_read : boolean (True if Lucian has read it)

(If you're cloning and re-creating for your own household, you'll probably want to change these names in models.py & a few other places)

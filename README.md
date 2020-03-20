# Full Stack CAPSTONE API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the project directory and running:

`
pip install -r requirements.txt
`

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


# API Reference

## Getting Started

* Base URL:
    - This app can be run localy at `http:/127.0.0.1:5000/`
    
    - This app is also hosted by heroku at `https://fsnd-capstone-project.herokuapp.com/`

## Endpoint

### GET'S

#### /actors

Can be accessed by Casting Assistant, Casting Director, and Executive Producer

* General :
    
    * Returns all actors as Actor objects, success value, and title.
    

* Sample: `curl -H "Authorization: Bearer <AccessToken>" -H "Content-Type: application/json" http://127.0.0.1:5000/actors`

###### Response :

```bash
    {
        "body": [
            {
                "name": "Mark Smith",
                "age": "26",
                "gender": "male",
                "id": 1
            },
            {
                "name": "Sarah Forbis",
                "age": "31",
                "gender": "female",
                "id": 2
            },
            {
                "name": "Jeff Johnson",
                "age", "23",
                "gender": "male",
                "id": 3
            }
        ],
        "success": true,
        "title": "Actors Page"
    }
```

#### /actors/{actor_id}

Can be accessed by Casting Assistant, Casting Director, and Executive Producer

* General :
    
    * Returns actor {actor_id} as Actor object, success value, and title.
    

* Sample: `curl -H "Authorization: Bearer <AccessToken>" -H "Content-Type: application/json" http://127.0.0.1:5000/actors/1`

###### Response :

```bash
    {
        "body": {
            "name": "Mark Smith",
            "age": "26",
            "gender": "male",
            "id": 1
        },
        "success": true,
        "title": "Actor Mark Smith's Page"
    }
```

#### /movies

Can be accessed by Casting Assistant, Casting Director, and Executive Producer

* General :
    
    * Returns all movies as Movie objects, success value, and title.
    

* Sample: `curl -H "Authorization: Bearer <AccessToken>" -H "Content-Type: application/json" http://127.0.0.1:5000/movies`

###### Response : 

```bash
    {
        "body": [
            {
                "title": "Udacity",
                "release_date": "Wed, 21 Oct 2020 18:30:00 GMT",
                "id": 1
            },
            {
                "title": "CAPSTONE",
                "release_date": "Mon, 21 Dec 2020 20:00:00 GMT",
                "id": 2
            }
        ],
        "success": true,
        "title": "Movies Page"
    }
```

#### /movies/{movie_id}

Can be accessed by Casting Assistant, Casting Director, and Executive Producer

* General :
    
    * Returns movie {movie_id} as Movie objects, success value, and title.
    

* Sample: `curl -H "Authorization: Bearer <AccessToken>" -H "Content-Type: application/json" http://127.0.0.1:5000/movies/1`

###### Response : 

```bash
    {
        "body": {
            "title": "Udacity",
            "release_date": "Wed, 21 Oct 2020 18:30:00 GMT",
            "id": 1
        },
        "success": true,
        "title": "Movie Udacity's Page"
    }
```

### POST's

#### /actors

Can be accessed by Casting Director, and Executive Producer

* General :
    
    * Creates a new Actor using the submitted name, age, and gender
    * Returns Actors as Actor objects, success value, and title
    

* Sample: `curl -X POST -H "Authorization: Bearer <AccessToken>" -H "Content-Type: application/json" http://127.0.0.1:5000/actors -d '{"name":"Jasmine Caylor", "age": "22", "gender": "female"}'`

###### Response :

```bash
    {
        "body": [
            {
                "name": "Mark Smith",
                "age": "26",
                "gender": "male",
                "id": 1
            },
            {
                "name": "Sarah Forbis",
                "age": "31",
                "gender": "female",
                "id": 2
            },
            {
                "name": "Jeff Johnson",
                "age", "23",
                "gender": "male",
                "id": 3
            },
            {
                "name": "Jeasmine Caylor",
                "age", "22",
                "gender": "female",
                "id": 4
            }
        ],
        "success": true,
        "title": "Actors Page"
    }
```

#### /movies

Can be accessed by Executive Producer

* General :
    
    * Creates a new Movie using the submitted title, and release date (YYYY-MM-DD HH:MM)
    * Returns Movies as Movie objects, success value, and title
    

* Sample: `curl -X POST -H "Authorization: Bearer <AccessToken>" -H "Content-Type: application/json" http://127.0.0.1:5000/movies -d '{"title":"FSND", "release_date": "2020-05-12 19:00"}'`

###### Response : 

```bash
    {
        "body": [
            {
                "title": "Udacity",
                "release_date": "Wed, 21 Oct 2020 18:30:00 GMT",
                "id": 1
            },
            {
                "title": "CAPSTONE",
                "release_date": "Mon, 21 Dec 2020 20:00:00 GMT",
                "id": 2
            },
            {
                "title": "FSND",
                "release_date": "Tue, 12 May 2020 19:00:00 GMT",
                "id": 3
            }
        ],
        "success": true,
        "title": "Movies Page"
    }
```

### DELETE'S

#### /actors/{actor_id}

Can be accessed by Casting Director, and Executive Producer

* General :
    
    * Delete an actor based on given id
    * Returns actor's id, and success value
    

* Sample: `curl -X DELETE -H "Authorization: Bearer <AccessToken>" -H "Content-Type: application/json" http://127.0.0.1:5000/actors/3`

###### Response : 

```bash
    {
        "Deleted Actor": 3,
        "success": true,
        "title": "Actors Page"
    }
```

#### /movies/{movie_id}

Can be accessed by Executive Producer

* General :
    
    * Delete a movie based on given id
    * Returns movie's id, and success value
    

* Sample: `curl -X DELETE -H "Authorization: Bearer <AccessToken>" -H "Content-Type: application/json" http://127.0.0.1:5000/movies/1`

###### Response : 

```bash
    {
        "Deleted Movie": 1,
        "success": true,
        "title": "Movies Page"
    }
```

### PATCH'S

#### /actors/{actor_id}

Can be accessed by Casting Director, and Executive Producer

* General :
    
    * Update an actor using the submitted name, age, or gender
    * Returns actors as Actor objects, success value, and title
    

* Sample: `curl -X PATCH -H "Authorization: Bearer <AccessToken>" -H "Content-Type: application/json" http://127.0.0.1:5000/actors/2 -d '{"age": "32"}'`

###### Response :

```bash
    {
        "body": [
            {
                "name": "Mark Smith",
                "age": "26",
                "gender": "male",
                "id": 1
            },
            {
                "name": "Sarah Forbis",
                "age": "32",
                "gender": "female",
                "id": 2
            },
            {
                "name": "Jeff Johnson",
                "age", "23",
                "gender": "male",
                "id": 3
            },
            {
                "name": "Jeasmine Caylor",
                "age", "22",
                "gender": "female",
                "id": 4
            }
        ],
        "success": true,
        "title": "Actors Page"
    }
```

#### /movies/{movie_id}

Can be accessed by Casting Director, and Executive Producer

* General :
    
    * Update a movie using the submitted title, or release date (YYYY-MM-DD HH:MM)
    * Returns movies as Movie objects, success value, and title
    

* Sample: `curl -X PATCH -H "Authorization: Bearer <AccessToken>" -H "Content-Type: application/json" http://127.0.0.1:5000/movies/2 -d '{"release_date": "2021-01-13 19:30"}'`

###### Response : 

```bash
    {
        "body": [
            {
                "title": "Udacity",
                "release_date": "Wed, 21 Oct 2020 18:30:00 GMT",
                "id": 1
            },
            {
                "title": "CAPSTONE",
                "release_date": "Wed, 13 Jan 2021 19:30:00 GMT",
                "id": 2
            },
            {
                "title": "FSND",
                "release_date": "Tue, 12 May 2020 19:00:00 GMT",
                "id": 3
            }
        ],
        "success": true,
        "title": "Movies Page"
    }
```

## Authentication

##### Use the following Access Tokens for testing purposes via curl or postman

###  Casting Assistant :

   * Permissions :
    
     - get:actors
     - get:movies



* Access Token (JWT) : 
```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6aEJNRE0yUVVaRk1UZEdOakF5UWpBd09VWkZPRU0yUkVReU5qSXpSa0pDTURZeE1ETkRSUSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2Fwc3RvbmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNzEwNmU5MTYzMjczMGQxZGJiZTRkNCIsImF1ZCI6WyJjYXBzdG9uZSIsImh0dHBzOi8vZnNuZC1jYXBzdG9uZS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTg0NzA0NzMzLCJleHAiOjE1ODUzMDk1MzMsImF6cCI6ImMwWEFKemY5QTlNNnJNNWpCMDJWN1NHR2JjMlBMa25mIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.ZiaD_s6mLfgnQpXHj8ugObfekFpafFI51objF0ZbH9xcFcXKB9W2LrxwqqkJcZM363hiCJ7mYk4u3y7EgZsD8iNyQONJZme5PWZmr_u5aKvD_lgI7OueV65d05lgYiNTWWNKfUw4wMA3XUu_RzVQeEcG-aScpoR2Wcur8hXt-J2ka6jM4ymL3H5WHW_vQwHoVAP2NZOYeoObWryvHZfUcRw2IOuG50Sh2J2ZFBJMXwaJSORKI4HwzT216J6ARDlkKDl2CoRc2s5F4SV6WkixG9wz-qzV3kC7DNQ_JTuEzhofljSl3vkASntty77mKva1os_YEQuV8RZJNGhn_X4GEQ
```


###  Casting Director :

   * Permissions :
        
     - get:actors
     - get:movies
     - patch:actors
     - patch:movies
     - post:actors
     - delete:actors



* Access Token (JWT) : 
```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6aEJNRE0yUVVaRk1UZEdOakF5UWpBd09VWkZPRU0yUkVReU5qSXpSa0pDTURZeE1ETkRSUSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2Fwc3RvbmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNmY2YWE4MTA4ODViMGNhNmFjZDQ3MiIsImF1ZCI6WyJjYXBzdG9uZSIsImh0dHBzOi8vZnNuZC1jYXBzdG9uZS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTg0NzA0NzgzLCJleHAiOjE1ODUzMDk1ODMsImF6cCI6ImMwWEFKemY5QTlNNnJNNWpCMDJWN1NHR2JjMlBMa25mIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.GVlqjGWgNVjCWfKnZaNt_4HXU74cjjsnSzCx6ZohHZDclDbSTQ2RsVIphGIg3rLv20mWAfSc2ltRcXXPq0T1Q0xClREigAWqieIMmXvkvc8mZAQ4e0zGz4mHgSmOeh7QGSKhqyLAK2-j83vJ2n2pYxx2tNxCyGN_KwJ1Sz_f6pqrcWI7A0cilAVB_-VpleI_Jgtj7fxbu8MG2GyPDP8Q8uXOfMcCNsfmwSufrbu-4FOOhKE6iWJDpCV0nK7OybxHjJW2LJOSkGWMHC7ic5t9TBnV3-_NRfxbSeyjYgi_1jB7POulEeCdR385hvF4-xQEtbR5qRTqOQaVhumt2U8G4Q
```


###  Executive Producer :

   * Permissions :
        
     - get:actors
     - get:movies
     - patch:actors
     - patch:movies
     - post:actors
     - post:movies
     - delete:actors
     - delete:movies



* Access Token (JWT) : 
```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6aEJNRE0yUVVaRk1UZEdOakF5UWpBd09VWkZPRU0yUkVReU5qSXpSa0pDTURZeE1ETkRSUSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2Fwc3RvbmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNzI0MzhiMTkwNGM0MGNmNWNhMzUzOSIsImF1ZCI6WyJjYXBzdG9uZSIsImh0dHBzOi8vZnNuZC1jYXBzdG9uZS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTg0NzA0ODE5LCJleHAiOjE1ODUzMDk2MTksImF6cCI6ImMwWEFKemY5QTlNNnJNNWpCMDJWN1NHR2JjMlBMa25mIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.p77YJqQdBDAhl5zF3kBFUvfmIIQgEsmN9JlvheEq8c0w1tL7PmJEE-z8TGXxjrKeRgb3EPmA0KI7fzjUHsq-1L21izDlDq4dxmfIAQ0pLm777oXWt4QOoSSoOt7DUt1yvexhHbdOPaxunHMoJpRHpoOtuoigQfVJX81OuoAQi0ntwEr5EV6TRMTjldycAukWYacP7yAyxIqzSfQ8-UYti4zT6qF6UvKjDEZanRjp4jPFxeKChG4CYdURTtSvtQtDJR5-oQxsVA0wirmgC6lqqZFj6mu9zrC5InAaClPK0qtZObijFD-Ul7MHZ8-yCuLu-3ZdFDoMfs8uszwglqLkig
```

## Error Handling

The API will return five error tyoes when requests fail:


   * 400 (Bad Request)
    
   * 404 (Page Not Found)
    
   * 405 (Method Not Allowed)
    
   * 422 (Unprocessable)
   
   
    
   * Authentication Error :
       - 400 (Invalid Claims)
       - 401 (Unauthorized)
       - 403 (Forbidden)

### Errors :


#### 400 (Bad Request) :

```bash
    {
        "error": 400,
        "message": "Bad Request",
        "success": False
    }
```

#### 404 (Page Not Found) :

```bash
    {
        "error": 404,
        "message": "Not Found",
        "success": False
    }
```

#### 405 (Method Not Allowed) :

```bash
    {
        "error": 405,
        "message": "Method Not Allowed",
        "success": False
    }
```

#### 422 (Unprocessable) :

```bash
    {
        "error": 422,
        "message": "Unprocessable",
        "success": False
    }
```

### Authentication Errors : 


#### 400 (Invalid Claims) :

```bash
    {
        "error": 400,
        "message": "Invalid Claims ...",
        "saccess": False
    }
```

#### 401 (Unauthorized) :

```bash
    {
        "error": 401,
        "message": "Invalid Header ...",
        "saccess": False
    }
```

#### 403 (Forbidden) :

```bash
    {
        "error": 403,
        "message": "Unauthorized ...",
        "saccess": False
    }
```

* Messages in Authentication Errors could vary.

## Deployment

#### This Application is hosted by Heroku at : `https://fsnd-capstone-project.herokuapp.com/`

## Authors

#### Ibrahim AlBlooshi, A Udacity FSND Student

## Acknowledgements

#### 1) Deploy a Flask App to Heroku : https://www.youtube.com/watch?v=FKy21FnjKS0

#### 2) Flask in general : https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g

#### 3) Handling Auth0 with Python : https://github.com/auth0/auth0-python

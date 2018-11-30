# A simple url shortener in flask

## Usage

    FLASK_APP=app.py flask run

## Settings

Edit config.py

Default database is SQLite and saved as `url_shortener.db`

To change the database backend edit config.py and change the `SQLALCHEMY_DATABASE_URI` variable. 
Alternatively add a `DATABASE_URL` environment variable containing the `DATABASE URI`

## API

To shorten a URL:

 Request:
    
        POST www.your_service.com/shorten_url
            body:
            {
                "url": "www.helloworld.com"
            }
 
 Response:
    
        Status code: 201
        response_body:
        {
            "shortened_url": 'http://www.your_service.com/ouoYFY48'
        }

To list all URLs (debug):
    
    GET www.your_service.com/list

# Build a url shortener
Your primary task is to build a URL shortener web service using Java, Scala or Python.

## Requirements

● Your web service should have a `POST /shorten_url` endpoint that receives a `JSON` body with the
`URL` to shorten. A successful request will return a `JSON` body with the shortened url. If a `GET`
request is made to the shortened `URL` then the user should be redirected to the the original `URL`,
or returned the contents of the original `URL`.

● It should perform appropriate validation on the `URL` to be shortened, and return appropriate error
responses if the URL is not valid.

● It should contain a `README.md`    file with instructions on how to run your service.

## Note:
This task is simple and straightforward, so we will be assessing you on your implementation of web
services, use of the language and solid engineering practices. Use this as an opportunity to
demonstrate how you write code and solve problems. You should also build your web service so it
can scale to a thousands of requests per second. Please explain in your `README.md` file how does
your solution allow for it and how would you scale it.

## Example usage:
1) `GET www.helloworld.com` -> hello world

2)

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

3) `GET http://www.your_service.com/ouoYFY48` -> hello world
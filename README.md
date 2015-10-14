# token-auth-flask-security
Learning how to build a full backend API solution including token-based authentication with Flask-Security.  The project may include a simple front end to show it working, but the main goal is to build the API to refer to in the future.

I will be following this link best I can:

* [Token Based Authentication with Flask-Security](https://mandarvaze.github.io/2015/01/token-auth-with-flask-security.html)

Any others I come across will be added here as well.

get a token like this:

POST testflask.local:5000/login with {"email":"email here", "password":"password here"}

then use the token to authenticate to /dummy-api/ with Authentication-Token:"token here"

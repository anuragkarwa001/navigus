# presence service
This is a small web application made on Django framework that gives access to the registered users for accesing a particular content
Also it blocks the user from directly accessing the protected web page and if unauthenticated user tries to access the page then it 
redirects to the login page automaticially but if the user is logged in it views the document 
It has dynamic login and logout button which were made by using jinja
For showing the name of user logged in we need to refresh the page for any update (as of now hot refreshing is not supported)
installation guide
1. clone the repository
2. install python version >=3.0 and django version >=3.0 (pip install django)
3. install postgresql and run the instance 
4. edit /backend/settings.py and in the database section add name of data base , username and password created in step 3
5. now in the root directory open cmd and type python manage.py migrate(it should aplly migration of models into your database sucessfully)
6. now in cmd type  python manage.py runserver  (for running the server on your localhost)
7. now you can hit the APIs mentioned using a web browser 
   1. http://127.0.0.1:8000/authentication/home   -- for accessing the home page 
   1. http://127.0.0.1:8000/authentication/login_page/   -- for login form(get method)
   1. http://127.0.0.1:8000/authentication/signup_page/    --for signup form (get method)
   1. http://127.0.0.1:8000/authentication/login_page/login   --for submitting login data(POST method) do not open it in browser as it 
      will through error as it is excepting data in post form 
   1. http://127.0.0.1:8000/authentication/signup_page/signup   --for submitting signup data(POST method) do not open it in browser as it 
      will through error as it is excepting data in post form 
   1. http://127.0.0.1:8000/authentication/logout  --for deauthenticating the user 
   1. http://127.0.0.1:8000/authentication/login_page/view_page   --for viewing the protected documnet if logged otherwise show error
  
Features Guide:-
1.Checks if the username already exists
2.Checks if the login id and password does not match 
3.from signup page redirect to home page welcoming the user and asking for login 
4.After login the page will be viewed along with the online users
5.If user tries to access that page directly using link it will redirect the user to login page


images(screenshots):
gdrive link 
https://drive.google.com/drive/folders/1sWjYYHBNSv6ev-VCgrUDnuDE1WKnc73q?usp=sharing

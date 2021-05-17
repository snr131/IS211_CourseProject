# IS211_CourseProject
 
For this project, I selected option 1, the book catalog. I will describe my solution to each of the project requirements. 

I used the flask_login library to support multiple users, which seems to work well for this type of project. With flask_login, I can manage user authentication and access information specific to each user (i.e., user_id) to customize the user's dashboard. I organized routes specific to logging in in the auth.py file. To collect user credentials at signup, I used a form that fed information stored in the User table of my SQLite database. Those user-defined credentials can be used on the login page to authenticate.

In addition to the forms used to collect signup and login input, I created forms to add and delete books from the user's catalog. These forms are in the forms.py file. The models.py file shows how I used the ORM sqlalchemy to take information input by users into the forms and feed that into the SQLite database. The models.py file also shows attributes not entered by the user, like the book title, author, image_url, etc. The routes.py file shows how those attributes are collected. 

When the user enters an ISBN, the /add route sends a request to the Google API, the response is stored as a json object, and information within is accessed as a dictionary. The data of interest is saved in appropriate variables. The dashboard.html file then displays this information using a for loop to access the appropriate user's book catalog, including an image of the bookcover. If the user is logged in, the /dashboard route shows how the user's catalog is accessed using the flask_login.current_user method.

To delete a book from a catalog, the .get() method can search for a book by it's id, then delete it from the SQLite database. 

To run this app, use the bookcatalog.py file. This is where the app objects are instantiated. 
# Library_Management

## How to Run the project locally
Currently I have not been able to host this project on Heroku due to issues of Heroku CLI with Windows OS. But this project can be run locally by cloning this repo
### Requirements
Python and Django should be installed locally.<br>
To install django open terminal and write 
```bash
pip install django
```
After this open the project and move to the directory where manage.py is located and type in the command
```bash
python manage.py runserver
```
## Dummy Users
|Username|Password|Role  |
|--------|--------|------|
|admin|admin|ADMIN|
|staff|staff|STAFF|
|user1|pass1|USER|
|user2|pass2|USER|
|user3|pass3|USER|
|user4|pass4|USER|
|user5|pass5|USER|
<br>

## Registration and Login System
<br>
We can create accounts by clicking the signUp link and we can login using login. Staff members can login into Django Admin as well as in users section.<br>

### Setting staff status for librarians
This project uses default django user model in which admin can assign staff roles to various users by checking the staff checkbox in django admin panel. Also he can set permissions
for the staff members limiting their powers on the admin portal.<br><br>

## Django Admin
<br>
In this portal staff memebers can edit data of various models that our project uses. They can edit, delete, add Books, Reviews, Users, IssueRequests.<br>
Most of the functions that can be performed with the django admin interface can be performed by loging in to our site as well. Altough the implementation of django admin remains far better.<br>

## Home Pages
Home Page shows various options available to users through which they can interact with our website. They can view and search books, see their profile pages and logout from the website<br>
Staff members see extra options in this page. They can Add a new Book, see pending requests, etc.<br>

## View Books
We can view books by clicking on the view all books link.<br>
### Search Boks
After this we can search for some book by typing its name in the search bar. We can open the page of our required book. 
### Dynamic Webpage For every Book
In the webpage of every book we have its info , we can add reviews, see aother reviews and put an issue request for the book it is available in the library.<br>
Staff people have more power and control in this page as well. They can update the book info, delete that particular book, delete offensive reviews apart from the things that a normal user can do.<br>

## Rating System
For making the rating system we have made a Review model and placed a form on the webpage of the book so that the users can rate their favourite books. Admins can delete offensive reviews by simply clicking on the delete review button that is right next to the review on the book's own webpage. Average Rating is also displayed in the book info section.<br>
## Updating/Delete Books

Only admins are allowed to update any books. To update any book they can simply visit that book's page and fill in the necessary updates there and submit the form by clicking on Update button. Then our webapp returns an HttpResponse saying book update successful on success of the task. We canreload the page to see the updates in effect. <br>
## Adding Books
Librarians can add new books to the database by clicking on the add book link on the top of the page. Librarians have to fill a small form giving the book info and then submit that form in order to create a new book.
This new book that is added is now visible under the all books section.<br>
Books can be deleted by admins by clicking on delete button on the books webpage.<br>

## Issuing a Book
Allowed issue requests per book per user is one only. However they are free to make requests for other books. Users can make issue requests only for books are available in the library.<br>
We make our issue requests by introducing an IssueRequest model in django framework. Under our mechanism issue requests are made by the users by visiting the book webpage. After making the request the users are redirected to teir profile page where they can see their issue requests. Now all the issue requests are visible to the librarian in the view pending requests section. He can choose to accept or decline them. To accept Simply click Issue book by logging in as a staff member. To decline simply decline the request.
After an action is taken the user can see the status of his issue request on his own profile pag. It shows pending/approved/declined for every reuest put in by user. If the request is accepted then the user also sees the deadline for return own his own profile page. 




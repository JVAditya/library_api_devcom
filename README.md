# library_api_devcom

The api can be found at http://localhost:<port>/ after running the command 'python maanage.py runserver'   - port is 8000 by default, though you could specify a custom value of the port too
In order to host the api, django and djangorestframework have to be installed using pip install django and pip install djangorestframework 
  
Endpoints:
  
  students/:  It shows a list view of the data of students. POST and GET requests can be made on this endpoint.
  students/<roll-no>/ : shows the info of a student with roll no = roll_no. GET and DELETE requests can be made at this endpoint.
  
  books/ : It shows the list of books available, new books can be added using POST request. If a book with the same name is already present in the database,
           , then the new book can only be created if the other parameters(author, subject, pages) exactly match with the pre-existing entry. 
  books/<book_id>/ : It shows the info about a particular book with id = book_id. A PUT request can be made at this endpoint to issue this book to 
                     a student or retrieve the book from a student. A DELETE request can also be made which deletes the book only if it is not issued to 
                     any student at the time of deletion.
  
  register/ : It is a list of the log of book issues and returns. Only a GET request can be made at this endpoint and the data shown at this endpoint can't
              be manually changed.
  
 Models:
   
  Student: has two fields - name and roll_no of which roll_no is set as the primary key of this model.
  Book: has a name, the date of acquiring(can be set only once when the objet is created in the database), the time of last issue and the time of last return.
        It also has fields for storing the name of the author, number of pages and subject. Subject can only be chosen from a list of available subjects.
        If a book of a differnt subject has to be created, the list of SUBJECTS can be changed in the models.py file of book app. And finally, it has a foreign
        key field which stores the roll no of the student who currently has that book. If no student is using it currently, then that field is set to null.
  Register: has fields for storing the roll_no of the student and name and id of the book. It also has a status field which tells us if the book was returned
            or issued. Then it has the action_time field which stores the time of issue/return. None of these fields can be set manually.
  
  
  

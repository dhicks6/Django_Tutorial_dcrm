from django.db import models

# This record class creates the database model in django. You don't have to write it in the language
#   that the database uses django does all of that for you.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address =  models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    zipcode =  models.CharField(max_length=20)

    def __str__(self):
        # Here we are returning what we want to show on the screen if we access one of these
        #       records using an f string.
        return(f"{self.first_name} {self.last_name}")
from django.db import models
from django.forms import ModelForm


class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10,default=1234567890)

    def __str__(self):
        return self.first_name

class CustomerForm(ModelForm):

    class Meta:
        model=Customers
        fields={'first_name',
            'last_name',
            'course'}
        #fields= "__all__"



from django.db import models
from Account.models import *

# Create your models here.

Methods=(
    ('GET', 'GET'),
    ('PUT', 'PUT'),
    ('POST', 'POST')

)

class Dstinations(models.Model):
    Account_name = models.ForeignKey(Account,on_delete=models.CASCADE)
    Destination_Url = models.URLField(max_length=200)
    Http_method = models.CharField(max_length=50,choices = Methods,default = '1')
    Header = models.JSONField()

from django.db import models
import uuid
# Create your models here.

class Account(models.Model):
    Account_id = models.CharField(max_length= 50,unique=True)
    Email_id = models.EmailField(max_length=100,unique=True)
    Account_Name = models.CharField(max_length= 100)
    Secret_token = models.UUIDField(default=uuid.uuid4,unique=True, editable=False)
     

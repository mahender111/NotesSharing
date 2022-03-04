from django.contrib.auth.models import User
from django.db import models



# Create your models here.


class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    contact = models.CharField(max_length=13,null=True)
    branch= models.CharField(max_length=30,default="")
    role= models.CharField(max_length=30,default="")

    def __str__(self):
        return self.user.username


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    uploadingdate = models.CharField(max_length=30,default="", null=True)
    branch = models.CharField(max_length=30,default="")
    subject = models.CharField(max_length=30,default="")
    notesfile = models.FileField(null=True)
    filetype = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=2000, null=True)
    status= models.CharField(max_length=10,default="")

    def __str__(self):
        return self.user.username+" "+self.status
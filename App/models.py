from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class userProfile(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='profile_pic',default='sherlock.jpg')
    is_farmer = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username + " profile"


class crop(models.Model):

    crop = models.CharField(default="none",max_length=500)
    description = models.CharField(default="none",max_length=50000)
    
    # image = models.ImageField(upload_to='profile_pic',default='sherlock.jpg')
    
    def __str__(self):
        return self.crop

class blog(models.Model):

    title = models.CharField(default="none",max_length=500)
    description = models.CharField(default="none",max_length=50000)
    
    image = models.ImageField(upload_to='blog',default = "default.jpg")
    
    date = models.DateTimeField(default=datetime.datetime.now())
    username = models.CharField(default = "none",max_length=1000)
    def __str__(self):
        return self.title

class chat(models.Model):

    from_u = models.ForeignKey(
        User, related_name='from_u', on_delete=models.CASCADE)

    to_u = models.ForeignKey(
        User, related_name='to_u', on_delete=models.CASCADE)

    sent_by = models.ForeignKey(
        User, related_name='sent_by', on_delete=models.CASCADE)
        
    message = models.CharField(default="none",max_length=10000000)
    chat_between = models.CharField(default="none",max_length=10000000)
    # is_bullying = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return self.to_u.username + "'s request."


class comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(default="none",max_length=5000)
    
    post = models.ForeignKey(blog,on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.user.username + " comment"


class product(models.Model):

    name = models.CharField(default="none",max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products',default = "default.jpg")
    price = models.ImageField(upload_to='products',default = "default.jpg")
    contact = models.CharField(default="none",max_length=500)
    date = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.name


class Advertisement(models.Model):

    name = models.CharField(default="none",max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads',default = "default.jpg")
    
    contact = models.CharField(default="none",max_length=500)
    date = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.name



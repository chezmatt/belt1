from django.db import models
from django.core.exceptions import ValidationError





class User(models.Model):
    def validateUsername(self, postdata):
        username = postdata['username'].lower()
        if self.objects.filter(username=username).exists():
            return (False, "Sorry that username is taken.")
        else:
            return (True, username)
    
    first_name = models.CharField(max_length=75, blank=True, null=True)
    last_name = models.CharField(max_length=75, blank=True, null=True)
    username = models.CharField(max_length=75, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    dob_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    # description = models.TextField(max_length=1000, blank=True, null=True)
    user_level = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.username

class Post(models.Model):
    post = models.TextField()
    user = models.ForeignKey(User, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    description = models.TextField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
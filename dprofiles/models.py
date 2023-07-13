from django.db import models
# Create your models here.
class userPosts(models.Model):
    postID = models.IntegerField(primary_key=True)
    username = models.ForeignKey('users.customUser', on_delete=models.CASCADE)
    postDate = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
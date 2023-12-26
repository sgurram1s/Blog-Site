from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now

from django.urls import reverse

class PostData(models.Model):
    CATEGORY_CHOICES = (
    ('Technology', 'Technology'),
    ('Entertainment', 'Entertainment'),
    ('Politics', 'Politics'),
    ('Food', 'Food'))
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    content_body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    content_type = models.CharField(max_length=100, null = True, choices=CATEGORY_CHOICES)
    

    def __str__(self):
        return self.title
    
    def body_snippet(self):
        return self.content_body[:150] + '.........'
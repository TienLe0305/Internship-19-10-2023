from django.db import models

from datetime import datetime

class Comment:
    def __init__(self, email, content, created = None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
        
comment = Comment(email='lvt030501@gmail.com', content='foo bar')

class Account(models.Model):
     account_name = models.CharField(max_length=100)
     users = models.ManyToManyField('auth.User')
     created = models.DateTimeField(auto_now_add=True)
     
     def __str__(self) -> str:
         return self.account_name

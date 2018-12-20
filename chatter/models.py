from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    content = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    @classmethod
    def create_message(cls, content, user):
        message = cls(content=content, user=user)
        return message
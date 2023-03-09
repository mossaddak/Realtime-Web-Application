from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="MessageSenderRelatedName", null=True)
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="MessageReciverRelatedName", null=True)
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_seen = models.BooleanField(default=False,null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.pk}.{self.sender}"
    
    def formatted_date(self):
        return self.date.strftime("%Y-%m-%d")

from django.db import models

# Create your models here.

class Conversation(models.Model):
    user1 = models.CharField(max_length=100)
    user2 = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('updated',)

    def create(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
        self.name = user1 + " " + user2
        self.save()

    def __str__(self):
        return self.name


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
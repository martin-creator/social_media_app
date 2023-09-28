from time import time
import uuid
from django.db import models
from account.models import User
from django.utils.timesince import timesince

# Create your models here.

class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_attachments')


class Post (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True) # null=True is used to specify that the body field can be null in the database.

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='posts')

    attachments = models.ManyToManyField(PostAttachment,blank=True)

    #likes
    #likes_count

    class Meta:
        ordering = ('-created_at',)

    def created_at_formatted(self):
        return timesince(self.created_at)
    
    

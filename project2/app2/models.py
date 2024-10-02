from django.db import models

# Create your models here.
class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
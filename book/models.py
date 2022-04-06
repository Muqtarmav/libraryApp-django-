from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    description = models.TextField(null=False)
    pageCount = models.IntegerField()



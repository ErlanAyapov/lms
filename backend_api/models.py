from django.db import models 
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=250)
	body  = models.TextField()


class Instruction(models.Model):
	title = models.CharField(max_length=500)
	body  = RichTextField(null=True)


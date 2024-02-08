from django.db import models

# Create your models here.
#here the return statement is used to show the actual name of the entry in the admin panel
#self.name=name shows the name of the post in the admin panel
#self.id shows the id of the post in the admin panel

#also to show the table field in the admin panel register the post model in the admin.py file 


class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=17)
    content=models.TextField()
    def __str__(self):
        return self.name
    
class Post(models.Model):
    categories=(
        ('Teacher','Teacher'),
        ('Student','Student')
    )
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    email=models.EmailField()
    salery=models.IntegerField()
    details=models.TextField()
    available=models.BooleanField()
    category=models.CharField(max_length=100,choices=categories)
    #show=id.concat(title)
    def __str__(self):
        return self.title



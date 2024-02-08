from django.db import models

# Create your models here.
#here the return statement is used to show the actual name of the entry in the admin panel
#self.name=name shows the name of the post in the admin panel
#self.id shows the id of the post in the admin panel

#here a new model named Post is created with its coresponding fields
#also to show the table field in the admin panel register the post model in the admin.py file 

#part 15----------------------------
#adding an image field. First in settings.py create MEIDA_ROOT and MEDIA_URL
#then in the selected model(POST) add imagefield() as param default has been used. 
#to use Default image we have to define where the uploaded image will be saved. Use upload_to param
#Dont forget to makemigrations and migrate
#then to show the uploaded picture go to main urls.py file for more documentation

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
    #2nd 
    salery=models.IntegerField() 
    details=models.TextField()
    available=models.BooleanField()
    category=models.CharField(max_length=100,choices=categories)
    image=models.ImageField(default='default.jpg',upload_to='tuition/images')
    #show=id.concat(title)
    def __str__(self):
        return self.title



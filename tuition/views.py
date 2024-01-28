from django.shortcuts import render
from .models import Contact
from .forms import contactForm
# Create your views here.
#----------------part 11--------------------
#here we have copied the views
#and for else block if the url is hit from get method 
#import he contactfrom class too and the models and i
#now just remove all the content from the html page of contact.html and replace with {{form}}
#need to change the url, new file under tuition app urls.py and import the views of tuition app
#then in the main project urls.py file add include with 'tuition' urls so that
#we can hit 'tuition/contact' url and the contact url is located inside the tuition app urls.py file

#then
def contact(request):
    if request.method=='POST':
        #here if we remove the precedding coma after name=request.POST['name'] then we can create a perfect type of values
        if form.is_valid():
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            content=form.cleaned_data['content']
            print(name)

            print(phone)
            print(content)
            print(type(name))
            obj=Contact(name=name,phone=phone,content=content)
            obj.save()
    else:
        form=contactForm()


        
    return render(request,'contact.html',{'form':form})

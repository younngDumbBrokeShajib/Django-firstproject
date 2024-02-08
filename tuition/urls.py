from django.urls import path
from .views import contact,postViews
urlpatterns = [
    path('contact/',contact,name="contact"),
    path('views/',postViews,name="postviews")
]
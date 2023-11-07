from django.urls import path
from . import views
app_name = 'tweetapp'

urlpatterns = [
    path('',views.listtweet, name='listtweet'), #127.0.0.1:8000/tweetapp/
    path('addtweet/', views.addtweet, name='addtweet'), #127.0.0.1:8000/tweetapp/addtweet   
    path('addtweetbyform', views.addtweetbyform, name="addtweetbyform"), #127.0.0.1:8000/tweetapp/addtweetbyform  
    path('addtweetbymodelform', views.addtweetbymodelform, name='addtweetbymodelform'),
    path('signup/',views.SignUpView.as_view(), name="signup"),
    path('deletetweet/<int:id>', views.deletetweet, name="deletetweet")
]
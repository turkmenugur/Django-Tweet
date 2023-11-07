from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweetapp.forms import AddTweetForm, AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# Create your views here.

#reverse_lazy -> sadece buraya ulaşıldığında hesaplanır
#reverse ise o fonksiyon ya da sınıf için programda sürekli hesaplanır ve sistem kaynaklarını tüketir. Örneğin, bu kodda signupview sınıfını kullanıcı bir defa kullansa da sürekli bu reverse çalıştırılır ve "login" görünümü olup olmadığı hesaplanır. ->     success_url = reverse("login")


def listtweet(request):
    all_tweets = models.Tweet.objects.all() #bütün tweetleri alma
    tweet_dict = {"tweets":all_tweets} #context olarak diğer tarafa yollama
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

@login_required(login_url="/login")
def addtweet(request):
    #form aracılığıyla bilgiyi alma
    if request.POST: 
        message = request.POST["message"]
        models.Tweet.objects.create(username=request.user, message=message)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, 'tweetapp/addtweet.html')
    
def addtweetbyform(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("Error in form!")
            return render(request,'tweetapp/addtweetbyform.html', context={"form":form})
    else:
        form = AddTweetForm()
        return render(request,'tweetapp/addtweetbyform.html', context={"form":form})
    
def addtweetbymodelform(request):
    if request.method == "POST":
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("Error in form!")
            return render(request,'tweetapp/addtweetbymodelform.html', context={"form":form})
    else:
        form = AddTweetModelForm()
        return render(request,'tweetapp/addtweetbymodelform.html', context={"form":form})
    
@login_required
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete() 
        #tweet.delete() de aynı işi yapar
        return redirect('tweetapp:listtweet')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


from django.contrib import admin
from tweetapp.models import Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        #field'ların gruplandırılmış hali
        ('Message Group',{"fields":["message"]}),
        ('Nickname Group',{"fields":["nickname"]})
    ]
    #fields = ['nickname', 'message']

admin.site.register(Tweet, TweetAdmin)

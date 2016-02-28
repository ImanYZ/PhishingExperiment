from django.contrib import admin

from .models import User
from .models import HoltLaury
from .models import Gamble
from .models import Investment
from .models import Pretest
from .models import Thankyou

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'totalearning', 'experimentearning',
        'firstgame', 'secondgame', 'thirdgame', 'startedstudy',
        'finishedstudy', 'created', 'updated']

    search_fields = ['username']

admin.site.register(User, UserAdmin)

class HoltLauryAdmin(admin.ModelAdmin):
    list_display = ['user', 'decision', 'option1', 'option2',
        'option3', 'option4', 'option5', 'option6', 'option7',
        'option8', 'option9', 'option10', 'die1', 'die2',
        'die3', 'die4', 'die5', 'die6', 'die7', 'die8',
        'die9', 'die10', 'originalPoints', 'points',
        'willingness', 'willingnessRand', 'started',
        'finished', 'created', 'updated']

    search_fields = ['username']

admin.site.register(HoltLaury, HoltLauryAdmin)

class GambleAdmin(admin.ModelAdmin):
    list_display = ['user', 'chosen', 'coin1', 'coin2',
        'coin3', 'coin4', 'coin5', 'coin6', 'coin7',
        'coin8', 'coin9', 'originalPoints', 'points',
        'willingness', 'willingnessRand', 'started',
        'finished', 'created', 'updated']

    search_fields = ['user']

admin.site.register(Gamble, GambleAdmin)

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'invested', 'returned0', 'returned1', 'returned2',
        'returned3', 'returned4', 'returned5', 'otheruser',
        'otherreturned', 'otherinvested', 'points', 'startedinvested',
        'finishedinvested', 'startedreturned0', 'finishedreturned0', 
        'startedreturned1', 'finishedreturned1', 
        'startedreturned2', 'finishedreturned2', 
        'startedreturned3', 'finishedreturned3', 
        'startedreturned4', 'finishedreturned4', 
        'startedreturned5', 'finishedreturned5', 'created', 'updated']

    search_fields = ['user']

admin.site.register(Investment, InvestmentAdmin)

class PretestAdmin(admin.ModelAdmin):
    list_display = ['user',
        'question1', 'question2',
        'question3', 'question4', 
        'question5', 'question6', 
        'question7', 
        'correct1', 'correct2',
        'correct3', 'correct4', 
        'correct5', 'correct6', 
        'correct7', 
        'questionclicked1', 'questionclicked2',
        'questionclicked3', 'questionclicked4', 
        'questionclicked5', 'questionclicked6', 
        'questionclicked7', 
        'questionrightclicked1', 'questionrightclicked2',
        'questionrightclicked3', 'questionrightclicked4', 
        'questionrightclicked5', 'questionrightclicked6', 
        'questionrightclicked7', 
        'questionhovered1', 'questionhovered2',
        'questionhovered3', 'questionhovered4', 
        'questionhovered5', 'questionhovered6', 
        'questionhovered7', 
        'questionhoveredseconds1', 'questionhoveredseconds2',
        'questionhoveredseconds3', 'questionhoveredseconds4', 
        'questionhoveredseconds5', 'questionhoveredseconds6', 
        'questionhoveredseconds7', 
        'startedquestion1', 'finishedquestion1', 
        'startedquestion2', 'finishedquestion2', 
        'startedquestion3', 'finishedquestion3', 
        'startedquestion4', 'finishedquestion4', 
        'startedquestion5', 'finishedquestion5', 
        'startedquestion6', 'finishedquestion6', 
        'startedquestion7', 'finishedquestion7', 
        'created', 'updated']

    search_fields = ['user']

admin.site.register(Pretest, PretestAdmin)

class ThankyouAdmin(admin.ModelAdmin):
    list_display = ['user', 'trainingComment', 'gamesComment',
        'pretestComment', 'created', 'updated']

    search_fields = ['user']

admin.site.register(Thankyou, ThankyouAdmin)


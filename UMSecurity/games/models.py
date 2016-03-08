from django.db import models

from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=200)
    firstgame = models.CharField(max_length=13, default="")
    secondgame = models.CharField(max_length=13, default="")
    thirdgame = models.CharField(max_length=13, default="")
    totalearning = models.FloatField(default=0)
    experimentearning = models.FloatField(default=0)
    startedstudy = models.DateTimeField(default=timezone.now)
    finishedstudy = models.DateTimeField(default=timezone.now)
    optout = models.BooleanField(default=0)
    postpone = models.BooleanField(default=0)

    # auto_now_add=True means it will return the date and time when the user signedup, and auto_now means it will return the date and time when it's updated.
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.username

class Pretest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question1 = models.IntegerField(default=-1)
    question2 = models.IntegerField(default=-1)
    question3 = models.IntegerField(default=-1)
    question4 = models.IntegerField(default=-1)
    question5 = models.IntegerField(default=-1)
    question6 = models.IntegerField(default=-1)
    question7 = models.IntegerField(default=-1)
    correct1 = models.IntegerField(default=-1)
    correct2 = models.IntegerField(default=-1)
    correct3 = models.IntegerField(default=-1)
    correct4 = models.IntegerField(default=-1)
    correct5 = models.IntegerField(default=-1)
    correct6 = models.IntegerField(default=-1)
    correct7 = models.IntegerField(default=-1)
    questionclicked1 = models.IntegerField(default=-1)
    questionclicked2 = models.IntegerField(default=-1)
    questionclicked3 = models.IntegerField(default=-1)
    questionclicked4 = models.IntegerField(default=-1)
    questionclicked5 = models.IntegerField(default=-1)
    questionclicked6 = models.IntegerField(default=-1)
    questionclicked7 = models.IntegerField(default=-1)
    questionrightclicked1 = models.IntegerField(default=-1)
    questionrightclicked2 = models.IntegerField(default=-1)
    questionrightclicked3 = models.IntegerField(default=-1)
    questionrightclicked4 = models.IntegerField(default=-1)
    questionrightclicked5 = models.IntegerField(default=-1)
    questionrightclicked6 = models.IntegerField(default=-1)
    questionrightclicked7 = models.IntegerField(default=-1)
    questionhovered1 = models.IntegerField(default=-1)
    questionhovered2 = models.IntegerField(default=-1)
    questionhovered3 = models.IntegerField(default=-1)
    questionhovered4 = models.IntegerField(default=-1)
    questionhovered5 = models.IntegerField(default=-1)
    questionhovered6 = models.IntegerField(default=-1)
    questionhovered7 = models.IntegerField(default=-1)
    questionhoveredseconds1 = models.FloatField(default=-1)
    questionhoveredseconds2 = models.FloatField(default=-1)
    questionhoveredseconds3 = models.FloatField(default=-1)
    questionhoveredseconds4 = models.FloatField(default=-1)
    questionhoveredseconds5 = models.FloatField(default=-1)
    questionhoveredseconds6 = models.FloatField(default=-1)
    questionhoveredseconds7 = models.FloatField(default=-1)
    startedquestion1 = models.DateTimeField(default=timezone.now)
    finishedquestion1 = models.DateTimeField(default=timezone.now)
    startedquestion2 = models.DateTimeField(default=timezone.now)
    finishedquestion2 = models.DateTimeField(default=timezone.now)
    startedquestion3 = models.DateTimeField(default=timezone.now)
    finishedquestion3 = models.DateTimeField(default=timezone.now)
    startedquestion4 = models.DateTimeField(default=timezone.now)
    finishedquestion4 = models.DateTimeField(default=timezone.now)
    startedquestion5 = models.DateTimeField(default=timezone.now)
    finishedquestion5 = models.DateTimeField(default=timezone.now)
    startedquestion6 = models.DateTimeField(default=timezone.now)
    finishedquestion6 = models.DateTimeField(default=timezone.now)
    startedquestion7 = models.DateTimeField(default=timezone.now)
    finishedquestion7 = models.DateTimeField(default=timezone.now)

    # auto_now_add=True means it will return the date and time when the user signedup, and auto_now means it will return the date and time when it's updated.
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username

class HoltLaury(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    decision = models.IntegerField(default=0)
    option1 = models.BooleanField(default=0)
    option2 = models.BooleanField(default=0)
    option3 = models.BooleanField(default=0)
    option4 = models.BooleanField(default=0)
    option5 = models.BooleanField(default=0)
    option6 = models.BooleanField(default=0)
    option7 = models.BooleanField(default=0)
    option8 = models.BooleanField(default=0)
    option9 = models.BooleanField(default=0)
    option10 = models.BooleanField(default=0)
    die1 = models.IntegerField(default=0)
    die2 = models.IntegerField(default=0)
    die3 = models.IntegerField(default=0)
    die4 = models.IntegerField(default=0)
    die5 = models.IntegerField(default=0)
    die6 = models.IntegerField(default=0)
    die7 = models.IntegerField(default=0)
    die8 = models.IntegerField(default=0)
    die9 = models.IntegerField(default=0)
    die10 = models.IntegerField(default=0)
    points = models.FloatField(default=0)
    originalPoints = models.FloatField(default=0)
    willingness = models.FloatField(default=0)
    willingnessRand = models.FloatField(default=16)
    started = models.DateTimeField(default=timezone.now)
    finished = models.DateTimeField(default=timezone.now)

    # auto_now_add=True means it will return the date and time when the user signedup, and auto_now means it will return the date and time when it's updated.
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username

class Gamble(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chosen = models.IntegerField(default=0)
    coin1 = models.BooleanField(default=0)
    coin2 = models.BooleanField(default=0)
    coin3 = models.BooleanField(default=0)
    coin4 = models.BooleanField(default=0)
    coin5 = models.BooleanField(default=0)
    coin6 = models.BooleanField(default=0)
    coin7 = models.BooleanField(default=0)
    coin8 = models.BooleanField(default=0)
    coin9 = models.BooleanField(default=0)
    points = models.FloatField(default=0)
    originalPoints = models.FloatField(default=0)
    willingness = models.FloatField(default=0)
    willingnessRand = models.FloatField(default=16)
    started = models.DateTimeField(default=timezone.now)
    finished = models.DateTimeField(default=timezone.now)

    # auto_now_add=True means it will return the date and time when the user signedup, and auto_now means it will return the date and time when it's updated.
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invested = models.IntegerField(default=-1)
    returned0 = models.IntegerField(default=-1)
    returned1 = models.IntegerField(default=-1)
    returned2 = models.IntegerField(default=-1)
    returned3 = models.IntegerField(default=-1)
    returned4 = models.IntegerField(default=-1)
    returned5 = models.IntegerField(default=-1)
    otheruser = models.ForeignKey(User, related_name="otherreturned_set", null=True)
    otherreturned = models.IntegerField(default=-1)
    otherinvested = models.IntegerField(default=-1)
    points = models.IntegerField(default=-1)
    startedinvested = models.DateTimeField(default=timezone.now)
    finishedinvested = models.DateTimeField(default=timezone.now)
    startedreturned0 = models.DateTimeField(default=timezone.now)
    finishedreturned0 = models.DateTimeField(default=timezone.now)
    startedreturned1 = models.DateTimeField(default=timezone.now)
    finishedreturned1 = models.DateTimeField(default=timezone.now)
    startedreturned2 = models.DateTimeField(default=timezone.now)
    finishedreturned2 = models.DateTimeField(default=timezone.now)
    startedreturned3 = models.DateTimeField(default=timezone.now)
    finishedreturned3 = models.DateTimeField(default=timezone.now)
    startedreturned4 = models.DateTimeField(default=timezone.now)
    finishedreturned4 = models.DateTimeField(default=timezone.now)
    startedreturned5 = models.DateTimeField(default=timezone.now)
    finishedreturned5 = models.DateTimeField(default=timezone.now)

    # auto_now_add=True means it will return the date and time when the user signedup, and auto_now means it will return the date and time when it's updated.
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username

class Thankyou(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pretestComment = models.TextField(null=True, blank=True)
    trainingComment = models.TextField(null=True, blank=True)
    gamesComment = models.TextField(null=True, blank=True)

    # auto_now_add=True means it will return the date and time when the user signedup, and auto_now means it will return the date and time when it's updated.
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username


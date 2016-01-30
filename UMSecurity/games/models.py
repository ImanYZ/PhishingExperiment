from django.db import models

from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=200)

    # auto_now_add=True means it will return the date and time when the user signedup, and auto_now means it will return the date and time when it's updated.
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.username

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
    points = models.IntegerField(default=0)
    originalPoints = models.IntegerField(default=0)
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
    points = models.IntegerField(default=0)
    originalPoints = models.IntegerField(default=0)
    willingness = models.FloatField(default=0)
    willingnessRand = models.FloatField(default=16)
    started = models.DateTimeField(default=timezone.now)
    finished = models.DateTimeField(default=timezone.now)

    # auto_now_add=True means it will return the date and time when the user signedup, and auto_now means it will return the date and time when it's updated.
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username


from django.contrib import admin

from .models import User
from .models import HoltLaury

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'created', 'updated']

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

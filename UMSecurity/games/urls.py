from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

app_name = 'games'
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/games/lottery'), name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^lottery/$', views.lottery, name='lottery'),
    url(r'^lottery/Submit$', views.lotterySubmit, name='lotterySubmit'),
    url(r'^lottery/Willingness$', views.lotteryWillingness, name='lotteryWillingness'),
    url(r'^gamble/$', views.gamble, name='gamble'),
    url(r'^gamble/Submit$', views.gambleSubmit, name='gambleSubmit'),
    url(r'^gamble/Willingness$', views.gambleWillingness, name='gambleWillingness'),
]
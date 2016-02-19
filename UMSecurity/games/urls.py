from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

app_name = 'games'
urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^pretest/(?P<question>[0-9]+)/$', views.pretest, name='pretest'),
    url(r'^pretest/Submit$', views.pretestsubmit, name='pretestsubmit'),
    url(r'^pretest/results$', views.pretestresults, name='pretestresults'),
    url(r'^training/$', views.training, name='training'),
    url(r'^gameselection/$', views.gameselection, name='gameselection'),
    url(r'^nextgame/(?P<current>[a-zA-Z]+)/$', views.nextgame, name='nextgame'),
    url(r'^lottery/$', views.lottery, name='lottery'),
    url(r'^lottery/Submit$', views.lotterySubmit, name='lotterySubmit'),
    url(r'^lottery/Willingness$', views.lotteryWillingness, name='lotteryWillingness'),
    url(r'^gamble/$', views.gamble, name='gamble'),
    url(r'^gamble/Submit$', views.gambleSubmit, name='gambleSubmit'),
    url(r'^gamble/Willingness$', views.gambleWillingness, name='gambleWillingness'),
    url(r'^investment/$', views.investment, name='investment'),
    url(r'^investment/Submit$', views.investmentSubmit, name='investmentSubmit'),
    url(r'^returning/(?P<part>[0-9]+)/$', views.returned, name='returned'),
    url(r'^returning/Submit$', views.returnedSubmit, name='returnedSubmit'),
    url(r'^returning/final$', views.final, name='final'),
    url(r'^thankyou/$', views.thankyou, name='thankyou'),
    url(r'^thankyou/submit$', views.thankyousubmit, name='thankyousubmit'),
]
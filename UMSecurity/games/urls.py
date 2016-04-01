from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.conf import settings

from . import views

app_name = 'games'
urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'games/media/blockm.png')),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^pretest/(?P<question>[0-9]+)/$', views.pretest, name='pretest'),
    url(r'^pretest/Submit$', views.pretestsubmit, name='pretestsubmit'),
    url(r'^pretest/results$', views.pretestresults, name='pretestresults'),
    url(r'^training/(?P<question>[0-9]+)$', views.training, name='training'),
    url(r'^training/Submit$', views.pretestsubmit, name='pretestsubmit'),
    url(r'^optout/$', views.optout, name='optout'),
    url(r'^postpone/$', views.postpone, name='postpone'),
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
    url(r'^results/$', views.results, name='results'),
    url(r'^(?i)downloadCSV', views.downloadCSV, name='downloadCSV'),
]
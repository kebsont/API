from django.conf.urls import url


from .views import MailingPostRudView, MailingPostAPIView

urlpatterns = [
    url(r'^$', MailingPostAPIView.as_view(), name='mail-listcreate'),
    url(r'^(?P<pk>\d+)/$', MailingPostRudView.as_view(), name='post-rud')
]

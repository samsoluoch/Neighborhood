from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static







urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search_business, name='search_business'),
    url(r'^signup/', views.register, name='signup'),
    url(r'^edit/', views.edit_profile, name='edit_profile'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^post/$', views.upload_post, name='upload_post'),
    url(r'^home/(\d+)', views.home, name='home'),
    url(r'^business/(\d+)', views.business, name='business'),
    url(r'^add_business/$', views.add_business, name='add_business'),
    url(r'^comment/(?P<post_id>\d+)', views.add_comment, name='comment'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
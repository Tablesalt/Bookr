from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^account/', views.private_account, name='account'),
    url(r'^sell/', views.sell, name='sell'),
    url(r'^book/(?P<book_id>[0-9]+)/$', views.book, name='book')

]
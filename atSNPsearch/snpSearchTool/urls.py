from django.conf.urls import url

from . import views

  #this is required to add another view?

app_name = 'snpSearchTool'
#include at least one example of a valid matching url for each of these.
urlpatterns = [
  #example: snpSearchTool/index
  url(r'^$', views.index, name='index'),

  #example :snpSearchTool/results/3
  url(r'^results/(?P<requested_snpid>[0-9]*)', views.results, name='results'),

  #example :snpSearchTool/3/detail
  url(r'^(?P<id_of_scoresrow>[0-9]*)/detail', views.detail , name='detail'),
  #url(r'^(?P<id_of_requested_row>[0-9]*)/detail', views.detail , name='detail'),
  

  #example: snpSearchTool/controlset
  url(r'^controlset$', views.controlset, name='controlset'),

  url(r'^lookup_one_snp$', views.lookup_one_snp, name='lookup_one_snp'),
]

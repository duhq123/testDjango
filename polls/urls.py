from django.urls import path
from django.conf.urls import url

from . import views

from . import views as imgs_db
from django.conf.urls.static import static

app_name = 'polls'
urlpatterns = [
    # # ex: / polls /
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.IndexView.as_view(), name='index'),
    path('upload', views.loadView),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('user/', views.TestView.as_view()),
    url(r'^up_imgs', imgs_db.up_imgs),
    url(r'^upload_imgs', imgs_db.upload_imgs),

]

from django.urls import path
from .views import allergy_prediction,  electrolyte_prediction


#from .views import home
from .import views



urlpatterns = [
    path('',views.home, name='home'),  #Home Page
    path('about/',views.about, name='about'),  #About page
    path('contact/',views.contact, name='contact'), #Contact page
    path('resume/', views.resume, name='resume'),  #resume page
    path('github/',views.github, name='github'), # github resource
    path('publication/', views.publication, name='publication'), # publicaton article
    path('photography/',views.photography, name='photography'), # data_scince_projects_show
    path('data_science_blog/',views.data_science_blog, name='data_science_blog'), # data_scince_projects_show

    path('allergy_prediction/', views.allergy_prediction, name='allergy_prediction'),  # allergy_prediction
    path('electrolyte_prediction/', views.electrolyte_prediction, name='electrolyte_prediction'),  # electrolyte_prediction
    path('blogs_1/',views.blogs_1, name='blogs_1'),  #blogs1
    path('blogs_2/',views.blogs_2, name='blogs_2'),  #blogs1
    path('blogs_3/',views.blogs_3, name='blogs_3'),  #blogs1
    path('blogs_4/',views.blogs_4, name='blogs_4'),  #blogs1
    path('blogs/notebook/', views.render_notebook_tmdb_movies, name='render_notebook_tmdb_movies'),
    path('blogs/notebook', views.render_notebook_T20_World_cup,name='render_notebook_T20_World_cup'),
    path('blogs_5/',views.blogs_5, name='blogs_5'),  #blogs1
    path('blogs_6/',views.blogs_6, name='blogs_6'),  #blogs1




    path('hh/',views.hh, name='hh'), # data_scince_projects_show    
]

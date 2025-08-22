from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    # Movie URLs
    path('movies/', views.MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movies/create/', views.MovieCreateView.as_view(), name='movie_create'),
    path('movies/<int:pk>/update/', views.MovieUpdateView.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
    # Review management page
    path('manage/<int:movie_id>/', views.manage, name='manage'),
    # Review URLs
    path('', views.index, name='index'),
    path('create/<int:movie_id>/', views.create, name='create'),
    path('delete/<int:review_id>/', views.delete, name='delete'),
    path('update/<int:review_id>/', views.update, name='update'),
]
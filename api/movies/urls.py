from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_put_delete_movie'),
    path('<int:pk>/comments/', views.ListCreateCommentAPIView.as_view(), name='get_post_comments'),
    path('<int:pk>/comments/<int:comment_pk>/', views.RetrieveUpdateDestroyCommentAPIView.as_view(), name='get_put_delete_comment'),
    path('<int:pk>/votes/', views.ListCreateVoteAPIView.as_view(), name='get_post_votes'),
    path('<int:pk>/votes/<int:vote_pk>/', views.RetrieveUpdateDestroyVoteAPIView.as_view(), name='get_put_delete_vote'),
]
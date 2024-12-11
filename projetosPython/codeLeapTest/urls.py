from django.urls import path
from .views import PostListCreate, PostRetrieveUpdateDestroy

urlpatterns = [
    path('careers/', PostListCreate.as_view(), name='post_list_create'),
    path('careers/<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post_retrieve_update_destroy'),
]

from django.urls import path, include
from . import views

from rest_framework import routers

# urlpatterns = [
#     path('', views.blogApiOverview, name="blog-overview"),
#     path('list/', views.blogList, name="blog-list"),
#     path('detail/<str:pk>/', views.blogDetail, name="blog-detail"),
#     path('create/', views.blogCreate, name="blog-create"),
#     path('update/<str:pk>/', views.blogUpdate, name="blog-update"),
#     path('delete/<str:pk>/', views.blogDelete, name="blog-delete"),
# ]

router = routers.DefaultRouter()
router.register('blogs', views.BlogView)

urlpatterns = [
    path('', include(router.urls)),
]
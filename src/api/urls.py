from django.urls import path, include
from . import views

from rest_framework import routers

# urlpatterns = [
#     path('', views.apiOverview, name="api-overview"),
#     path('list/', views.userList, name="user-list"),
#     path('detail/<str:pk>/', views.userDetail, name="user-detail"),
#     path('create/', views.userCreate, name="user-create"),
#     path('update/<str:pk>/', views.userUpdate, name="user-update"),
#     path('delete/<str:pk>/', views.userDelete, name="user-delete"),
# ]

router = routers.DefaultRouter()
router.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls))
]

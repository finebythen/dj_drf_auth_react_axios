from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from .views import MyTokenObtainPairView


urlpatterns = [
    # routes
    path('routes/', views.apiRoutes, name="routes"),

    path('authors/', views.apiAuthors, name="authors"),
    path('author/<int:pk>/', views.apiAuthor, name="author"),

    path('books/', views.apiBooks, name="books"),
    path('book/<int:pk>/', views.apiBook, name="book"),

    # token routes
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
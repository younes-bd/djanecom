from django.urls import path
from . import views



urlpatterns =[
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #path('login/', views.LoginAPIView.as_view(), name="login"),
    path('register/', views.registerUser, name= 'register'),
    path('email-verify/', views.VerifyEmail.as_view(), name="email-verify"),
    path('profile/', views.getUserProfile, name= "users-profile"),
    path('profile/update/', views.updateUserProfile, name= "user-profile-update"),
    path('', views.getUsers, name= "users"),

    path('<str:pk>/', views.getUserById, name= "user"),
    path('update/<str:pk>/', views.updateUser, name= "user-update"),
    path('delete/<str:pk>/', views.deleteUser, name= "user-delete"),

]
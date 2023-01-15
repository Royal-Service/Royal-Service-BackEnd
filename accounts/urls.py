from django.urls import path
from accounts.views import MyObtainTokenPairView, RegisterView,CustmerProfileView,CraftsmanProfileView,CraftsmanView,CraftsmanProfileEdit
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),

    path('profile/<int:pk>/', CustmerProfileView.as_view(), name='Custmer_profile'),

    path('Craftsmans/', CraftsmanView.as_view(), name='Craftsman_list'),
    path('Craftsmans/profile/<int:pk>', CraftsmanProfileView.as_view(), name='Craftsman_profile'),
    path('Craftsmans/profile/edit/<int:pk>', CraftsmanProfileEdit.as_view(), name='Craftsman_edit'),


]
























# from django.urls import path, include
# from .views import (
#     CreateUserView, LoginView, UpdatePasswordView, MeView,
#     UserActivitiesView, UsersView
# )

# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter(trailing_slash=False)

# router.register("create-user", CreateUserView, 'create user')
# # router.register("login", LoginView, 'login')
# router.register("update-password", UpdatePasswordView, 'update password')
# router.register("me", MeView, 'me')
# router.register("activities-log", UserActivitiesView, 'activities log')
# router.register("users", UsersView, 'users')

# urlpatterns = [
#     path("", include(router.urls)),
#     path('login/', TokenObtainPairView.as_view()),
# ]
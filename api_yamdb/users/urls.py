from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users import views

urlpatterns = [
    path(
        'auth/token/',
        views.GetRefreshTokens.as_view(),
        name='get_token'
    ),
    path(
        'auth/token/refresh',
        views.GetRefreshTokens.as_view(),
        name='refresh_token'
    ),
    path(
        'auth/email/',
        views.send_confirmation_code,
        name='send_confirmation_code'
    ),
]

router = DefaultRouter()
router.register('users', views.UsersViewSet, basename='users')

urlpatterns += [
    path('', include(router.urls)),
]

from django.contrib.auth import views as auth_views
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView

from user import apis

router = SimpleRouter()
router.register("accounts", apis.UserViewSet)

auth_urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", apis.RegisterUser.as_view(), name="register_user"),
]

urlpatterns = [
    path("auth/", include(auth_urlpatterns)),
    path("", include(router.urls)),
    path("accounts/all", apis.GetAllUser.as_view(), name="get_all_users"),
]

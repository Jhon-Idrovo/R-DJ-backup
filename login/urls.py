from django.urls import path, re_path
from .views import BlacklistTokenView, CreateUser, Home

app_name = 'login'

urlpatterns = [
    path('logout/', BlacklistTokenView.as_view(), name='logout'),
    path('register/', CreateUser.as_view(), name='register'),
    re_path('.*', Home.as_view(template_name='index.html'))
]
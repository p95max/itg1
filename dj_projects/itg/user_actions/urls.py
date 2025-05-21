from django.urls import path
from user_actions.views import (user_action)

app_name = 'user_actions'

urlpatterns = [
    path('user_action/', user_action, name='user_action'),

]
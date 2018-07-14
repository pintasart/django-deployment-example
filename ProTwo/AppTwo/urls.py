from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    # url('',views.help,name="help"),
    url('',views.users,name="users"),
    
]
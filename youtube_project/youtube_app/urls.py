from django.urls import path
from . import views

app_name='youtube_app'

urlpatterns = [
    path('',views.home,name="homepage"),
    path('linksubmit',views.submit,name='submit'),
    path('<str:pixel>',views.down,name='download'),
]
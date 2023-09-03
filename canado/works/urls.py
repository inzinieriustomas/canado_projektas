from django.urls import path
from .views import create_work

app_name = 'works'
urlpatterns = [
    # path('works/', views.works_list, name='works-list'),
    # path("priskirti_darbuotoja/", views.priskirti_darbuotoja, name="priskirti_darbuotoja"),
    path('create_work/', create_work, name='create_work'),
    path ('works/', create_work, name='works_list'),

]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.draw_menu_view, name='draw_menu'),
    path('<str:selected_node>/', views.draw_menu_view, name='draw_menu'),
]

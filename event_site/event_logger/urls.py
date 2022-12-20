from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('create', views.create_event, name='create_event'),
    path('<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('<int:pk>/update', views.EventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/delete', views.EventDeleteView.as_view(), name='event-delete'),
]

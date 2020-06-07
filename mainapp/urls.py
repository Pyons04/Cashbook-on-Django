from django.urls import path

from . import views

app_name = "mainapp"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index', views.IndexView.as_view(), name='index'),
    path('usage', views.UsageView.as_view(), name='usage'),
    path('usage-delete/<int:pk>', views.UsageDeleteView.as_view(), name='usage_delete'),
    path('genre-delete/<int:pk>', views.GenreDeleteView.as_view(), name='genre_delete'),
    path('usage-edit/<int:pk>'  , views.UsageUpdateView.as_view(), name='usage_edit'),
    path('summary', views.SummaryView.as_view(), name='summary'),
]


from django.urls import include, path
from . import views

app_name = "teachers"


urlpatterns = [
    path('', views.default, name='default'),

    path(
        route="requests/edit/<slug:slug>/",
        view=views.TeachersUpdateView.as_view(),
    ),

    path(
        route="requests",
        view=views.TeachersListView.as_view(),
    ),

]
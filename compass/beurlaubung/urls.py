from django.urls import include, path
from . import views

app_name = "beurlaubung"


urlpatterns = [
   path('', views.default, name='default'),

    path(
        route="status/<slug:slug>/",
        view=views.BeurlaubungDetailView.as_view(),
        name="detail"
    ),
   path(
        route="antrag/",
        view=views.BeurlaubungCreateView.as_view(),
        name="antrag"
    ),
]
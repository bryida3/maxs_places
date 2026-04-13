from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.place, name="place"),
    path("<str:mun>/", views.municipality, name="municipality"),
]

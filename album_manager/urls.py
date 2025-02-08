# Ingresar tus URLs de la app aquí
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_artistas, name='listar_artistas'),
    path('artista/nuevo/', views.nuevo_artista, name='nuevo_artista'),
    path('artista/<int:artista_id>/', views.detalle_artista, name='detalle_artista'),
    path('artista/<int:artista_id>/editar/', views.editar_artista, name='editar_artista'),
    path('artista/<int:artista_id>/eliminar/', views.eliminar_artista, name='eliminar_artista'),
    path('albums/', views.listar_albums, name='listar_albums'),
    path('album/nuevo/', views.nuevo_album, name='nuevo_album'),
    path('album/<int:album_id>/', views.detalle_album, name='detalle_album'),
    path('album/<int:album_id>/editar/', views.editar_album, name='editar_album'),
    path('album/<int:album_id>/eliminar/', views.eliminar_album, name='eliminar_album'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]


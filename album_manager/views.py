from django.http import HttpResponse
from django.template import loader
from .models import Album, Artista
from django.shortcuts import redirect, render
from .forms import AlbumForm, ArtistaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


def listar_artistas(request):
    artistas = Artista.objects.all()
    template = loader.get_template('artista_list.html')
    return HttpResponse(template.render({
        'artistas': artistas,
    }, request))

def detalle_artista(request, artista_id):
    artista = Artista.objects.get(id=artista_id)
    template = loader.get_template('artista_detail.html')
    context = {
        'artista': artista
    }
    return HttpResponse(template.render(context, request))

@login_required
def nuevo_artista(request):
    if request.method == "POST":
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_artistas')
    else:
        form = ArtistaForm()

    return render(request, 'artista_form.html', {'form': form})

@login_required
def editar_artista(request, artista_id):
    artista = Artista.objects.get(id=artista_id)
    if request.method == "POST":
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('detalle_artista', artista_id=artista.id)
    else:
        form = ArtistaForm(instance=artista)
    
    return render(request, 'artista_form.html', {'form': form})

@login_required
def eliminar_artista(request, artista_id):
    artista = Artista.objects.get(id=artista_id)
    artista.delete()
    return redirect('listar_artistas')

def listar_albums(request):
    albums = Album.objects.all()
    template = loader.get_template('album_list.html')
    return HttpResponse(template.render({
        'albums': albums,
    }, request))

def detalle_album(request, album_id):
    album = Album.objects.get(id=album_id)
    template = loader.get_template('album_detail.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))

@login_required
def nuevo_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_albums')
    else:
        form = AlbumForm()

    return render(request, 'album_form.html', {'form': form})

@login_required
def editar_album(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('detalle_album', album_id=album.id)
    else:
        form = AlbumForm(instance=album)
    
    return render(request, 'album_form.html', {'form': form})

@login_required
def eliminar_album(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('listar_albums')


class CustomLoginView(LoginView):
    template_name = "login.html"

def logout_view(request):
    logout(request)
    return redirect('listar_artistas')

from django.shortcuts import render
from musician.models import Musician
from album.models import Album

def home(request):
    # Query all musicians and albums from the database
    musicians = Musician.objects.all()
    albums = Album.objects.all()
    
    # Pass the queried data to the template context
    context = {
        'musicians': musicians,
        'albums': albums,
    }
    
    # Render the home.html template with the provided context
    return render(request, 'home.html', context)

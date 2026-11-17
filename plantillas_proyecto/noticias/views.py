from django.shortcuts import render


def home(request):
    return render(request, 'noticias/home.html')


def detalle(request, id):
    # Noticia de ejemplo (todavía no usamos base de datos)
    noticia = {
        'titulo': f'Noticia #{id}',
        'contenido': 'Este es el contenido de ejemplo de la noticia, '
                     'mostrado con la misma estructura de base.html.',
    }
    return render(request, 'noticias/detalle.html', {'noticia': noticia})

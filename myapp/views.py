from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Url
from .serializer import UrlSerializer
import string
import random
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")

def generate_short_url():
    """Generate a random 6-character string"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

def shorten_url(request):
    """Handle URL shortening"""
    if request.method == 'POST':
        long_url = request.POST.get('url')
        if not long_url:
            return JsonResponse({'error': 'URL is required'}, status=400)
        
        # Generate a unique short URL code
        while True:
            short_url_code = generate_short_url()
            if not Url.objects.filter(short_url=short_url_code).exists():
                break
        
        # Save ONLY the short code to the database
        url_obj = Url(origin_url=long_url, short_url=short_url_code)
        url_obj.save()
        
        # Construct the full URL for display to the user
        scheme = request.scheme  # 'http' or 'https'
        host = request.get_host()  # Includes domain and port
        complete_short_url = f'{scheme}://{host}/{short_url_code}'
        
        # Return the shortened URL
        return JsonResponse({
            'original_url': long_url,
            'short_url': complete_short_url,
        })
    else:
        return render(request, 'shorten.html')
      
def redirect_to_original(request, short_url):
    """Redirect to the original URL"""
    try:
        url_obj = Url.objects.get(short_url=short_url)
        return redirect(url_obj.origin_url)
    except Url.DoesNotExist:
        return JsonResponse({'error': 'URL not found'}, status=404)

class UrlViewSet(viewsets.ModelViewSet):
  queryset = Url.objects.all()
  serializer_class = UrlSerializer
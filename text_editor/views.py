from django.shortcuts import render, get_object_or_404  # Correct imports
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'text_editor/index.html', {'articles': articles})
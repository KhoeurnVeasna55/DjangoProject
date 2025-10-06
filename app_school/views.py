from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def content(request):
    return render(request, 'pages/content.html')
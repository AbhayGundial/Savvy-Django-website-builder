from django.shortcuts import render

def index(request):
    return render(request, 'blog/blog_index_page.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'contact/contact_page.html')

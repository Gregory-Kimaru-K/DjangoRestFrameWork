from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def blog_list(request):
    blogs = Task.objects.all()
    return render(request, 'bloglist.html', {'blogs' : blogs})

def blog_dets(request, pk):
    blog = get_object_or_404(Task, pk=pk)
    serializer = TaskSerializer(blog)
    return render(request, 'blogdets.html', {'blog':serializer.data})

def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        blog = Task(title=title, content=content)
        blog.save()

        return redirect('blog_list')
    return render(request, 'create.html')

def update_blog(request, pk):
    blog = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.save()
        return redirect('blog_details', pk=pk)
    return render(request, 'blog_form.html', {'blog' : blog})

def delete_blog(request, pk):
    blog = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    
    return render(request, '404.html')
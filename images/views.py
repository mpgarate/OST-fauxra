from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from images.models import Image
from images.forms import ImageForm

import cloudinary

def index(request):
    images = Image.objects.all()
    context = { 'images': images}
    return render(request, 'images/index.html', context)

def show(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    context = { 'image': image }
    return render(request, 'images/show.html', context)

def new(request):
    form = ImageForm()
    context =  { 'form': form }
    return render(request, 'images/new.html', context)

def create(request):
    form = ImageForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('images:index')

    return redirect('images:new')



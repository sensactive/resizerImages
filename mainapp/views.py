from django.shortcuts import render, get_object_or_404
from .models import Picture
from .forms import PictureUploadForm, PictureUpdateForm
from PIL import Image
import os
from django import forms
# Create your views here.


def main_view(request):
    pictures = Picture.objects.all()

    content = {
        'pictures': pictures,
    }

    return render(request, 'mainapp/index.html', content)

def upload_image(request):

    if request.method == 'POST':
        upload_form = PictureUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
    else:
        upload_form = PictureUploadForm()

    content = {
        'upload_form': upload_form,
    }

    return render(request, 'mainapp/upload.html', content)

def get_picture(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    error = ''
    if request.method == 'POST':
        form = PictureUpdateForm(request.POST)
        if form.is_valid():
            # Получаем путь к файлу картинки
            filename = picture.img.path
            # Получаем ширину из формы
            width = int(request.POST['width'])
            # Получаем высоту из формы
            height = int(request.POST['height'])
            # Получаем минимальный размер файлы из формы
            size = int(request.POST['size'])
            image = Image.open(filename)
            # Создаем копию изображения и сохраняем, чтобы узнать размер файла при высоте и ширине из запроса
            tmpImg = image.copy()
            tmpImg = tmpImg.resize((width, height), Image.ANTIALIAS)
            tmpImg.save('tempimage.jpg')
            if os.path.getsize('tempimage.jpg') < size:
                os.remove('tempimage.jpg')
                error = 'При таких параметрах ширины и высоты размер файла будет меньше, чем size'
            else:
                os.remove('tempimage.jpg')
                image = image.resize((width, height), Image.ANTIALIAS)
                image.save(filename)

    else:
        form = PictureUpdateForm(initial={
            'width': picture.img.width,
            'height': picture.img.height
        })

    content = {
        'error': error,
        'picture': picture,
        'form': form,
    }

    return render(request, 'mainapp/picture.html', content)
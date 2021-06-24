from django.shortcuts import render
from .models import Pictures, Dog_pics, Tech_pics
from .forms import pictures_form
from django.template import RequestContext


# Create your views here.
def home(args):
    pics = Pictures.objects.all().order_by('-added_on')
    return render(args, 'home.html', {'pics': pics})


def upload_pictures(request):
    if request.method == "POST":
        form = pictures_form(request.POST, request.FILES)
        if form.is_valid():
            posted_name = form.cleaned_data.get('name')
            posted_image = form.cleaned_data.get('image')
            web_form = Pictures.objects.create(
                name=posted_name,
                image=posted_image
            )
            web_form.save()

    else:
        form = pictures_form()
    return render(request, 'post_pictures.html', {'form': form})


def details(args):
    pass


def view_dogs(args):
    pics = Dog_pics.objects.all().order_by('-added_on')
    return render(args, 'dogs.html', {'pics': pics})


def view_tech(args):
    pics = Tech_pics.objects.all().order_by('-added_on')
    return render(args, 'tech.html', {'pics': pics})


def handler404(request, *args, **argv):
    response = render('base.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render('base.html', {})

    response.status_code = 500
    return response

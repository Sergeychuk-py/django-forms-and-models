from django.shortcuts import render
from app_forms.forms import MyForms

def index(request):
    if request.method == "POST":
        form = MyForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForms()

    return render(request, "app_forms/index.html", {'form': form})


def final(request):
    return render(request, 'final.html')



from django.contrib import messages
from django.shortcuts import render
from app_forms.forms import MyForms

# def index(request):
#     if request.method == "POST":
#         form = MyForms(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = MyForms()
#
#     return render(request, "app_forms/index.html", {'form': form})


def index(request):
    if request.method == "POST":
        form = MyForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact request submitted successfully.')
            return render(request, 'app_forms/messages.html', {'form': MyForms(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = MyForms()
    return render(request, 'app_forms/index.html', {'form': form})



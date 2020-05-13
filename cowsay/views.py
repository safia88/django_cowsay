from django.shortcuts import render, reverse, HttpResponseRedirect
from cowsay.models import CowSay
from cowsay.forms import AddCowSayForm
from django.shortcuts import redirect
from django.contrib import messages


def add_cowsay(request):
    html = "add_cowsay.html"
    form = None
    # message = None
    if request.method == "POST":
        form = AddCowSayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowSay.objects.create(
                title=data["title"]
            )
            # message = 'Test'
            messages.success(request, 'Form submission successful')
            form = AddCowSayForm()
            return redirect('/')
            # form = AddCowSayForm()
            # return HttpResponseRedirect(reverse('homepage'))
    else:
        form = AddCowSayForm()
    return render(request, html, {"form": form})


def history(request):
    return render(request, 'history.html', {'list': CowSay.objects.all()})

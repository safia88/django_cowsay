from django.shortcuts import render, redirect
from cowsay.forms import CowsayForm
from cowsay.models import Cowsay
import subprocess as sp
import platform


def insert_view(request):
    if request.method == 'POST':
        form = CowsayForm(request.POST)
        if form.is_valid():
            name = request.POST['cowsay_string']
            form.save()
            if platform.system() == "Windows":
                expand_shell = True
            else:
                expand_shell = False
            s = sp.check_output(
                ['cowsay', name], universal_newlines=True, stderr=sp.STDOUT, shell=expand_shell)
            return render(request, 'cowsay.html', {'name': s})
    return render(request, 'cowsay.html')


def history(request):
    cowsay_list = Cowsay.objects.values('cowsay_string').order_by('-id')[:10]
    newList = []
    if platform.system() == "Windows":
        expand_shell = True
    else:
        expand_shell = False

    for item in cowsay_list:
        s = sp.check_output(
            ['cowsay', item['cowsay_string']], universal_newlines=True, stderr=sp.STDOUT, shell=expand_shell)
        newList.append(s)

    return render(request, 'history.html', {'cowsay_list': newList})

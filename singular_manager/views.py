from django.shortcuts import render, redirect, get_object_or_404
from news.models import News
from .models import Singular_Manager
from django.contrib.auth.models import User, Group, Permission

def trending_list(request):
    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        return render(request, 'back/error.html', {'error': error})


    newstrend = News.objects.filter(trending=True)


    return render(request, 'back/trending_list.html', {'newstrend': newstrend})

def trending_remove(request, pk):

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        return render(request, 'back/error.html', {'error': error})


    obj = News.objects.get(pk=pk)

    obj.trending = False
    
    obj.save()


    return redirect('trending_list')

def identifier_home_list(request):

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        return render(request, 'back/error.html', {'error': error})


    obj = Singular_Manager.objects.all()


    return render(request, 'back/identifier_home_list.html', {'obj': obj})

def identifier_home_add(request):

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        return render(request, 'back/error.html', {'error': error})


    if request.method == 'POST':

        identifier_home = request.POST.get('identifier_home')

        if identifier_home == "" :
            error = 'Fill all the required details.'
            return render(request, 'back/error.html', {'error': error})

        else :
            obj = Singular_Manager(identifier_home=identifier_home)

            obj.save()


    return render(request, 'back/identifier_home_add.html')

def identifier_home_edit(request, pk):

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        return render(request, 'back/error.html', {'error': error})


    obj = Singular_Manager.objects.get(pk=pk)

    if request.method == 'POST' :

        identifier_home = request.POST.get('identifier_home')

        if identifier_home == "":
            error = 'Fill all the required details.'
            return render(request, 'back/error.html', {'error': error})

        else :

            obj.identifier_home = identifier_home

            obj.save()
            
            return redirect(identifier_home_list)

    return render(request, 'back/identifier_home_edit.html', {'obj': obj, 'pk':pk})

def identifier_home_remove(request, pk):

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        return render(request, 'back/error.html', {'error': error})


    obj = Singular_Manager.objects.get(pk=pk)

    obj.delete()

    return redirect(identifier_home_list)

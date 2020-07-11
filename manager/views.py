from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Manager
from news.models import News
from category.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


def manager_list(request) :

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})

    manager = Manager.objects.all()

    return render(request, 'back/manager_list.html', {'manager': manager})



def manager_in_groups(request, pk) :
    
    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})

    manager = Manager.objects.get(pk=pk)

    user = User.objects.get(username=manager.username)

    user_group = []

    for i in user.groups.all() :
        user_group.append(i)

    group = Group.objects.all()


    distinct_vals = list(set(group).difference(set(user_group)))

    # distinct_vals = np.setdiff1d(list(group), list(user_group), assume_unique=False)


    return render(request, 'back/manager_in_groups.html', {'group': group, 'user_group': user_group, 'distinct_vals': distinct_vals, 'pk': pk})



def add_manager_to_group(request, pk):

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST' :

        group_name = request.POST.get('group_name')
        
        group = Group.objects.get(name=group_name)
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.username)
        user.groups.add(group)

    return redirect('manager_in_groups', pk=pk)



def manager_permission(request, pk) :
    
    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})


    manager = Manager.objects.get(pk=pk)

    user = User.objects.get(username=manager.username)

    permission = Permission.objects.filter(user=user)

    user_permission = []

    for i in permission :
        user_permission.append(i)

    # Show distinct values in permission add drop-down
    all_permissions = Permission.objects.all()
    user_permissions = Permission.objects.filter(user=user)

    distinct_perms = list(set(all_permissions).difference(set(user_permissions)))


    return render(request, 'back/manager_permission.html', {'user_permission': user_permission, 'distinct_perms': distinct_perms, 'pk': pk})


def manager_permission_delete(request, pk, name) :
    
    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})


    manager = Manager.objects.get(pk=pk)

    user = User.objects.get(username=manager.username)

    permission = Permission.objects.get(name=name)
    user.user_permissions.remove(permission)


    return redirect('manager_permission', pk=pk)


def manager_permission_add(request, pk) :
    
    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})

    
    if request.method == 'POST' :

        permission_name = request.POST.get('permission_name')

        manager = Manager.objects.get(pk=pk)

        user = User.objects.get(username=manager.username)

        permission = Permission.objects.get(name=permission_name)
        user.user_permissions.add(permission)


    return redirect('manager_permission', pk=pk)



def del_group_from_manager(request, name, pk):

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})

    group = Group.objects.get(name=name)
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.username)
    
    user.groups.remove(group)

    return redirect('manager_in_groups', pk=pk)



def manager_delete(request, pk) :

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})

    manager = Manager.objects.get(pk=pk)

    try:
        obj = User.objects.get(username = manager.username)
        obj.delete()

        manager.delete()
    except :
        manager.delete()


    return redirect('manager_list')



def group(request) :

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})

    group = Group.objects.all().exclude(name="masteruser")


    return render(request, 'back/groups.html', {'group': group})



def group_add(request) :

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST' :

        name = request.POST.get('group_name')

        if name != "" :

            if len(Group.objects.filter(name=name)) == 0 :

                obj = Group(name=name)
                obj.save()

    return redirect('group')



def group_delete(request, name) :

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})

    obj = Group.objects.get(name=name)
    obj.delete()

    return redirect('group')



def permission(request) :

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})

    perms = Permission.objects.all()


    return render(request, 'back/permissions.html', {'perms': perms})



def permission_delete(request, name) :

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :
        error = "Access Denied ! "
        
        return render(request, 'back/error.html', {'error': error})

    perm = Permission.objects.get(name=name)
    perm.delete()

    return redirect('permission')


def permission_add(request) :

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :

        error = "Access Denied ! "
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST' :

        permission_name = request.POST.get('permission_name')
        permission_code_name = request.POST.get('permission_code_name')

        if len(Permission.objects.filter(codename=permission_code_name)) == 0 :
        
            content_type = ContentType.objects.get(app_label='main', model='main')
            permission = Permission.objects.create(codename=permission_code_name, content_type=content_type, name=permission_name)

        else :
            error = "Permission Code Name Must Be Unique. "
            return render(request, 'back/error.html', {'error': error})


    return redirect('permission')



def group_permission(request, name) :

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :

        error = "Access Denied ! "
        return render(request, 'back/error.html', {'error': error})

    group = Group.objects.get(name=name)
    perms = group.permissions.all()

    all_permissions = Permission.objects.all()

    distinct_perms = list(set(all_permissions).difference(set(perms)))


    return render(request, 'back/group_permission.html', {'perms': perms, 'name': name, 'distinct_perms': distinct_perms})



def group_permission_delete(request, name, gname) :

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :

        error = "Access Denied ! "
        return render(request, 'back/error.html', {'error': error})

    group = Group.objects.get(name=gname)
    perms = Permission.objects.get(name=name)

    group.permissions.remove(perms)


    return redirect('group_permission', name=gname)


def group_permission_add(request, name) :

    # login check
    if not request.user.is_authenticated :
        return redirect('mylogin')

    # masteruser check
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" :
            perm = 1

    if perm == 0 :

        error = "Access Denied ! "
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST' :

        permission_name = request.POST.get('permission_name')

        group = Group.objects.get(name=name)

        perm = Permission.objects.get(name=permission_name)

        group.permissions.add(perm)


    return redirect('group_permission', name=name)


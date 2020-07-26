from django.shortcuts import render, redirect, get_object_or_404
from .models import Category

def category_list(request):

    name = Category.objects.all()

    return render(request, 'back/category_list.html', {'name' : name})

def category_add(request):

    if request.method == 'POST' :

        name = request.POST.get('category') 

        if name == "" :
            error = 'Fill all the required details.'
            return render(request, 'back/error.html', {'error': error})

        if len(Category.objects.filter(name=name)) !=0 :
            error = 'Category already exists, try adding different one. '
            return render(request, 'back/error.html', {'error': error})

        obj = Category(name=name)
        obj.save()

        return redirect('category_list')


    return render(request, 'back/category_add.html')

def category_edit(request, pk):

    obj = Category.objects.get(pk=pk)

    if request.method == 'POST':

        category = request.POST.get('category')

        if category == "":
            error = 'Fill all the required details.'
            return render(request, 'back/error.html', {'error': error})

        else :
            obj1 = Category.objects.get(pk=pk)

            obj1.name = category

            obj1.save()
            
            return redirect(category_list)

    return render(request, 'back/category_edit.html', {'obj': obj, 'pk':pk})


def category_delete(request, pk):

    obj = Category.objects.get(pk=pk)
    obj.delete()

    return redirect('category_list')
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Comments, Comments_Reply, Comments_Doodle
from django.core.files.storage import FileSystemStorage
import random

# Create your views here.
def comments_list(request):

    comments = Comments.objects.all()
    commentss = reversed(list(comments))


    doodles = Comments_Doodle.objects.all()
    
    return render(request, 'back/comments_list.html', {'comments': commentss, 'doodles': doodles})


def comments_delete(request, pk):
    try :
        obj = Comments.objects.get(pk=pk)
        obj.delete()

        return redirect('comments_list')

    except :
        error = 'Object Not Found.'
        return render(request, 'back/error.html', {'error': error})



def doodle_add(request) :

    if request.method == 'POST' :

        custome_name = request.POST.get('custome_name')

        try :

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith('image') :

                if myfile.size < 5000000:

                    obj = Comments_Doodle(comments_custom_picname=custome_name, comments_picurl=url, comments_picname=filename) 
                    obj.save()

                    return redirect('comments_list')

                else : 
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    
                    error = 'File size is larger than 5 MB, select smaller file.'
                    return render(request, 'back/error.html', {'error': error})

            
            else : 
                fs = FileSystemStorage()
                fs.delete(filename)
                
                error = 'File selected must be type of Image.'
                return render(request, 'back/error.html', {'error': error})

        except :

            error = 'Fill all the required details.'
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/testing.html', {})



def doodle_list(request) :

    doodles = Comments_Doodle.objects.all()

    return render(request, 'back/comments_doodle_list.html', {'doodles': doodles})

def doodle_delete(request, pk) :

    obj = Comments_Doodle.objects.get(pk=pk)

    fs = FileSystemStorage()
    fs.delete(obj.comments_picname)

    obj.delete()

    return redirect('doodle_list')

def comments_reply_list(request, pk) :

    replies = Comments_Reply.objects.filter(comment_id=pk)

    return render(request, 'back/comments_reply_list.html', {'replies': replies, 'pk':pk})

def comments_reply_delete(request, pk, news_pk) :

    obj = Comments_Reply.objects.get(pk=pk)
    obj.delete()

    return redirect('comments_reply_list', pk=news_pk)
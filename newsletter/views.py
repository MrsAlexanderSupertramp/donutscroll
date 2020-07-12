from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Newsletter
from django.core.files.storage import FileSystemStorage
import random
from django.contrib import messages
from category.models import Category
from news.models import News

def news_letter(request) :

    if request.method == 'POST' :
        try:
            email = request.POST.get('email')
            name = request.POST.get('name')

            if len(Newsletter.objects.filter(email=email)) == 0 :

                obj = Newsletter(email=email, name=name)
                obj.save()

                # For master page i.e. Header, footer & sidebar content
                category  = Category.objects.all()
                news = News.objects.all()
                newshead = []
                for i in category:
                    newss = News.objects.filter(catname = i.name).order_by("pk").reverse()[:5]
                    for j in newss:
                        newshead.append(j)

                newstrend = News.objects.filter(trending=True)


                message = "Voi̇̀la, you have successfully subscribed to our weekly newsletter."

                return render(request, 'front/newsletter_info.html', {'message': message, 'news': news, 'category': category, 'newstrend': newstrend, 'newshead': newshead})

            else :
                try :
                    obj = Newsletter.objects.get(name=name)
                    Name = obj.name
                    Email = obj.email

                    msg = "Hello {0}, its good to see you. Your email  #'{1}' is already under our subscribers family. If you want to change your email then try adding a new one so that you dont miss-out on our latest posts, Cheers.".format(Name, Email)
                    messages.success(request, msg)

                    return redirect('error')
                except : 
                    pass
        except:
            pass


def news_letter_list(request) :

    newsletter = Newsletter.objects.all()

    return render(request, 'back/newsletter_list.html', {'newsletter': newsletter})


def news_letter_delete(request, pk) :
    
    try :
        obj = Newsletter.objects.get(pk=pk)
        obj.delete()
    except:
        pass

    return redirect('news_letter_list')
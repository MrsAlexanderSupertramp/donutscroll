from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import News
from main.models import Main
from category.models import Category
from comments.models import Comments
from main.models import Main, HeadingDropdown, MostViewed, FeaturedHome, MasonryHome, PicturesGallery, ExtraPages
from singular_manager.models import Singular_Manager
from django.core.files.storage import FileSystemStorage
import datetime


def news_list(request):

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    news = News.objects.all()
    category = Category.objects.all()

    return render(request, 'back/news_list.html', {'news': news, 'category': category})


def news_list_by_position_home(request):

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    news = News.objects.all()
    category = Category.objects.all()

    temp = News.objects.raw('SELECT ID, name, identifier_home FROM news_news')

    for i in temp:
        print(i.name)
        print(i.identifier_home)


    return render(request, 'back/news_list_by_position_home.html', {'news': news, 'category': category})


def news_add(request):

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')


    now = datetime.datetime.now()

    year  = now.year
    month = now.month
    day   = now.day

    hour = now.hour
    minute = now.minute

    if len(str(day)) == 1 :
        day = "0" + str(day)

    if len(str(month)) == 1 :
        month = "0" + str(month)

    if len(str(hour)) == 1 :
        hour = "0" + str(hour)

    if len(str(minute)) == 1 :
        minute = "0" + str(minute)

    today = str(year) + "/" + str(month) + "/" + str(day)
    time  = str(hour) + ":" + str(minute)

    category = Category.objects.all()
    singular_manager = Singular_Manager.objects.all()

    if request.method == 'POST':

        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstrend = request.POST.get('newstrend')
        newsintro = request.POST.get('newsintro')
        newsbody = request.POST.get('newsbody')
        newsidentifierHome = request.POST.get('newsidentifierHome')
        


        if newstitle == "" or newscat == "" or newstrend == "" or newsbody == "" or newsintro == "" or newsidentifierHome == "":
            error = 'Fill all the required details.'
            return render(request, 'back/error.html', {'error': error})


        try :    
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)


            if str(myfile.content_type).startswith('image'):

                if myfile.size < 5000000:

                    obj = News(name=newstitle, intro_text=newsintro, identifier_home=newsidentifierHome, body_text=newsbody, date=today, time= time, picname= filename, picurl=url, writer="-", catname=newscat, catid=0, views=0, trending=newstrend) 
                    obj.save()

                    # temp = len(News.objects.filter(catname = newscat))
                    # obj2 = Category.objects.get(name = newscat)
                    # obj2.count = temp

                    # obj2.save()

                    category = Category.objects.all()

                    for i in category :
                        i.count = len(News.objects.filter(catname = i.name))
                        i.save()


                    return redirect('news_list')

                else : 
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    
                    error = 'File size is larger than 5 MB, select smaller file.'
                    return render(request, 'back/error.html', {'error': error})

            else :
                fs = FileSystemStorage()
                fs.delete(filename)

                error = 'File type not supported.'
                return render(request, 'back/error.html', {'error': error})

        except :
            error = 'You can not leave your image field empty.  '
            return render(request, 'back/error.html', {'error': error})    
        
  
    return render(request, 'back/news_add.html', {'category' : category, 'singular_manager': singular_manager})


def news_delete(request, pk):

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')


    obj = News.objects.get(pk=pk)
    news_name = obj.name

    fs = FileSystemStorage()
    fs.delete(obj.picname)

    # all the special Posts by position will be deleted here
    try: 
        obj_heading_dropdown = HeadingDropdown.objects.get(name = news_name)
        obj_heading_dropdown.delete()
    except: 
        pass

    try:
        obj_most_viewed = MostViewed.objects.get(name = news_name)
        obj_most_viewed.delete()
    except: 
        pass

    try :
        obj_featured_home = FeaturedHome.objects.get(name = news_name)
        obj_featured_home.delete()
    except: 
        pass

    try :
        obj_masonry_home = MasonryHome.objects.get(name = news_name)
        obj_masonry_home.delete()
    except: 
        pass

    obj.delete()



    return redirect('news_list')


def news_edit(request, pk):

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    if len(News.objects.filter(pk=pk)) == 0 :
        error = 'News not found. '
        return render(request, 'back/error.html', {'error': error})

    else :

        news = News.objects.get(pk=pk)
        news_name = news.name
        


        if request.method == 'POST':

            newstitle = request.POST.get('newstitle')
            newscat = request.POST.get('newscat')
            newstrend = request.POST.get('newstrend')
            newsintro = request.POST.get('newsintro')
            newsbody = request.POST.get('newsbody')
            newsidentifierHome = request.POST.get('newsidentifierHome')
            

            if newstitle == "" or newscat == ""  or newstrend == "" or newsintro == "" or newsbody == "" or newsidentifierHome == "":
                error = 'Fill all the required details.'
                return render(request, 'back/error.html', {'error': error})


            try :    
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                url = fs.url(filename)

                if str(myfile.content_type).startswith('image'):

                    if myfile.size < 5000000:

                        obj = News.objects.get(pk=pk)

                        fss = FileSystemStorage()
                        fss.delete(obj.picname)

                        obj.name       = newstitle
                        obj.intro_text = newsintro
                        obj.body_text  = newsbody
                        obj.picname    = filename
                        obj.picurl     = url
                        obj.catname    = newscat
                        obj.trending   = newstrend
                        obj.identifier_home = newsidentifierHome

                        # all the special Posts by position will be modified here
                        try: 
                            obj_heading_dropdown = HeadingDropdown.objects.get(name = news_name)
                            obj_heading_dropdown.name = newstitle
                            obj_heading_dropdown.picurl = url
                            obj_heading_dropdown.catname = newscat
                            obj_heading_dropdown.save()
                        except: 
                            pass

                        try:
                            obj_most_viewed = MostViewed.objects.get(name = news_name)
                            obj_most_viewed.name = newstitle
                            obj_most_viewed.picurl = url
                            obj_most_viewed.catname = newscat
                            obj_most_viewed.save()
                        except: 
                            pass

                        try :
                            obj_featured_home = FeaturedHome.objects.get(name = news_name)
                            obj_featured_home.name = newstitle
                            obj_featured_home.picurl = url
                            obj_featured_home.catname = newscat
                            obj_featured_home.intro_text = newsintro
                            obj_featured_home.save()
                        except: 
                            pass

                        try :
                            obj_masonry_home = MasonryHome.objects.get(name = news_name)
                            obj_masonry_home.name = newstitle
                            obj_masonry_home.picurl = url
                            obj_masonry_home.catname = newscat
                            obj_masonry_home.intro_text = newsintro
                            obj_masonry_home.save()
                        except: 
                            pass

                        obj.save()


                        return redirect('news_list')

                    else : 
                        fs = FileSystemStorage()
                        fs.delete(filename)
                        
                        error = 'File size is larger than 5 MB, select smaller file.'
                        return render(request, 'back/error.html', {'error': error})

                else :
                    fs = FileSystemStorage()
                    fs.delete(filename)

                    error = 'File type not supported.'
                    return render(request, 'back/error.html', {'error': error})

            except :

                obj = News.objects.get(pk=pk)


                obj.name       = newstitle
                obj.intro_text = newsintro
                obj.body_text  = newsbody
                obj.catname    = newscat
                obj.trending   = newstrend
                obj.identifier_home = newsidentifierHome

                # all the special Posts by position will be modified here
                try :
                    obj_heading_dropdown = HeadingDropdown.objects.get(name = news_name)
                    obj_heading_dropdown.name = newstitle
                    obj_heading_dropdown.catname = newscat
                    obj_heading_dropdown.save()
                except: 
                    pass

                try :
                    obj_most_viewed = MostViewed.objects.get(name = news_name)
                    obj_most_viewed.name = newstitle
                    obj_most_viewed.catname = newscat
                    obj_most_viewed.save()
                except: 
                    pass

                try :
                    obj_featured_home = FeaturedHome.objects.get(name = news_name)
                    obj_featured_home.name = newstitle
                    obj_featured_home.catname = newscat
                    obj_featured_home.intro_text = newsintro
                    obj_featured_home.save()
                except: 
                    pass

                try : 
                    obj_masonry_home = MasonryHome.objects.get(name = news_name)
                    obj_masonry_home.name = newstitle
                    obj_masonry_home.catname = newscat
                    obj_masonry_home.intro_text = newsintro
                    obj_masonry_home.save()
                except: 
                    pass


                obj.save()

                return redirect('news_list')  

        return render(request, 'back/news_edit.html', {'pk': pk, 'news': news,})
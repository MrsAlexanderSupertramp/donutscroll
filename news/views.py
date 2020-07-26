from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import News
from main.models import Main
from category.models import Category
from comments.models import Comments
from main.models import Main, HeadingDropdown, MostViewed, FeaturedHome, MasonryHome, PicturesGallery, ExtraPages
from django.core.files.storage import FileSystemStorage
import datetime


def news_list(request):

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    news = News.objects.all()
    category = Category.objects.all()

    return render(request, 'back/news_list.html', {'news': news, 'category': category})


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

    if len(str(hour)) == 1 :
        hour = "0" + str(hour)

    if len(str(minute)) == 1 :
        minute = "0" + str(minute)

    # weekday = now.strftime("%A")

    

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(month) + " " + str(day) + ", " + str(year)
    print(today)


    time  = str(hour) + ":" + str(minute)

    category = Category.objects.all()

    if request.method == 'POST':

        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newsintro = request.POST.get('newsintro')
        newsbody = request.POST.get('newsbody')
        newscredit = request.POST.get('newscredit')
        


        if newstitle == "" or newscat == "" or newsbody == "" or newsintro == "" :
            error = 'Fill all the required details.'
            return render(request, 'back/error.html', {'error': error})


        try :    
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith('image'):

                if myfile.size < 5000000:

                    obj = News(name=newstitle, intro_text=newsintro, body_text=newsbody, date=today, time= time, picname= filename, picurl=url, piccredit=newscredit,writer="DonutScroll", catname=newscat) 
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
            fs = FileSystemStorage()
            fs.delete(filename)
            error = 'You can not leave your image field empty.  '
            return render(request, 'back/error.html', {'error': error})    
        
  
    return render(request, 'back/news_add.html', {'category' : category})


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
            newscredit = request.POST.get('newscredit')
            

            if newstitle == "" or newscat == ""  or newstrend == "" or newsintro == "" or newsbody == "" :
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
                        obj.piccredit  = newscredit

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
                obj.piccredit  = newscredit

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

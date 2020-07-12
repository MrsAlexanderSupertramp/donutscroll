from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Main, HeadingDropdown, MostViewed, FeaturedHome, MasonryHome, PicturesGallery, ExtraPages, Trending
from news.models import News
from category.models import Category
from comments.models import Comments
from comments.models import Comments_Reply
from comments.models import Comments_Doodle
from manager.models import Manager
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from itertools import chain
from django.db.models import Q
import datetime
import random
# from ipware import get_client_ip
# from ip2geotools.databases.noncommercial import DbIpCity
import urllib.request
import json
from django.core.files.storage import FileSystemStorage


def home(request):
    
    category  = Category.objects.all()
    news = News.objects.all()


    # newshead = News.objects.raw(
    #     'SELECT * FROM news_news WHERE catname="Fashion" UNION SELECT * FROM news_news WHERE catname="Travel"').reverse()

    newshead = []

    heading_posts = HeadingDropdown.objects.all()
    

    featured_home_general = []

    for i in category :
        featured_home_main = FeaturedHome.objects.filter(catname=i.name)
        for k in featured_home_main:
            temp = News.objects.filter(catname=i.name).order_by('-pk').exclude(name=k.name)[:5]
            for j in temp :
                featured_home_general.append(j)



    most_viewed = MostViewed.objects.all()
    featuredhome = FeaturedHome.objects.all()
    masonryhome = MasonryHome.objects.all()
    pictures_gallery = PicturesGallery.objects.all()
    trending = Trending.objects.all()

    # Temperature
    # ip, is_routable = get_client_ip(request)

    # try :
    #     response = DbIpCity.get(ip, api_key='free')
    #     city = response.city
    # except :
    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(round(json_data['main']['temp'] - 273.15, 1), 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'news': news, 
        'category': category, 
        'trending': trending, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        "featuredhome": featuredhome,
        "featured_home_general": featured_home_general,
        "masonryhome": masonryhome,
        "pictures_gallery": pictures_gallery,
        'temp': temp,
        'city': city,
        'today': today,
    }


    return render(request, 'front/home.html', dictionary)


def news_search(request):

    if request.method == "POST":

        search = request.POST.get('search')

    category  = Category.objects.all()
    trending = Trending.objects.all()
    allnews = News.objects.all()

    newshead = []

    for i in category:
        newss = News.objects.filter(catname = i.name).order_by("pk").reverse()[:5]
        for j in newss:
            newshead.append(j)


    if search :
        newss = News.objects.filter(
            Q(name__contains=search) | Q(body_text__contains=search) | Q(intro_text__contains=search) 
        ).distinct()

    
    paginator = Paginator(newss,9)
    page = request.GET.get('page')
    last = paginator.num_pages
    
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    for i in news:
        print(i.name)

    for i in newss:
        print(i.name)

    # Temperature
    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'news': news, 
        'category': category, 
        'newshead': newshead,
        'trending': trending,
        'last': last,
        'temp': temp,
        'city': city,
        'today': today,
    }

    for i in News.objects.all():
        print(i.name)



    return render(request, 'front/search.html', dictionary)
    

def news_detail(request, name, cat):

    category  = Category.objects.all()
    news = News.objects.all()
    news_details = News.objects.get(name=name)
    comments = Comments.objects.filter(news_id=news_details.pk)
    trending = Trending.objects.all()
    heading_posts = HeadingDropdown.objects.all()
    most_viewed = MostViewed.objects.all()
    related_posts = News.objects.filter(catname=news_details.catname).order_by('-pk')[: 7]
    pictures_gallery = PicturesGallery.objects.all()


    replies = []

    for c in comments :
        comments_reply = Comments_Reply.objects.filter(comment_id=c.pk)
        for d in comments_reply :
            replies.append(d)

    comments_count = comments.count() + len(replies)

    newshead = []

    for i in category:
        newss = News.objects.filter(catname = i.name).order_by("pk").reverse()[:5]
        for j in newss:
            newshead.append(j)

    comments_count = comments.count() + len(replies)


    # Temperature
    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()   
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'news': news, 
        'category': category, 
        'trending': trending, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        'news_details': news_details, 
        "pictures_gallery": pictures_gallery,
        'comments': comments, 
        'comments_reply': replies, 
        'comments_count': comments_count, 
        'pk': news_details.pk,
        'temp': temp,
        'city': city,
        'today': today,
        'related_posts': related_posts,
    }

    return render(request, 'front/news_detail.html', dictionary)


def comments_add(request):

    if request.method == 'POST' :

        CommentBody = request.POST.get('CommentBody')
        CommentName = request.POST.get('CommentName')
        CommentEmail = request.POST.get('CommentEmail')
        news_pk = request.POST.get('news_pk')


        # Date for Comments
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        weekday = now.strftime("%A")

        month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        for i in range(11) :
            if month == i+1 :
                month = month_list[i]
                break
        
        today = str(weekday) + " , " + str(month) + " " + str(day) + "," + str(year)


        if CommentBody != "" and CommentEmail != "" and CommentName != "" :

            if 'container' in request.session :

                comment_session_dict = request.session.get('container')

            else :

                doodles = Comments_Doodle.objects.all()
                random_doodle = random.choice(doodles)
                random_doodle_picurl = random_doodle.comments_picurl

                session_dict = {
                    "name" : CommentName,
                    "email" : CommentEmail,
                    "url" : random_doodle_picurl
                }

                request.session['container'] = session_dict

                comment_session_dict = request.session.get('container')


            obj = Comments(body=CommentBody, name=comment_session_dict['name'], email=comment_session_dict['email'], picurl=comment_session_dict['url'], date=today, news_id=news_pk)
            obj.save()

            return redirect('news_detail', pk=news_pk)
             
        else :
            
            error =  "Please Enter All The Details"
            return render(request, 'front/error.html', {'error': error})


def comments_reply_add(request):

    if request.method == 'POST' :

        CommentReplyBody = request.POST.get('CommentReplyBody')
        CommentReplyName = request.POST.get('CommentReplyName')
        CommentReplyEmail = request.POST.get('CommentReplyEmail')
        news_pk = request.POST.get('news_pk')
        comments_pk = request.POST.get('comments_pk')

        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        weekday = now.strftime("%A")

        month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        for i in range(11) :
            if month == i+1 :
                month = month_list[i]
                break
        
        today = str(weekday) + " , " + str(month) + " " + str(day) + "," + str(year)


        if CommentReplyBody != "" and CommentReplyEmail != "" and CommentReplyName != "" :

            if 'container' in request.session :

                comment_session_dict = request.session.get('container')

    

            else :

                doodles = Comments_Doodle.objects.all()
                random_doodle = random.choice(doodles)
                random_doodle_picurl = random_doodle.comments_picurl

                session_dict = {
                    "name" : CommentReplyName,
                    "email" : CommentReplyEmail,
                    "url" : random_doodle_picurl
                }

                request.session['container'] = session_dict

                comment_session_dict = request.session.get('container')

            Robj = Comments_Reply(body=CommentReplyBody, name=comment_session_dict['name'], email=comment_session_dict['email'], picurl=comment_session_dict['url'] ,date=today, news_id=news_pk, comment_id=comments_pk)
            Robj.save()

            Cobj = Comments.objects.get(pk=comments_pk)
            Cobj.count += 1
            Cobj.save()

            return redirect('news_detail', pk=news_pk)
             
        else :
            
            error =  "Please Enter All The Details"
            return render(request, 'front/error.html', {'error': error})


def news_section(request, name):
    category  = Category.objects.all()
    trending = Trending.objects.all()
    most_viewed = MostViewed.objects.all()
    pictures_gallery = PicturesGallery.objects.all()

    heading_posts = HeadingDropdown.objects.all()


    newss = News.objects.filter(catname=name).order_by("-pk")
    page = request.GET.get('page')
    paginator = Paginator(newss,12)
    last = paginator.num_pages
    
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)


        # Temperature
    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'news': news, 
        'category': category, 
        'trending': trending, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        "pictures_gallery": pictures_gallery,
        'last': last,
        'temp': temp,
        'city': city,
        'today': today,
    }

    return render(request, 'front/news_section.html', dictionary)


def panel(request):

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')


    return render(request, 'back/panel.html')


def mylogin(request):
    print("------------------------")

    if request.method == 'POST' :

        username = request.POST.get('username')
        password = request.POST.get('password')

        if username != "" and password != "" :

            user = authenticate(username=username, password=password)

            if user != None :

                login(request, user)
                
                return redirect('panel')

            elif User.objects.filter(username = username).exists() :

                msg = "Incorrect Password, Try forgot password if you are not able to remember your password ! "
                messages.success(request, msg)

                return render(request, 'back/mylogin.html')

            else :

                msg = "No user found, Try registering if you havent registered yet ! "
                messages.success(request, msg)

                return render(request, 'back/mylogin.html')


    return render(request, 'back/mylogin.html')


def myregister(request):

    if request.method == 'POST' :

        name = request.POST.get('name')
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password :

            msg = "Passwords don't match ! "
            messages.success(request, msg)

            return render(request, 'back/myregister.html')

        if len(password) < 8 :

            msg = "Password needs to be of at least 8 characters ! "
            messages.success(request, msg)

            return render(request, 'back/myregister.html')

        
        # c1, c2, c3, c4 = 0, 0, 0, 0

        # for i in password :

        #     if i > "0" and i < "9" :
        #         c1 = 1
        #     if i > "A" and i < "Z" :
        #         c1 = 1
        #     if i > "a" and i < "z" :
        #         c1 = 1
        #     if i > "!" and i < "(" :
        #         c1 = 1

        # if c1 == 0 or c2 == 0 or c3 == 0 or c4 == 0 :
        #     msg = "Password must contain at least 1 Uppercase, 1 Lowercase, 1 number and 1 Special character !"
        #     messages.success(request, msg)

        #     return render(request, 'back/myregister.html')



        if name != "" and username != "" and password != "" and password !="" and confirm_password != "" :

            if len(User.objects.filter(username=username)) == 0 and len(User.objects.filter(email=email)) == 0 :

                user = User.objects.create_user(username=username, email=email, password=password)
                obj = Manager(name=name, username=username, email=email)
                
                obj.save()

                return render(request, 'back/mylogin.html')

            else :

                msg = "User is taken, try putting different Username or Email ! "
                messages.success(request, msg)

                return render(request, 'back/myregister.html')
        else :

            msg = "Enter all the details ! "
            messages.success(request, msg)

            return render(request, 'back/myregister.html')



    return render(request, 'back/myregister.html')


def mylogout(request):

    logout(request)

    return redirect('mylogin')


def error(request) :

    category  = Category.objects.all()

    news = News.objects.all()

    newshead = []

    for i in category:
        newss = News.objects.filter(catname = i.name).order_by("pk").reverse()[:5]
        for j in newss:
            newshead.append(j)

    newstrend = News.objects.filter(trending=True)

    # Temperature
    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'news': news, 
        'category': category, 
        'newstrend': newstrend, 
        'newshead': newshead,
        'temp': temp,
        'city': city,
        'today': today,
    }
    

    return render(request, 'front_extra/404.html', dictionary)


def post_by_position(request) :

    category = Category.objects.all()
    allnews = News.objects.all().order_by('-pk')
    dropdown = HeadingDropdown.objects.all()
    mostviewed = MostViewed.objects.all()
    featuredhome = FeaturedHome.objects.all()
    masonryhome = MasonryHome.objects.all()

    dictionary = {
        "category" : category,
        "allnews" : allnews,
        "dropdown" : dropdown,
        "mostviewed" : mostviewed,
        "featuredhome": featuredhome,
        "masonryhome": masonryhome,

    }

    return render(request, 'back/post_by_position.html', dictionary)


def heading_dropdown_add(request) :

    if request.method == 'POST' :

        post_name = request.POST.get('item')
        news = News.objects.get(name=post_name)

        obj = HeadingDropdown(name=news.name, catname=news.catname, picurl=news.picurl)
        obj.save()

        return redirect('post_by_position')


def heading_dropdown_delete(request, pk) :

    obj = HeadingDropdown.objects.get(pk=pk)
    obj.delete()

    return redirect('post_by_position')


def most_viewed_add(request) :

    if request.method == 'POST' :

        post_name = request.POST.get('item')
        news = News.objects.get(name=post_name)

        obj = MostViewed(name=news.name, catname=news.catname, picurl=news.picurl, date=news.date)
        obj.save()

        return redirect('post_by_position')


def most_viewed_delete(request, pk) :

    obj = MostViewed.objects.get(pk=pk)
    obj.delete()

    return redirect('post_by_position')


def featured_home_add(request) :

    if request.method == 'POST' :

        post_name = request.POST.get('item')
        position = request.POST.get('position')
        news = News.objects.get(name=post_name)

        obj = FeaturedHome(name=news.name, catname=news.catname, picurl=news.picurl, position=position, intro_text=news.intro_text, date=news.date)
        obj.save()

        return redirect('post_by_position')


def featured_home_delete(request, pk) :

    obj = FeaturedHome.objects.get(pk=pk)
    obj.delete()

    return redirect('post_by_position')


def masonry_home_add(request) :

    if request.method == 'POST' :

        post_name = request.POST.get('item')
        position = request.POST.get('position')
        news = News.objects.get(name=post_name)

        obj = MasonryHome(name=news.name, catname=news.catname, picurl=news.picurl, position=position, intro_text=news.intro_text, date=news.date)
        obj.save()

        return redirect('post_by_position')


def masonry_home_delete(request, pk) :

    obj = MasonryHome.objects.get(pk=pk)
    obj.delete()

    return redirect('post_by_position')



def trending_list(request):

    if request.method == 'POST' :

        name = request.POST.get('name')

        obj = Trending(name=name)
        obj.save()


    allnews = News.objects.all().order_by("-pk")
    trending = Trending.objects.all()

    dictionary = {
        "allnews": allnews,
        "trending": trending,
    }

    return render(request, 'back/trending_list.html', dictionary)


def trending_remove(request, pk) :

    obj = Trending.objects.get(pk=pk)
    obj.delete()

    return redirect('trending_list')


def pictures_gallery(request):

    pictures_gallery = PicturesGallery.objects.all()

    return render(request, 'back/pictures_gallery.html', {'pictures_gallery': pictures_gallery})


def pictures_gallery_add(request):

    if request.method == 'POST' :

        try :
            given_name = request.POST.get('given_name')
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            picname = fs.save(myfile.name, myfile)
            picurl = fs.url(picname)

            if str(myfile.content_type).startswith('image'):

                obj = PicturesGallery(givenname=given_name, picname=picname, picurl=picurl)
                obj.save()

            else : 
                fs = FileSystemStorage()
                fs.delete(picname)
                
                error = 'File type not supported..'
                return render(request, 'back/error.html', {'error': error})

        except:
            error = 'You can not leave your any field empty.  '
            return render(request, 'back/error.html', {'error': error})    

    return redirect('pictures_gallery')


def pictures_gallery_delete(request, pk):

    try : 
        obj = PicturesGallery.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(obj.picname)
        obj.delete()

    except:
        error = 'You can not leave your any field empty.  '
        return render(request, 'back/error.html', {'error': error})   

    return redirect('pictures_gallery')


def about(request):


    category  = Category.objects.all()

    newshead = []

    heading_posts = HeadingDropdown.objects.all()
    

    most_viewed = MostViewed.objects.all()
    pictures_gallery = PicturesGallery.objects.all()
    content = ExtraPages.objects.get(pagename="About")
    trending = Trending.objects.all() 

    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'category': category, 
        'trending': trending, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        'content': content,
        "pictures_gallery": pictures_gallery,
        'temp': temp,
        'city': city,
        'today': today,
    }

    print(content)

    return render(request, 'front_extra/contact.html', dictionary)


def contact(request):


    category  = Category.objects.all()

    newshead = []

    heading_posts = HeadingDropdown.objects.all()
    

    most_viewed = MostViewed.objects.all()
    pictures_gallery = PicturesGallery.objects.all()
    content = ExtraPages.objects.get(pagename="Contact Us")
    trending = Trending.objects.all()

    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'category': category, 
        'trending': trending, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        "pictures_gallery": pictures_gallery,
        "content": content,
        'temp': temp,
        'city': city,
        'today': today,
    }


    return render(request, 'front_extra/contact.html', dictionary)


def copyright(request):


    category  = Category.objects.all()

    newshead = []

    heading_posts = HeadingDropdown.objects.all()
    

    most_viewed = MostViewed.objects.all()
    pictures_gallery = PicturesGallery.objects.all()

    newstrend = News.objects.filter(trending=True)

    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'category': category, 
        'newstrend': newstrend, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        "pictures_gallery": pictures_gallery,
        'temp': temp,
        'city': city,
        'today': today,
    }

    return render(request, 'front/copyright.html', dictionary)


def privacy_policy(request):


    category  = Category.objects.all()

    newshead = []

    heading_posts = HeadingDropdown.objects.all()
    

    most_viewed = MostViewed.objects.all()
    pictures_gallery = PicturesGallery.objects.all()

    newstrend = News.objects.filter(trending=True)

    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'category': category, 
        'newstrend': newstrend, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        "pictures_gallery": pictures_gallery,
        'temp': temp,
        'city': city,
        'today': today,
    }

    return render(request, 'front/privacy_policy.html', dictionary)


def cookie_policy(request):


    category  = Category.objects.all()

    newshead = []

    heading_posts = HeadingDropdown.objects.all()
    

    most_viewed = MostViewed.objects.all()
    pictures_gallery = PicturesGallery.objects.all()

    newstrend = News.objects.filter(trending=True)

    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'category': category, 
        'newstrend': newstrend, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        "pictures_gallery": pictures_gallery,
        'temp': temp,
        'city': city,
        'today': today,
    }

    return render(request, 'front/cookie_policy.html', dictionary)


def terms_of_service(request):


    category  = Category.objects.all()

    newshead = []

    heading_posts = HeadingDropdown.objects.all()
    

    most_viewed = MostViewed.objects.all()
    pictures_gallery = PicturesGallery.objects.all()

    newstrend = News.objects.filter(trending=True)

    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'category': category, 
        'newstrend': newstrend, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        "pictures_gallery": pictures_gallery,
        'temp': temp,
        'city': city,
        'today': today,
    }

    return render(request, 'front/terms_of_service.html', dictionary)


def diversity_and_corrections_policy(request):


    category  = Category.objects.all()

    newshead = []

    heading_posts = HeadingDropdown.objects.all()
    

    most_viewed = MostViewed.objects.all()
    pictures_gallery = PicturesGallery.objects.all()

    newstrend = News.objects.filter(trending=True)

    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'category': category, 
        'newstrend': newstrend, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        "pictures_gallery": pictures_gallery,
        'temp': temp,
        'city': city,
        'today': today,
    }

    return render(request, 'front/diversity_and_corrections_policy.html', dictionary)


def ownership(request):


    category  = Category.objects.all()

    newshead = []

    heading_posts = HeadingDropdown.objects.all()
    

    most_viewed = MostViewed.objects.all()
    pictures_gallery = PicturesGallery.objects.all()

    newstrend = News.objects.filter(trending=True)

    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'category': category, 
        'newstrend': newstrend, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        "pictures_gallery": pictures_gallery,
        'temp': temp,
        'city': city,
        'today': today,
    }

    return render(request, 'front/ownership.html', dictionary)


def ethics_policy(request):


    category  = Category.objects.all()

    newshead = []

    heading_posts = HeadingDropdown.objects.all()
    

    most_viewed = MostViewed.objects.all()
    pictures_gallery = PicturesGallery.objects.all()

    newstrend = News.objects.filter(trending=True)

    city = 'Delhi'

    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=3901fffe544e24790a601a25c1182976&q="
    url = api_address + city

    source = urllib.request.urlopen(url).read()

    json_data = json.loads(source)
    temp = round(json_data['main']['temp'] - 273.15, 1)

    # Datetime
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    weekday = now.strftime("%A")

    

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(11) :
        if month == i+1 :
            month = month_list[i]
            break
    
    today = str(weekday) + " , " + str(month) + " " + str(day)

    dictionary = {
        'category': category, 
        'newstrend': newstrend, 
        'heading_posts': heading_posts,
        'most_viewed': most_viewed,
        "pictures_gallery": pictures_gallery,
        'temp': temp,
        'city': city,
        'today': today,
    }

    return render(request, 'front/ethics_policy.html', dictionary)

    
def extra_pages(request) :

    extrapages = ExtraPages.objects.all()

    dictionary = {
        'extrapages': extrapages
    }

    return render(request, 'back/extra_pages.html', dictionary)


def extra_pages_add(request) :

    if request.method == 'POST' :

        page_name = request.POST.get('page_name')

        obj = ExtraPages(pagename=page_name)
        obj.save()

    return redirect('extra_pages')


def extra_pages_delete(request, pk) :

    try :
        obj = ExtraPages.objects.get(pk=pk)
        obj.delete()

        return redirect('extra_pages')
    
    except:
        error =  "Object not found !"
        return render(request, 'front/error.html', {'error': error})


def extra_pages_content(request, pk) :

    if request.method == 'POST' :

        try :
            page_content = request.POST.get('body')

            obj = ExtraPages.objects.get(pk=pk)
            obj.pagecontent = page_content

            obj.save()

            return redirect('extra_pages')
        
        except:
            error =  "Object not found !"
            return render(request, 'back/error.html', {'error': error})



    try :
        extrapages = ExtraPages.objects.get(pk=pk)

        dictionary = {
            'extrapages': extrapages,
            'pk': pk,
        }

        return render(request, 'back/extra_pages_content.html', dictionary)
    
    except:
        error =  "Object not found !"
        return render(request, 'back/error.html', {'error': error})








from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from sympy import product
from .models import Advertisement, comment, crop, userProfile,blog,chat,product
# Create your views here.

def homepage(request):
    blogs = blog.objects.all().order_by("-date")
    try:
        profile = userProfile.objects.filter(user = request.user).first()
    except:
        pass
    if request.user.is_authenticated:
        profile = userProfile.objects.filter(user = request.user).first()

    else:
        profile = ''

    
    if profile:
        cht_faculty = User.objects.all()
    else:
        chat_users = userProfile.objects.filter(is_farmer = True)
        cht_faculty = []
        for c in chat_users:
            cht_faculty.append(c.user)
        
    c_u = []
    u_p = {}

    for us in cht_faculty:  
        u_p = {}
        msg = ""
        time = ""
        try:
            cht = chat.objects.filter(chat_between = request.user.username+","+us.username).order_by("-time").first()
                    
            if cht == None:
                cht = chat.objects.filter(chat_between = us.username+","+request.user.username).order_by("-time").first()
                msg = cht.message 
                time = cht.time
            else:
                msg = cht.message
                time = cht.time
                        
            if cht == None:
                msg = "send a new message"
                time = "0:00"
        except:
            msg = "send a new message"
        
        pf = userProfile.objects.filter(user = us).first()
        try:
            u_p["username"] = pf.user.username 
            u_p["image"] = pf.image.url 
            u_p["message"] = msg
            u_p["time"] = time    
            c_u.append(u_p)
        except:
            pass


    return render(request,'index.html',context = {'profile':profile,"blogs":blogs,"all_users_list":c_u})


message = 0
reg_error = 0


def checkSignup(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    
    u = User.objects.filter(username = username).first()
    
    if u == None:
        message = 0
    else:
        message = 1
    
    return JsonResponse({"message":message})

def register(request):
    if request.method == 'POST':
        user = User.objects.create(username = request.POST.get('username'),email=request.POST.get('email'))
        user.set_password(request.POST.get('password'))
        user.save()

        # user = User.objects.filter(username=request.POST.get('firstname')).first()
        # if str(request.FILES.get('profilePic')) == "None":
        #     profile = userProfile.objects.create(user=user)
        #     profile.save()
        # else:
        #     profile = userProfile.objects.create(user=user,image=request.FILES.get('profilePic'))
        #     profile.save()

    return HttpResponseRedirect(reverse('homepage'))


def checkLogin(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username = username,password = password)
    if user:
        print(username)
        return JsonResponse({"message":0})
            
    else:
        print("No user found")
        return JsonResponse({"message":1})
        

def user_login(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username,password = password)
        if user:

            if user.is_active:
                login(request, user)
                print("login success!!!")
                return HttpResponseRedirect(reverse('homepage'))
        else:
            
            print("No such user")


    return HttpResponseRedirect(reverse('homepage'))
    
@login_required
def user_logout(request):

    logout(request)


    return HttpResponseRedirect(reverse('homepage'))

import pickle 
from sklearn.preprocessing import MinMaxScaler
def cropPrediction(request):
    crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
    
    loaded_model = pickle.load(open("models/naive.sav", 'rb'))
    values = [float(request.POST.get("nitrogen")),float(request.POST.get("phosphorous")),float(request.POST.get("pottassium")),float(request.POST.get("temperature")),float(request.POST.get("humidity")),float(request.POST.get("ph")),float(request.POST.get("rainfall"))]
    m = max(values)
    print(m)
    values = [float(request.POST.get("nitrogen"))/m,float(request.POST.get("phosphorous"))/m,float(request.POST.get("pottassium"))/m,float(request.POST.get("temperature"))/m,float(request.POST.get("humidity"))/m,float(request.POST.get("ph"))/m,float(request.POST.get("rainfall"))/m]
    print(values)
    # values = scaler.fit([values])
    pred = loaded_model.predict([values])
    print(crops[pred[0]])
    try:
        desc = crop.objects.filter(crop = crops[pred[0]]).first()
        desc = desc.description
    except:
        desc = ""
    return JsonResponse({"result":[crops[pred[0]]],"description":desc})


def sendMsg(request):

    to_u = User.objects.filter(username = request.POST.get('to_user')).first()
    is_cyberbullying_comment = 0
    c1 = chat.objects.filter(Q(from_u = request.user) & Q(to_u = to_u)).first()
    if c1 == None:
        c1 = chat.objects.filter(Q(from_u = to_u) & Q(to_u = request.user)).first()
    
    if c1 == None:
        between = request.user.username +  ","+to_u.username
    else:
        between = c1.chat_between 
 
    chatUser = chat.objects.create(from_u = request.user,to_u = to_u,message = request.POST.get("message"),sent_by = request.user,chat_between =between)
    chatUser.save()

    return JsonResponse({"res":"success"})


def chatsDisplay(request):
    u = User.objects.filter(username = request.POST.get('username')).first()
    print("************",request.POST.get('username'))
    c1 = chat.objects.filter(Q(from_u = request.user) & Q(to_u = u)).first()
    if c1 == None:
        c1 = chat.objects.filter(Q(from_u = u) & Q(to_u = request.user)).first()
    
    if c1 == None:
        between = ""
    else:
        between = c1.chat_between 

    chats = chat.objects.filter(chat_between = between)
    # print("----------",chats)
    
        
    c_f = []
    c = {}
    for cht in chats:
        c = {}
        c["to_user"] = cht.to_u.username
        c["from_u"] = cht.from_u.username
        c["message"] = cht.message 
        c["sent_by"] = cht.sent_by.username
        # print(c)
        c_f.append(c)
        
    # print(c_f)    
    return JsonResponse({"chats":c_f})


def services(request):
    return render(request,'services.html')

def blogs(request,pk):
    blg = blog.objects.filter(pk = pk).first()
    comments = comment.objects.filter(post = blg)
    print("-------------",comments)
    profile = userProfile.objects.filter(user = request.user).first()
    return render(request,'blog.html',{"blog":blg,"comments":comments,"profile":profile})


def comments(request):
    blg = blog.objects.filter(pk = request.POST.get('pk')).first()
    user = User.objects.filter(username = request.user.username).first()
    cm = comment.objects.create(comment = request.POST.get('comment'),post = blg,user = user)
    cm.save()
    return HttpResponseRedirect(reverse('homepage'))


def createPost(request):
    
    try:
        blg =blog.objects.create(title = request.POST.get('title'),description = request.POST.get('title'),image = request.FILES['image'],username = request.user.username)
        blg.save()
    except:
        blg =blog.objects.create(title = request.POST.get('title'),description = request.POST.get('title'),username = request.user.username)
        blg.save()
    
    return HttpResponseRedirect(reverse('homepage'))


def createProduct(request):
    
    try:
        user = User.objects.filter(username = request.user.username).first()
        prod = product.objects.create(name = request.POST.get('name'),price = request.POST.get('price'),image = request.FILES['image'],contact = request.POST.get('contact'),user = user)
        prod.save()
    except:
        user = User.objects.filter(username = request.user.username).first()
        prod =product.objects.create(name = request.POST.get('name'),price = request.POST.get('price'),contact = request.POST.get('contact'),user = user,image = request.FILES['image'])
        prod.save()
    
    return HttpResponseRedirect(reverse('homepage'))


def products(request):
    prod = product.objects.all()
    profile = userProfile.objects.filter(user = request.user).first()
    return render(request,'products.html',{"products":prod,"profile":profile})


def ads(request):
    ads = Advertisement.objects.all()
    profile = userProfile.objects.filter(user = request.user).first()
    return render(request,'advertisement.html',{"advertisements":ads,"profile":profile})
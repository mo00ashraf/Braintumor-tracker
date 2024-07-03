from django.shortcuts import render
from django.shortcuts import render , redirect
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import modelformset_factory
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import *
from django.core.files import File
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage, get_connection
from django.contrib import messages
import re
from .form import ImageForm 
from .form import UserProfileForm
import os


def home(request):
    user_img = user_image.objects.filter(user_id=request.user.id).last()
    is_authenticated = request.user.is_authenticated
    return render(request, 'home.html', {'user_img': user_img, 'is_authenticated': is_authenticated})






import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def sign_up(request):
    if request.method == 'POST':
        fn = request.POST.get('firstName')
        ls = request.POST.get('lastName')
        un = request.POST.get('username')
        pa = request.POST.get('Age')
        g = request.POST.get('sex')
        em = request.POST.get('email')
        pwd = request.POST.get('password')


        print(f'First Name: {fn}')
        print(f'Last Name: {ls}')
        print(f'Username: {un}')
        print(f'Age: {pa}')
        print(f'Sex: {g}')
        print(f'Email: {em}')
        print(f'Password: {pwd}')

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        reg = r'\b[A-Za-z0-9._%+-].[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\.[A-Z|a-z]{2,7}\.[A-Z|a-z]{2,7}\b'

        if re.fullmatch(regex, em) or re.fullmatch(reg, em):
            # Check if username or email already exists
            if User.objects.filter(username=un).exists() or User.objects.filter(email=em).exists():
                messages.error(request, "Username or email already exists.")
            else:
                new_user = User.objects.create_user(un, em, pwd, first_name=fn, last_name=ls)
                return redirect('login')
        else:
            messages.error(request, "Invalid email.")
    
    return render(request, 'sign_up.html', {'messages': messages.get_messages(request)})



from django.contrib import messages
from django.contrib.auth import authenticate, login

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password invalid")
    return render(request, 'login.html', {'messages': messages.get_messages(request)})



@login_required(login_url='/login')
def Detection(request):
    if request.method == 'POST':
        newdoc = Image(image= request.FILES.get('image'),image_save= request.FILES.get('image'))
        newdoc.save()
        # form = ImageForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        return redirect('confirmationD')  # Replace 'image_list' with the URL name of the page you want to redirect to after successful image upload
    else:
        form = ImageForm()

    is_authenticated = request.user.is_authenticated
    return render(request, 'Detection.html', {'form': form , 'is_authenticated': is_authenticated}) 



@login_required(login_url='/login')  
def confirm(request):
    if request.method == 'POST':
        os.system('cmd /c "docker run  -v  D:\FinalProject\media:/MyProjectFiles/in  -v D:\o:/MyProjectFiles/out brain-detection"')
        file_to_save = open('D:\o/output.txt', 'r').read()
        new_entry = Result(content=file_to_save)
        new_entry.save()
        hotel = Image.objects.last()
        image_url = hotel.image_save.url
        user_id = request.user.id
        result=file_to_save
        new = process_image(user_id=user_id,url_img=image_url,result=result)
        new.save()
        hotel = Image.objects.last()
        image_url = hotel.image_save.url
        user_id = request.user.id
        subject = 'Brain Tumor Detection Result'
        message = f'Hi {request.user.first_name} {request.user.last_name} ,  We here for helping you and to be better. We show and explain to you in this result that you have {new.result} , Thanks you  '
        v=request.user.email
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [v, ]

        send_mail( subject, message, email_from, recipient_list ,fail_silently=False )
        return redirect('DetectionL')

    is_authenticated = request.user.is_authenticated 
    return render(request, 'confirmationD.html' ,{'is_authenticated': is_authenticated})
   



@login_required(login_url='/login')
def DetectionL(request):

    is_authenticated = request.user.is_authenticated 
    return render(request, 'DetectionL.html',{'is_authenticated': is_authenticated})





from django.contrib import messages

from django.contrib import messages

@login_required(login_url='/login')
def Segmentation(request):
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        folder_name = 'BraTS20_Training_001'  # Specify the desired folder name here

        if len(files) == 4:
            image_model = Files()
            image_model.save_images(files, folder_name)
            return redirect('confirmationS')
        else:
            messages.error(request, 'Please choose four images for segmentation.')

    is_authenticated = request.user.is_authenticated 
    return render(request, 'Segmentation.html', {'is_authenticated': is_authenticated})

    

@login_required(login_url='/login')
def confirmaion(request):
    if request.method == 'POST':
        os.system('cmd /c "docker run  -v  D:\FinalProject\media:/MyProjectFiles/in  -v D:\o:/MyProjectFiles/out seegm"')
        image_path = 'D:\o/fig.jpg'  # Specify the path to your image here
        with open(image_path, 'rb') as f:
            image_file = File(f)
            new_entry = ResultS()
            new_entry.content.save('fig.jpg', image_file)
            user_id = request.user.id
            result = new_entry.content.name  # Get the path of the saved image
            new = process_Seg(user_id=user_id, result=result)
            new.save()
            subject = 'Brain Tumor Segmentation Result'
        message = f'Hi {request.user.first_name} {request.user.last_name}, We here for helping you and to be better. We show and explain to you in this image the areas of evidence for the possibility of cancer in these areas. Therefore, you can quickly follow up and solve the problem at its inception.Green color refer to edema region , bink color refer to enhancing region , and blue color refer to core region.If there is no color , this means that there is no tumor.'

        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [request.user.email],
        )

        # Attach the image to the email
        email.attach_file(new_entry.content.path)

        # Send the email
        email.send()
            
        return redirect('SegmentationL')

    is_authenticated = request.user.is_authenticated 
    return render(request, 'confirmationS.html',{'is_authenticated': is_authenticated})


    


@login_required(login_url='/login')
def SegmentationL(request):
    is_authenticated = request.user.is_authenticated 
    return render(request, 'SegmentationL.html',{'is_authenticated': is_authenticated})

def AboutUs(request):
    is_authenticated = request.user.is_authenticated 
    return render(request, 'AboutUs.html',{'is_authenticated': is_authenticated})




@login_required(login_url='/login')
def HistoryD(request):
    entry = process_image.objects.filter(user_id=request.user.id).order_by('-id')
    images= process_image.objects.all()
    last = images.last()
    count = entry.count
    user_img = user_image.objects.filter(user_id=request.user.id).last()

    if request.method=='POST':
        newdoc = user_image(user_id =request.user.id, image= request.FILES.get('image'))
        newdoc.save()
        return redirect('HistoryD')
    return render(request,'HistoryD.html',{'images':images , 'entry':entry ,'last':last,'count':count,'user_img':user_img})



@login_required
def Logoutuser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login')
def notification(request):
    return render(request, 'notification.html')




@login_required(login_url='/login')
def edit_profile(request):
    user = request.user
    try:
        user_profile = user.userprofile
    except UserProfile.DoesNotExist:
        # Create a UserProfile object for the user if it doesn't exist
        user_profile = UserProfile(user=user)
        user_profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.save()
            form.save()
            return redirect('notification')  # Replace 'notification' with the desired URL name for the notification page
    else:
        form = UserProfileForm(instance=user_profile, initial={'email': user.email})

    return render(request, 'EditProfile.html', {'form': form})




def HistorySeg(request):
    user_id = request.user.id
    entry = process_Seg.objects.filter(user_id=user_id).order_by('-id')
    images = process_Seg.objects.all()
    last = images.last()
    count = entry.count()
    user_img = user_image.objects.filter(user_id=user_id).last()

    if request.method == 'POST':
        newdoc = user_image(user_id=user_id, image=request.FILES.get('images'))
        newdoc.save()
        return redirect('HistorySeg')

    image_filenames = [os.path.basename(image.result) for image in images]  # Get image filenames without path

    return render(request, 'HistorySeg.html', {'images': images, 'entry': entry, 'last': last, 'count': count, 'user_img': user_img, 'image_filenames': image_filenames})

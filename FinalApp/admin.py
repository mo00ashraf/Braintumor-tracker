from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Image , Result , Files , ResultS,process_image,user_image ,process_Seg,UserProfile
from .form import ImageForm ,UserProfileForm

admin.site.register(Image)
admin.site.register(Result)
admin.site.register(Files)
admin.site.register(ResultS)
admin.site.register(process_image)
admin.site.register(user_image)
admin.site.register(process_Seg)
admin.site.register(UserProfile)

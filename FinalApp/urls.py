from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.Login, name='login'),
    path('Detection/', views.Detection, name='Detection'),
    path('Segmentation/', views.Segmentation, name='Segmentation'),
    path('Confirmation/', views.confirm, name='confirmationD'),
    path('DetectionL/', views.DetectionL, name='DetectionL'),
    path('SegmentationL/', views.SegmentationL, name='SegmentationL'),
    path('ConfirmationS/', views.confirmaion, name='confirmationS'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('HistoryD/', views.HistoryD, name='HistoryD'),
    path('logout/',views.Logoutuser,name='logout'),
    path('notification/',views.notification,name='notification'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('HistorySeg/', views.HistorySeg, name='HistorySeg'),
]
from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.
import datetime
from django.contrib.auth.models import User
from django.conf import settings
import shutil


class RenameStorag(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if self.exists('image.jpg'):
            self.delete('image.jpg')
        return super(RenameStorag, self).save('image.jpg', content, max_length=max_length)
    
class RenameStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if self.exists('BraTS20_Validation_001_flair.nii'):
            self.delete('BraTS20_Validation_001_flair.nii')
        return super(RenameStorage, self).save('BraTS20_Validation_001_flair.nii', content, max_length=max_length)

class RenameStorage1(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if self.exists('BraTS20_Validation_001_t1.nii'):
            self.delete('BraTS20_Validation_001_t1.nii')
        return super(RenameStorage1, self).save('BraTS20_Validation_001_t1.nii', content, max_length=max_length)
    
class RenameStorage2(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if self.exists('BraTS20_Validation_001_t1ce.nii'):
            self.delete('BraTS20_Validation_001_t1ce.nii')
        return super(RenameStorage2, self).save('BraTS20_Validation_001_t1ce.nii', content, max_length=max_length)
    
class RenameStorage3(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if self.exists('BraTS20_Validation_001_t2.nii'):
            self.delete('BraTS20_Validation_001_t2.nii')
        return super(RenameStorage3, self).save('BraTS20_Validation_001_t2.nii', content, max_length=max_length)
    
class RenameStorage4(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if self.exists('BraTS20_Validation_001_t2.nii'):
            self.delete('BraTS20_Validation_001_t2.nii')
        return super(RenameStorage4, self).save('BraTS20_Validation_001_t2.nii', content, max_length=max_length)
    

class Image(models.Model):
    image=models.ImageField(storage=RenameStorag() ,upload_to='')
    image_save=models.ImageField(upload_to='images/')


class Result(models.Model):
    content=models.CharField(max_length=50,default=True)

    
def get_image_path(instance, filename):
    
    folder_name = 'output'
    return os.path.join(folder_name, filename)


class ResultS(models.Model):
    content = models.ImageField(upload_to=get_image_path)




class process_image(models.Model):
    user_id = models.IntegerField()
    url_img = models.TextField()
    result = models.CharField(max_length=50) 
    date_on = models.DateTimeField( default=datetime.datetime.now)



class user_image(models.Model):
    user_id = models.IntegerField()
    image = models.ImageField(upload_to='users/',null=True)


import os
def rename_uploaded_file(instance, filename):
    # Get the filename extension
    ext = os.path.splitext(filename)[1]
    # Set the constant filenames
    constant_filenames = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]
    # Set a default value for index
    index = 0
    # Get the index based on the instance ID
    if instance.id is not None:
        index = (instance.id - 1) % len(constant_filenames)
    # Return the new filename
    return os.path.join('images', constant_filenames[index])
    
class RenameStorageee(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if self.exists('BraTS20_Validation_001_t2.nii'):
            self.delete('BraTS20_Validation_001_t2.nii')
        return super(RenameStorage4, self).save('BraTS20_Validation_001_t2.nii', content, max_length=max_length)

class RenameStoragee(FileSystemStorage):




    def save(self, name, content, max_length=None):
        image_names = ['image1.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg']

        for image_name in image_names:
            if self.exists(image_name):
                self.delete(image_name)

        saved_names = []
        for i, image_name in enumerate(image_names):
            saved_name = super(RenameStoragee, self).save(image_name, content[i], max_length=max_length)
            saved_names.append(saved_name)

        return saved_names

class Files(models.Model):
    image_1 = models.ImageField(storage=RenameStorage(), upload_to='', default='')
    image_2 = models.ImageField(storage=RenameStorage1(), upload_to='', default='')
    image_3 = models.ImageField(storage=RenameStorage2(), upload_to='', default='')
    image_4 = models.ImageField(storage=RenameStorage3(), upload_to='', default='')
    image_save = models.ImageField(upload_to='files/')

    def save_images(self, files, folder_name):
        if len(files) == 4:  # Updated condition for four images
            for i, file in enumerate(files[:4]):  # Save only the first four images
                setattr(self, f'image_{i+1}', file)
            self.save()

            for file in files[:4]:  # Save only the first four images
                new_file = Files(image_save=file)
                new_file.save()

            # Move the saved images to the specified folder within the media directory
            folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            for field in ['image_1', 'image_2', 'image_3', 'image_4']:
                image_field = getattr(self, field)
                if image_field:
                    file_path = os.path.join(settings.MEDIA_ROOT, str(image_field))
                    new_file_path = os.path.join(folder_path, os.path.basename(file_path))
                    shutil.move(file_path, new_file_path)
                    setattr(self, field, os.path.relpath(new_file_path, settings.MEDIA_ROOT))
            self.save()




class process_Seg(models.Model):
    user_id = models.IntegerField()
    result = models.CharField(max_length=50) 
    date_on = models.DateTimeField( default=datetime.datetime.now)




from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.firstname
        

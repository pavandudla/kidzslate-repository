# # from django.db import models
# # from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# # # Create your models here.
# #
# # class Student(models.Model):
# #     # Photo=models.ImageField(upload_to='media/')
# #     Admission_number=models.IntegerField(null=True,blank=True,default=0)
# #     Roll_no=models.IntegerField(null=True,blank=True,default=0)
# #     Name=models.CharField(default='pavan',max_length=100)
# #     Age=models.IntegerField(null=True,blank=True,default=0)
# #     Father_name=models.CharField(null=True,max_length=100)
# #     Father_phone_Number=models.IntegerField(null=True,blank=True,default=0)
# #     Mother_phone_Number=models.IntegerField(null=True,blank=True,default=0)
# #     class_name=models.CharField(null=True,max_length=100)
# #     Address=models.CharField(null=True,max_length=100)
# #     Total_fees=models.IntegerField(null=True,blank=True,default=0)
# #     First_term_fee=models.IntegerField(null=True,blank=True,default=0)
# #     Second_term_fee=models.IntegerField(null=True,blank=True,default=0)
# #     Third_term_fee=models.IntegerField(null=True,blank=True,default=0)
# #     username = models.CharField(null=True,max_length=150, unique=True)
#     # email = models.EmailField(null=True, blank=True, unique=True)  # Make the field nullable
#     # password=models.CharField(max_length=100,null=True,blank=True, unique=True)
#     # date_joined = models.DateTimeField(auto_now_add=True)
#
#     # def __str__(self):
#     #     return self.Name
#
# # class User(models.Model):
# #     username=models.CharField(max_length=100)
# #     password=models.CharField(max_length=100)
# #     email=models.EmailField(max_length=100)
#
# # ------------------------------------------- own user creation not built in user creation--------------------
# # class CustomUserManager(BaseUserManager):
# #     def create_user(self, email, password=None, **extra_fields):
# #         if not email:
# #             raise ValueError('The Email field must be set')
# #         email = self.normalize_email(email)
# #         user = self.model(email=email, **extra_fields)
# #         user.set_password(password)
# #         user.save(using=self._db)
# #         return user
# #
# #     def create_superuser(self, email, password=None, **extra_fields):
# #         extra_fields.setdefault('is_staff', True)
# #         extra_fields.setdefault('is_superuser', True)
# #         return self.create_user(email, password, **extra_fields)
# #
# # class CustomUser(AbstractBaseUser):
# #     email = models.EmailField(unique=True)
# #     username = models.CharField(max_length=100)
# #     is_active = models.BooleanField(default=True)
# #     is_staff = models.BooleanField(default=False)
# #     is_superuser = models.BooleanField(default=False)
# #
# #     objects = CustomUserManager()
# #
# #     USERNAME_FIELD = 'email'
# #     REQUIRED_FIELDS = ['username']
# #
# #     def __str__(self):
# #         return self.email
#
#
#
#
#
#
# # from django.db import models
# #
# # class Student(models.Model):
# #     student_img = models.ImageField(upload_to='students/', null=True, blank=True)
# #     Admission_number = models.IntegerField(null=True, blank=True, default=0)
# #     Roll_no = models.IntegerField(null=True, blank=True, default=0)
# #     Name = models.CharField( max_length=100)
# #     Age = models.IntegerField(null=True, blank=True, default=0)
# #     Father_name = models.CharField(null=True, max_length=100)
# #     Father_phone_Number = models.IntegerField(null=True, blank=True, default=0)
# #     Mother_phone_Number = models.IntegerField(null=True, blank=True, default=0)
# #     class_name = models.CharField(null=True, max_length=100)
# #     Address = models.CharField(null=True, max_length=100)
# #     Total_fees = models.IntegerField(null=True, blank=True, default=0)
# #     First_term_fee = models.IntegerField(null=True, blank=True, default=0)
# #     Second_term_fee = models.IntegerField(null=True, blank=True, default=0)
#     # Third_term_fee = models.IntegerField(null=True, blank=True, default=0)
#
#
#
#
#
#
#
# # from django.contrib.auth.models import User
# # from django.db import models
# #
# # class Student(models.Model):
# #     user = models.OneToOneField(user, on_delete=models.CASCADE, related_name='student_profile', default=0)
# #     # user_id=models.IntegerField(default=0)
# #     student_img = models.ImageField(upload_to='students/', null=True, blank=True)
# #     Admission_number = models.IntegerField(null=True, blank=True, default=0)
# #     Roll_no = models.IntegerField(null=True, blank=True, default=0)
# #     Name = models.CharField(max_length=100)
# #     Age = models.IntegerField(null=True, blank=True, default=0)
# #     Father_name = models.CharField(null=True, max_length=100)
# #     Father_phone_Number = models.IntegerField(null=True, blank=True, default=0)
# #     Mother_phone_Number = models.IntegerField(null=True, blank=True, default=0)
# #     class_name = models.CharField(null=True, max_length=100)
# #     Address = models.CharField(null=True, max_length=100)
# #     Total_fees = models.IntegerField(null=True, blank=True, default=0)
# #     First_term_fee = models.IntegerField(null=True, blank=True, default=0)
# #     Second_term_fee = models.IntegerField(null=True, blank=True, default=0)
# #     Third_term_fee = models.IntegerField(null=True, blank=True, default=0)
# #
# #     def __str__(self):
# #         return self.Name
#
#
#
# from django.contrib.auth.models import User
# from django.db import models
#
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
#     # Other fields remain the same
#
#
# # from django.contrib.auth.models import User
# # from django.db import models
# #
# #
# # class Student(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', null=True, blank=True)
#
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', null=True, blank=True)
#     student_img = models.ImageField(upload_to='students/', null=True, blank=True)
#     Admission_number = models.IntegerField(null=True, blank=True, default=0)
#     Roll_no = models.IntegerField(null=True, blank=True, default=0)
#     Name = models.CharField(max_length=100)
#     Age = models.IntegerField(null=True, blank=True, default=0)
#     Father_name = models.CharField(null=True, max_length=100)
#     Father_phone_Number = models.IntegerField(null=True, blank=True, default=0)
#     Mother_phone_Number = models.IntegerField(null=True, blank=True, default=0)
#     class_name = models.CharField(null=True, max_length=100)
#     Address = models.CharField(null=True, max_length=100)
#     Total_fees = models.IntegerField(null=True, blank=True, default=0)
#     First_term_fee = models.IntegerField(null=True, blank=True, default=0)
#     Second_term_fee = models.IntegerField(null=True, blank=True, default=0)
#     Third_term_fee = models.IntegerField(null=True, blank=True, default=0)
#
#     def __str__(self):
#         return self.Name
#








from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', null=True, blank=True)
    student_img = models.ImageField(upload_to='students/', null=True, blank=True)
    Admission_number = models.IntegerField(null=True, blank=True, default=0)
    Roll_no = models.IntegerField(null=True, blank=True, default=0)
    Name = models.CharField(max_length=100)
    # username = models.CharField(max_length=255, null=True)
    Age = models.IntegerField(null=True, blank=True, default=0)
    Father_name = models.CharField(null=True, max_length=100)
    Father_phone_Number = models.IntegerField(null=True, blank=True, default=0)
    Mother_phone_Number = models.IntegerField(null=True, blank=True, default=0)
    class_name = models.CharField(null=True, max_length=100)
    Address = models.CharField(null=True, max_length=100)
    Total_fees = models.IntegerField(null=True, blank=True, default=0)
    First_term_fee = models.IntegerField(null=True, blank=True, default=0)
    Second_term_fee = models.IntegerField(null=True, blank=True, default=0)
    # Third_term_fee = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.Name





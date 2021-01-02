from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from multiselectfield import MultiSelectField
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=self.make_random_password(password),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name="date_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    object = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True


class Profile(models.Model):
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    MARITAL_STATUS_CHOICE = (
        ('married',"Married"),
        ('unmarried','Unmarried'),
        ('divorced','Divorced'),
        ('engaged','Engaged'),
        ('separated','Separated')
    )
    CATEGORY = (
        ('student','Student'),
        ('teacher','Teacher'),
        ('employee', 'Employee'),
        ('employeer','Employeer')
    )
    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+', 'AB+'),
        ('AB-','AB-')
    )
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True, null=True)
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICE, max_length=100, blank=True)
    category = MultiSelectField(choices=CATEGORY, blank=True, null=True)
    blood_groups = models.CharField(choices=BLOOD_GROUP, max_length=5, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='profile_pic', default='avater.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Subject(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class TutionClassDetails(models.Model):
    STATUS = (
        ('available', 'Available'),
        ('busy', 'Busy')
    )
    Tution_class = (
        ('0', 'Nursery'),
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
        ('6','Six'),
        ('7', 'Seven'),
        ('8','Eight'),
        ('9','Nine'),
        ('10','Ten'),
        ('11','Inter-1st'),
        ('12','Inter-2nd'),
        ('13','Varsity Admission')
    )
    Tutoring_style = (
        ('group_tution', 'Group Tution'),
        ('privet_tution', 'Privet Tution')
    )
    Choice_place = (
        ('class_room', 'Class Room'),
        ('Coaching_center', 'Coaching Center'),
        ('home_visit', 'Home Visit'),
        ('my_place', 'My Place')
    )
    Choice_mediam = (
        ('bangla_mediam', 'Bangla Mediam'),
        ('english_mediam', 'English Mediam')
    )
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    tution_class = MultiSelectField(
        choices=Tution_class, blank=True, null=True)
    # location are place here by importing from another apps
    teacher_address = models.CharField(max_length=400)
    tutoring_style = MultiSelectField(choices=Tutoring_style, blank=True, null=True)
    tutoring_place = MultiSelectField(choices=Choice_place, blank=True, null=True)
    mediam = MultiSelectField(choices=Choice_mediam, blank=True, null=True)
    subject = models.ManyToManyField(Subject, related_name='subjects', blank=True, null=True)
    days = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=50, null=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.status}"


class vedio(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    vedio = models.URLField(blank=True, null=True)

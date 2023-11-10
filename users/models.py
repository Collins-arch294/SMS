from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
reportChoices = (( 'Reported Online', 'O'),
                 ('Reported ERP','E', ))
#report model
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    semester = models.CharField(max_length=150)
    date_reported = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=50, choices=reportChoices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.semester

#report model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default="First Name")
    last_name = models.CharField(max_length=30, default="Last Name")
    picture = models.ImageField(default="default.jpeg",upload_to='profile_pictures')
    school = models.CharField(max_length=100 , default="School")
    course = models.CharField(max_length=100, default="Course")
    bio = models.TextField(max_length=500)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    
    

    def __str__(self):
        return self.user.username


from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from tinymce.models import HTMLField
from django.utils.translation import gettext as _

from datetime import datetime , date
# Create your models here.

class Info(models.Model):
    class Meta:
        unique_together = (('user','Name','Roll'),)

    user = models.ForeignKey(User,default='admin')

    Course_list = (('ipg', 'IPG'), ('mtech', 'MTECH'), ('mba', 'MBA'), ('phd', 'PHD'))
    Year_list = (('first', 'FIRST'), ('second', 'SECOND'), ('third', 'THIRD'), ('fourth', 'FOURTH'), ('fifth', 'FIFTH'))
    Name = models.CharField(max_length=250, )

    Course = models.CharField(max_length=10, choices=Course_list, default='ipg', )
    Year = models.CharField(max_length=10, choices=Year_list, default='first', )
    Roll = models.CharField(max_length=100 )
    Pic = models.ImageField(default=None)
    Email = models.EmailField(max_length=250, default=None)
    Website = models.URLField(max_length=250, default=None)
    About = HTMLField(default=None)
    Education = HTMLField(default=None)
    Experience = HTMLField(default=None)
    Test_Scores = HTMLField(default=None)
    Projects = HTMLField(default=None)
    Honors_Awards = HTMLField(default=None)
    Courses = HTMLField(default=None)
    Skills = HTMLField(default=None)




    def get_absolute_url(self):

        return reverse('profile' , kwargs={'student_id':self.pk})




    def __str__(self):
        return self.Name +str(self.id)

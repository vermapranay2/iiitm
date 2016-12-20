
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login , logout
from django import forms
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, request

from .models import Info
from .forms import UserForm


# Create your views here.



class UserFormView(View):


    form_class = UserForm
    template_name = 'students/registration_from.html'

    def get(self,request):


        if self.request.user.is_authenticated():
            try:
                student = Info.objects.get(user=self.request.user)
            except Info.DoesNotExist:
                student = None
            if student == None:
                return redirect('profile-add')
            else:
                return redirect('profile', student_id=student.id)
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profile-add')

        return render(request, self.template_name, {'form': form})


class ProfileCreate(CreateView):
    model = Info
    fields = ['Name', 'Course','Year', 'Roll', 'Pic', 'Email', 'Website', 'About', 'Education', 'Experience', 'Test_Scores',
              'Projects', 'Honors_Awards', 'Courses', 'Skills']




    def form_valid(self, form,):
        l = list()


        for i in Info.objects.all():
            l.append(i.user)
        if self.request.user in l:
            student = Info.objects.get(user=self.request.user)
            return redirect('profile-update', pk=student.id)
        else:

            form.instance.user = self.request.user
            user = self.request.user
            user.first_name = form.instance.Name
            print(form.instance.Name)
            user.save()
            return super(ProfileCreate, self).form_valid(form)

class ProfileUpdate(UpdateView):

    model = Info
    fields = ['Year','Pic', 'Email', 'Website', 'About', 'Education', 'Experience', 'Test_Scores', 'Projects', 'Honors_Awards',
              'Courses', 'Skills']




    def form_valid(self, form):
        instance = form.save(commit=False)
        student = Info.objects.get(user=self.request.user)
        if instance.user != self.request.user:
            return redirect('profile-update', pk=student.id)

        else:

            instance.user = self.request.user
            return super(ProfileUpdate, self).form_valid(form)



def index(request):
    return render(request, 'students/index.html')

def alumni(request):
    return render(request, 'students/alumni.html')

def ipg(request):

    all_students = Info.objects.all()
    student_list=list()
    for i in all_students:
        if i.Course =='ipg':
            student_list.append(i)
    context = {'all_students': student_list}
    return render(request, 'students/ipg.html', context)

def mtech(request):

    all_students = Info.objects.all()
    context = {'all_students': all_students}
    return render(request, 'students/ipg.html', context)

def mba(request):

    all_students = Info.objects.all()
    context = {'all_students': all_students}
    return render(request, 'students/ipg.html', context)

def phd(request):

    all_students = Info.objects.all()
    context = {'all_students': all_students}
    return render(request, 'students/ipg.html', context)


def profile(request, student_id):
    try:
        student = Info.objects.get(pk=student_id)
    except Info.DoesNotExist:
        student = None


    if student!=None:

        return render(request, 'students/profile.html', {'student': student})

    else:
        print("hai")
        return redirect('profile-add')




def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username , password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                try:
                    student = Info.objects.get(user=request.user)
                except Info.DoesNotExist:
                    student = None
                if student==None:
                    return redirect('profile-add')



                return redirect('profile',student_id=student.id)
            else:
                    return render(request, 'students/registration_from.html', {'error_message': 'Your account has been disabled'})
        else:

                return redirect( '/register', {'error_message': 'Invalid login'},)
    return render(request, 'students/registration_from.html')


def user_logout(request):
    logout(request)
    return redirect('/register')

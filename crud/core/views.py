from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import student
from .forms import AddstudentForm
# Create your views here.
@login_required(login_url='login/')

def SignupPage(request):
    if  request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse('your password and confirm password does not match')
        else:
            
          my_user=User.objects.create_user(uname,email,pass1)
          my_user.save()
        return redirect('login/')
      
        

    return render(request,'core/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        print(username,pass1)
        if user is not None:
            login(request,user)
            return redirect('home1')
        else:
            return HttpResponse('username or password incorrect!!')


    return render(request,'core/login.html')

def LogoutPage(request):
    logout (request)
    return redirect('login')



class Home1 (View):
    def get (self, request):

        stu_data=student.objects.all()
        return render(request, 'core/home1.html',{'studata':stu_data})

class Add_student (View):
    def get (self, request):

        fm = AddstudentForm()
        return render(request, 'core/add-student.html',{'form':fm})
    
    def  post(self,request):
        fm=AddstudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home1')
        else:
             return render(request, 'core/add-student.html',{'form':fm})    
 
class Delete_student(View):
    def post(self,request):
        data=request.POST
        id= data.get('id')
        studata= student.objects.get(id=id)
        studata.delete()
        return redirect('home1')
    


class Editstudent (View):
        def get(self, request,id):
             stu= student.objects.get(id=id)
             fm=AddstudentForm(instance=stu)

             return render(request, 'core/edit-student.html',{'form':fm})
        def post(self,request,id):
             stu= student.objects.get(id=id)
             fm= AddstudentForm(request.POST,instance=stu)
             if fm.is_valid():
                  fm.save()
             return redirect('home1')
        

       
from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse 
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import UpdateView, DeleteView
from django.core.exceptions import *
from payments.models import * 
import datetime

def render_pdf_view(request , *args, **kwargs):
    email = request.session['email']
    user = User.objects.get(email = email)
    data = Pass.objects.get(User = user)

    template_path = 'pass_pdf.html'
    context = {'data': data,'user':user}
   
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{data.User.fname} {data.User.lname} Bus Pass.pdf"'
   
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
       html, dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# def pass_pdf(request):
#     email = request.session['email']
#     user = User.objects.get(email = email)
#     data = Pass.objects.get(User = user)
#     return render(request,'pass_pdf.html',{"data":data,"user":user})

###########################################################################################
def index(request):
    try:
        if request.session['email']:
            return render(request, "index.html")
    except:
        return HttpResponseRedirect(reverse('login'))

def login(request):
    try:
        if request.session['email']:
            return HttpResponseRedirect(reverse('index'))
    except:
        if request.POST:
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = User.objects.get(email = email)
                if user:
                    if user.password == password:
                        request.session['email'] = email
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        msg = "Password Does Not Match."
                        return render(request,"login.html",{'msg':msg})
                else:
                    msg = "Email Does Not Match."
                    return render(request,"login.html",{'msg':msg})
                
            except Exception as e:
                msg = "Improper Credentials."
                return render(request, 'login.html', {'msg':msg})

        else:
            return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        global temp 
        temp = {
            'Username' : request.POST['Username'],
            'fname': request.POST['fname'],
            'lname': request.POST['lname'],
            'contact': request.POST['contact'],
            'email': request.POST['email'],
            'address': request.POST['address'],
            'password': request.POST['password'],
            'c_password': request.POST['c_password'],
            'gender': request.POST['Gender'],
            'age': request.POST['age']
            }
        otp = random.randint(1000,9999)
        subject = 'OTP for Sign up'
        message = f'Hello!! Your OTP for Successfully Signing up is {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email'], ]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,'otp_verify.html',{'otp':otp,'temp':temp})
    else:
        return render(request,"signup.html")

def otp_verify(request):
    if request.method =="POST":
        if request.POST['otp'] == request.POST['otp1']:
            if temp['password'] == temp['c_password']:
                ur = User.objects.create(
                    Username = temp['Username'],
                    fname = temp['fname'],
                    lname = temp['lname'],
                    contact = temp['contact'],
                    email = temp['email'],
                    address =  temp['address'],   
                    password = temp['password'],
                    Gender = temp['gender'],
                    age =   temp['age']
                )
                ur.save()
                return render(request,'login.html')
            else:
                return HttpResponse("<h1>Password and Confirm Password Does not match</h1>")
        else:
            return HttpResponse("<h1>OTP Not varify</h1>")
    else:
        return render(request,"otp_verify.html")

def forgot_password(request):
    if request.method == "POST":
        email = request.POST['email']
        otp = random.randint(111111,999999)
        try:
            mail = User.objects.get(email=email)
            send_mail(
                'OTP for New Password',
                f'Here is your otp for new password: {otp}',
                settings.EMAIL_HOST_USER,
                [mail.email],
                fail_silently=False, )
            return render(request,'otp_password.html',{'otp':otp,'mail':mail})
        except:
            return HttpResponse("User Not Valid")
        
    else:
        return render(request,"forgot_password.html")

def otp_password(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        otp1 = request.POST['otp1']
        email = request.POST['email']
        if otp == otp1:
            return render(request, 'user_password.html',{'email':email})
        else:
            return HttpResponse("<h1>OTP Verification Failed </h1>")
    else:
        return render(request, "login.html")

def user_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            email = User.objects.get(email = email)
            if request.POST['password'] == request.POST['c_password']:
                if email:
                    email.password = request.POST['password']
                    email.save()
                    send_mail(
                        'Password Change',
                        f'Your password changed successfully..',
                        settings.EMAIL_HOST_USER,
                        [email.email],
                        fail_silently=False, )

                    return HttpResponseRedirect(reverse('login'))
            else:
                return HttpResponse("<h1>Password and Confirm Password Does not match...</h1>")
        except:
            return HttpResponse("User Not Valid")
    else:
        return render(request,"login.html")

def logout(request):
    try:
        del request.session['email']
        return HttpResponseRedirect(reverse('login'))
    except KeyError:
        return render(request,'login.html')


def header(request):
    return render(request,'header.html')

def pass_form(request):
    try:
        if request.method == "POST":
            email = request.session['email']
            user = User.objects.get(email = email)
            generate = Pass.objects.create(
                User = user,
                Destination = request.POST['Destination'],
                From = request.POST['From'],
                To =request.POST['To'],
                Distance = request.POST['Distance'],
                Duration =request.POST['Duration'],
                Issue_date = request.POST['Issue_date'],
                End_date = request.POST['End_date'],
                Pass_amount = request.POST['Pass_amount']
            )
            generate.save()
            return HttpResponseRedirect(reverse('user_pass'))
        else:
            return render(request,'pass_form.html')
    except:
        return HttpResponse("<h1>User already Exiets..</h1>")
    
def user_pass(request):
    try:
        email = request.session['email']
        user = User.objects.get(email = email)
        data = Pass.objects.get(User = user)
        status = Transaction.objects.filter(pass_id = data).latest('pay_status')
        date = datetime.date.today().strftime("%d/%m/%Y")
        return render(request,'user_pass.html',{"data":data,"user":user,"status":status})
    except:
        try:
            email = request.session['email']
            user = User.objects.get(email = email)
            data = Pass.objects.get(User = user)
            return render(request,'user_pass.html',{"data":data,"user":user})
        except:
            email = request.session['email']
            user = User.objects.get(email = email)
            return render(request,'user_pass.html',{"user":user})

class UserUpdateView(UpdateView):
    model = User
    fields= "__all__"
    template_name = "user_update.html"
    success_url = reverse_lazy('logout')

    def form_valid(self,form):
        if self.request.session['email'] == self.request.POST['email']:
            return super().form_valid(form) and HttpResponseRedirect(reverse('user_pass'))
        else:
            return super().form_valid(form)

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('logout')
    template_name = "user_delete.html"


class PassUpdateView(UpdateView):
    model = Pass
    fields= ['Destination','From','To','Distance','Duration','Issue_date','End_date','Pass_amount']
    template_name = "pass_update.html"
    success_url = reverse_lazy('pay')

class PassDeleteView(DeleteView):
    model = Pass
    success_url = reverse_lazy('user_pass')
    template_name = "pass_delete.html"

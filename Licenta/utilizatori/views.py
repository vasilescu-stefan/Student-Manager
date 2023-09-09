from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm, ResetPasswordForm, ForgotPasswordForm
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated
from vizualizare.models import Note, Students, Cursuri
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q
from email.message import EmailMessage
import ssl
import smtplib
# Create your views here.


def activate(request, uidb64, token):
    User=get_user_model()
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Multumesc pentru confirmare")
        return redirect("login")
    else:
        messages.error(request, "Link-ul de activare este invalid")
    return redirect("starting-page")

def activateEmail2(request, user, email):

    email_sender = ""
    email_pass = ""
    email_receiver = [email]

    subject = "Activate your account"
    body = render_to_string("utilizatori/activate_account.html", context={
            "user":user,
            "domain": get_current_site(request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocol": 'https' if request.is_secure() else 'http',
        })
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_sender, email_pass)
        server.sendmail(email_sender, email_receiver, em.as_string())
        messages.success(request, f"Draga {user.username}, te rog sa verifici la adresa de email: {email} pentru a iti activa contul in urmatoarele 15 minute\
                            Observatie: nu uita sa verifici spam-ul")


def register(request):
    exista=False
    if request.user.is_authenticated:
        return redirect("starting-page")
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            if not Students.objects.filter(nr_matricol=form.cleaned_data["nr_matricol"]):
                exista = True
                return render(request, template_name="utilizatori/register.html", context={
                "form": form,
                "exista": exista,
                })
            else:
                #For activation without email
                user=form.save(commit=False)
                user.is_active=False
                user.save()
                activateEmail2(request, user, form.cleaned_data["email"])
                #For email activation
                # user=form.save()
                # messages.success(request,f"New account created {user.username}")
                # login(request,user)
                return redirect("/")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form= RegisterForm()
    return render(request, template_name="utilizatori/register.html", context={
        "form": form,
        "exista": exista,
    })

@login_required
def logout_request(request):
    logout(request)
    messages.success(request,("You were logged out"))
    return redirect("starting-page")


def login_request(request):
    if request.user.is_authenticated:
        return redirect("starting-page")

    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user=authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                messages.success(request, ("Successfully logged in"))
                return redirect ("profil")
                # return render(request, "starting-page",context={})
        else:
            for key, error in list(form.errors.items()):
                if key=="captcha" and error[0] == "This field is requierd.":
                    messages.error(request, "Nu uita de testul reCAPTCHA")
                messages.error(request,error)
    else:
        form = LoginForm()
        return render(request, "utilizatori/login.html",context={
            "form": form
        })

@login_required    
def profil(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
        nr_matricol=request.user.nr_matricol
        student_an=Students.objects.get(nr_matricol=nr_matricol).an
        nume_student=Students.objects.get(nr_matricol=nr_matricol).nume
        prenume_student=Students.objects.get(nr_matricol=nr_matricol).prenume
        grupa_student=Students.objects.get(nr_matricol=nr_matricol).grupa
        specializare_student=Students.objects.get(nr_matricol=nr_matricol).specializare
        data_nasterii_student=Students.objects.get(nr_matricol=nr_matricol).data_nastere
        telefon_sudent=Students.objects.get(nr_matricol=nr_matricol).telefon
        mama_student=Students.objects.get(nr_matricol=nr_matricol).mama
        tata_student=Students.objects.get(nr_matricol=nr_matricol).tata
        nationalitate_student=Students.objects.get(nr_matricol=nr_matricol).nationalitatea
        cetatenia_student=Students.objects.get(nr_matricol=nr_matricol).cetatenia
        nota = Note.objects.filter(nr_matricol=nr_matricol)
        curs=Cursuri.objects.filter(an=student_an)
        puncte1=0
        suma1=0
        credite1=0
        for note in nota:
            cursuri=Cursuri.objects.filter(semestru=1)
            for curse in cursuri:
                if note.id_curs == curse.id_curs:
                    if note.valoare is None:
                        media_sem1=0
                        credite1=0
                        puncte1=0
                        break
                    puncte1=puncte1+note.valoare*curse.credite
                    suma1+=note.valoare
                    credite1+=curse.credite
        media_sem1=suma1/6
        media_sem1=round(media_sem1, 2)     
        puncte2=0
        suma2=0
        credite2=0
        for note in nota:
            cursuri=Cursuri.objects.filter(semestru=2)
            for curse in cursuri:
                if note.id_curs == curse.id_curs:
                    if note.valoare is None:
                        media_sem2=0
                        credite2=0
                        puncte2=0
                        break
                    puncte2=puncte2+note.valoare*curse.credite
                    suma2+=note.valoare
                    credite2+=curse.credite
        media_sem2=suma2/6
        media_sem2=round(media_sem2, 2)      
        puncte3=0
        suma3=0
        credite3=0
        for note in nota:
            cursuri=Cursuri.objects.filter(semestru=3)
            for curse in cursuri:
                if note.id_curs == curse.id_curs:
                    if note.valoare is None:
                        media_sem3=0
                        credite3=0
                        puncte3=0
                        break
                    puncte3=puncte3+note.valoare*curse.credite
                    suma3+=note.valoare
                    credite3+=curse.credite
        media_sem3=suma3/6
        media_sem3=round(media_sem3, 2)    
        puncte4=0
        suma4=0
        credite4=0
        for note in nota:   
            cursuri=Cursuri.objects.filter(semestru=4)
            for curse in cursuri:
                if note.id_curs == curse.id_curs:
                    if note.valoare is None:
                        media_sem4=0
                        credite4=0
                        puncte4=0
                        break
                    puncte4=puncte4+note.valoare*curse.credite
                    suma4+=note.valoare
                    credite4+=curse.credite
        media_sem4=suma4/6
        media_sem4=round(media_sem4, 2)      
        puncte5=0
        suma5=0
        credite5=0
        for note in nota:
            cursuri=Cursuri.objects.filter(semestru=5)
            for curse in cursuri:
                if note.id_curs == curse.id_curs:
                    if note.valoare is None:
                        media_sem5=0
                        credite5=0
                        puncte5=0
                        break
                    puncte5=puncte5+note.valoare*curse.credite
                    suma5+=note.valoare
                    credite5+=curse.credite
        media_sem5=suma5/6
        media_sem5=round(media_sem5, 2)        
        puncte6=0
        suma6=0
        credite6=0
        for note in nota:
            cursuri=Cursuri.objects.filter(semestru=6)
            for curse in cursuri:
                if note.id_curs == curse.id_curs:
                    if note.valoare is None:
                        media_sem6=0
                        credite6=0
                        puncte6=0
                        break
                    puncte6=puncte6+note.valoare*curse.credite
                    suma6+=note.valoare
                    credite6+=curse.credite
        media_sem6=suma6/6
        media_sem6=round(media_sem6, 2)
        media_an1=(media_sem1+media_sem2)/2
        puncte_an1=puncte1+puncte2
        credite_an1=credite1+credite2
        media_an2=(media_sem3+media_sem4)/2
        puncte_an2=puncte3+puncte4
        credite_an2=credite3+credite4
        media_an3=(media_sem5+media_sem6)/2
        puncte_an3=puncte5+puncte6
        credite_an3=credite5+credite6
    else:
        username = None
        email = None
        nr_matricol = None

    context = {
        'username': username,
        'email': email,
        "nr_matricol": nr_matricol,
        "nota":nota,
        "curs": curs,
        "student_an":student_an,
        "nume_student":nume_student,
        "prenume_student":prenume_student,
        "grupa_student":grupa_student,
        "specializare_student":specializare_student,
        "data_nasterii_student":data_nasterii_student,
        "telefon_sudent":telefon_sudent,
        "mama_student":mama_student,
        "tata_student":tata_student,
        "nationalitate_student":nationalitate_student,
        "cetatenia_student":cetatenia_student,
        "media_sem1":media_sem1,
        "puncte1":puncte1,
        "credite1":credite1,
        "media_sem2":media_sem2,
        "puncte2":puncte2,
        "credite2":credite2,
        "media_sem3":media_sem3,
        "puncte3":puncte3,
        "credite3":credite3,
        "media_sem4":media_sem4,
        "puncte4":puncte4,
        "credite4":credite4,
        "media_sem5":media_sem5,
        "puncte5":puncte5,
        "credite5":credite5,
        "media_sem6":media_sem6,
        "puncte6":puncte6,
        "credite6":credite6,
        "media_an1":media_an1,
        "puncte_an1":puncte_an1,
        "credite_an1":credite_an1,
        "media_an2":media_an2,
        "puncte_an2":puncte_an2,
        "credite_an2":credite_an2,
        "media_an3":media_an3,
        "puncte_an3":puncte_an3,
        "credite_an3":credite_an3,
    }

    return render(request, 'utilizatori/profil.html', context)


@login_required
def change_password(request):
    user= request.user
    if request.method == "POST":
        form = ResetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Parola a fost schimbata")
            return redirect("login")
        else:
            for error in list(form.errors.values()):
                messages.error(request,error)
    form = ResetPasswordForm(user)
    return render(request, "utilizatori/password_reset.html", context = {
        "form":form,
    })


def password_reset_request(request):
    if request.user.is_authenticated:
        return redirect("starting-page")
    
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            user_email=form.cleaned_data["email"]
            user_with_existing_email=get_user_model().objects.get(email=user_email)
            print("USER",user_with_existing_email.pk)
            if user_with_existing_email:
                    email_sender = "esims9978@gmail.com"
                    email_pass = "cvxmijylmkmmiqbf"
                    email_receiver = [user_email]

                    subject = "Cerere resetare parola"
                    body = render_to_string("utilizatori/reset_password.html", context={
                            "user":user_with_existing_email,
                            "domain": get_current_site(request).domain,
                            "uid": urlsafe_base64_encode(force_bytes(user_with_existing_email.pk)),
                            "token": account_activation_token.make_token(user_with_existing_email),
                            "protocol": 'https' if request.is_secure() else 'http',
                        })
                    em = EmailMessage()
                    em['From'] = email_sender
                    em['To'] = email_receiver
                    em['Subject'] = subject
                    em.set_content(body)

                    context = ssl.create_default_context()

                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login(email_sender, email_pass)
                        server.sendmail(email_sender, email_receiver, em.as_string())
                        messages.success(request, f"Email cu istructiuni trimis catre {user_email}")
            return redirect("starting-page")
        for key, error in list(form.errors.items()):
                if key=="captcha" and error[0] == "This field is requierd.":
                    messages.error(request, "Nu uita de testul reCAPTCHA")
                messages.error(request,error)
    form=ForgotPasswordForm()
    return render(request, "utilizatori/forgot_password.html", context={
        "form":form,
    })

def password_reset_confirm(request, uidb64, token):
    User=get_user_model()
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == "POST":
            form=ResetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Parola a fost resetata")
                return redirect("login")
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
        form=ResetPasswordForm(user)
        return render(request, "utilizatori/password_reset.html", context = {
                    "form":form,
                    })
    else:
        messages.error(request, "Link-ul a expirat")
    messages.error(request, "Ceva nu a functiona, vei fi redirectionat catra pagina de start")
    return redirect("starting-page")


@login_required
def materii_an1(request):
    username = request.user.username
    nr_matricol=request.user.nr_matricol
    nota = Note.objects.filter(nr_matricol=nr_matricol)
    curs=Cursuri.objects.filter(an=1)

    context = {
        'username': username,
        "nr_matricol": nr_matricol,
        "nota":nota,
        "curs": curs,
    }

    return render(request, 'utilizatori/materii_an1.html', context)


@login_required
def materii_an2(request):
    username = request.user.username
    nr_matricol=request.user.nr_matricol
    nota = Note.objects.filter(nr_matricol=nr_matricol)
    curs=Cursuri.objects.filter(an=2)

    context = {
        'username': username,
        "nr_matricol": nr_matricol,
        "nota":nota,
        "curs": curs,
    }

    return render(request, 'utilizatori/materii_an2.html', context)

@login_required
def materii_an3(request):
    username = request.user.username
    nr_matricol=request.user.nr_matricol
    nota = Note.objects.filter(nr_matricol=nr_matricol)
    curs=Cursuri.objects.filter(an=3)

    context = {
        'username': username,
        "nr_matricol": nr_matricol,
        "nota":nota,
        "curs": curs,
    }

    return render(request, 'utilizatori/materii_an3.html', context)

from django.shortcuts import render
from basicapp import forms
from basicapp.models import Contact, RegistredUser

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')
    

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            name_input = form.cleaned_data['name']
            email_input = form.cleaned_data['email']
            text_input = form.cleaned_data['text']
            print("VALIDATION SUCCESS!")
            print("NAME: " + name_input)
            print("EMAIL: " + email_input)
            print("TEXT: " + text_input)
            ins = Contact.objects.get_or_create(name=name_input, email=email_input, text=text_input)[0]
            #ins.save()
            print("The contact form data has been saved to the database.")
            return render(request, 'basicapp/thanks.html', {})

    return render(request, 'basicapp/form_page.html', {'form':form})


def thanks(request):
    template = "basicapp/thanks.html"
    context = {}
    return render(request, template, context)


def form_user_view(request):
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            username_input = form.cleaned_data['username']
            name_input = form.cleaned_data['name']
            email_input = form.cleaned_data['email']
            re_email_input = form.cleaned_data['re_email']
        
            if email_input != re_email_input:
                form.add_error('re_email', "Typed emails mismatch.")
            elif RegistredUser.objects.filter(username=username_input).exists():
                form.add_error('username', 'Username is not unique')
            else: 
                print("VALIDATION SUCCESS!")
                print("USERNAME: " + username_input)
                print("NAME: " + name_input)
                print("EMAIL: " + email_input)
                ins = RegistredUser.objects.get_or_create(username=username_input, name=name_input, email=email_input)[0]
                print("The user data has been registred to the database.")
                return render(request, 'basicapp/thanks.html', {})

    return render(request, 'basicapp/user_page.html', {'form':form})
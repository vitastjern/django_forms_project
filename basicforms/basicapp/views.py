
from django.shortcuts import render, redirect
from basicapp import forms
from basicapp.models import Contact

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
            print("The data has been saved to the database.")
            return render(request, 'basicapp/thanks.html', {})

    return render(request, 'basicapp/form_page.html', {'form':form})


def thanks(request):
    template = "basicapp/thanks.html"
    context = {}
    return render(request, template, context)

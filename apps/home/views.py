from django.shortcuts import redirect,render
from apps.home.models import (
    Home, Service, Price,
    Partners, Team, FAQ,
    About,AboutService,Benefits,
    Contact  
)
from apps.home.forms import ContactForm
# Create your views here.
def index(request):
    home = Home.objects.latest('id')
    service = Service.objects.all().order_by('-id') 
    price = Price.objects.all().order_by('-id')[:3]
    partners = Partners.objects.all().order_by('-id')
    teams = Team.objects.all().order_by('-id')
    faq = FAQ.objects.all().order_by('-id')
    about = About.objects.all().order_by('-id') 
    aboutservice = AboutService.objects.all().order_by('-id')[:6]
    benefits = Benefits.objects.all()[:6]
    contact = Contact.objects.all().order_by('-id')  

    context = {
        'homes' : home,
        'prices' : price,
        'services' : service,
        'partners' : partners,
        'teams' : teams,
        'faqs' : faq,
        'abouts': about,
        'aboutservices': aboutservice,
        'benefits' : benefits, 
        'contacts' : contact
    }
    return render(request, 'index.html', context)


def service_page(request):
    home = Home.objects.latest('id')
    context = {
        'homes':home,
    }
    return render(request,'services.html',context)

def service_details_page(request,id):
    service = Service.objects.get(id = id)
    context = {
        'service':service,
    }
    return render(request,'service-details.html',context)
 

def contact_us_page(request):
    home = Home.objects.latest('id')
    context = {
        'homes':home,
    }
    return render(request,'contact-us.html',context)

def contact_us(request):
    home = Home.objects.latest('id')
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            contact = form.save()
            return redirect('thank_you')
   
    return render(request, 'contact-us.html', locals())

def thank_you(request):
    return render(request, 'thank_you.html')

def support(request):  
    contact = Contact.objects.all()
    home = Home.objects.latest('id')
    context = {
        'contacts' : contact,
        'homes' : home,
    }

    return render(request, 'support.html',context)

def about_us_page(request):
    home = Home.objects.latest('id')
    partners = Partners.objects.all().order_by('-id') 
    teams = Team.objects.all().order_by('-id')
    service = Service.objects.all().order_by('-id')
    contact = Contact.objects.all().order_by('-id') 
    context = {
        'homes':home, 
        'partners' : partners,
        'teams' : teams,
        'services' : service,
        'contacts' : contact
    }
    return render(request,'about-us.html',context)




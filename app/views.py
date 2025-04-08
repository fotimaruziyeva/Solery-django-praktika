from django.shortcuts import render,HttpResponse
from .models import Shop,Faq,Blog,Contact
from hitcount.views import HitCountDetailView

def home_view(request):
    return render(request, 'index.html')


def shopdetails_view(request):
    return render(request, 'shop-details.html')

def shop_view(request):
    model = Shop.objects.all()
    context = {
       'items': model,
    }
    return render(request, 'shop.html',context=context)


def blog_view(request):
    model = Blog.objects.all()
    context = {
        "blogs":model
    }
    
    return render(request, 'blog.html',context) 


    
    
def faq_view(request):
    model=Faq.objects.all()
    context={
        "items":model
    }
    return render(request, 'faq.html',context)

class BlogdetailsView(HitCountDetailView):
    model=Blog
    context_object_name = 'blog'
    template_name='blog-details.html'
    count_hit = True   
    
# def blogdetails_view(request,id):
#     model= Blog.objects.get(id=id)
#     context={
#         "blog":model
#     }
#     return render(request, 'blog-details.html',context)


def contact_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if not firstname or not email or not subject or not message or not lastname:
            print(f"contact_firstname: {firstname}, contact_email: {email}, contact_subject: {subject}, contact_message: {message}")
            return HttpResponse('All fields are required.', status=400)

    
        print(firstname, lastname,email, subject, message)
        print("Siz POST request yubordingiz")

       
        contact = Contact(firstname=firstname,lastname=lastname, email=email, subject=subject, message=message)
        contact.save()

       
        return render(request,'contact2.html', {'success': True})
    return render(request, 'contact.html')
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Example view function
    return HttpResponse("Hello, world! This is the index page.")

def about(request):
    # Another view function
    return render(request, 'about.html')

def contact(request):
    # Another view function
    if request.method == 'POST':
        # Process form data if the request is a POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Process the data, maybe save it to a database, send emails, etc.
        # Here, we're just returning a simple response for demonstration
        return HttpResponse(f"Thank you {name} for your message. We'll get back to you soon.")
    else:
        # Render the contact form template for GET requests
        return render(request, 'contact.html')

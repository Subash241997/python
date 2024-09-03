import random, string

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import models

# Create your views here.

def generate_email_address(request):
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email_address = f"{random_string}@example.com"  # Replace example.com with your domain
    return JsonResponse({"email_address": email_address})

@csrf_exempt
def receive_email(request):
    email_address = request.POST.get('to')
    subject = request.POST.get('subject')
    body = request.POST.get('text')

    if email_address and subject and body:
        models.Email.objects.create(
            email_address=email_address,
            subject=subject,
            body=body
        )
        return HttpResponse(status=200)

    return HttpResponse(status=400)

def view_inbox(request, email_address):
    emails = models.Email.objects.filter(email_address=email_address).order_by('-received_at')
    return render(request, 'emails/inbox.html', {'emails': emails})
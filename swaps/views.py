from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import SwapRequest

@login_required
def send_request(request, user_id):
    receiver = User.objects.get(id=user_id)

    if request.method == 'POST':
        offered = request.POST['offered']
        requested = request.POST['requested']

        SwapRequest.objects.create(
            sender=request.user,
            receiver=receiver,
            skill_offered=offered,
            skill_requested=requested
        )
        return redirect('browse')

    return render(request, 'send_request.html', {'receiver': receiver})

@login_required
def requests_page(request):
    received = SwapRequest.objects.filter(receiver=request.user)
    sent = SwapRequest.objects.filter(sender=request.user)

    return render(request, 'requests.html', {
        'received': received,
        'sent': sent
    })

@login_required
def accept_request(request, id):
    req = SwapRequest.objects.get(id=id)
    req.status = 'Accepted'
    req.save()
    return redirect('requests')

@login_required
def reject_request(request, id):
    req = SwapRequest.objects.get(id=id)
    req.status = 'Rejected'
    req.save()
    return redirect('requests')

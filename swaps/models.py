from django.db import models
from django.contrib.auth.models import User

class SwapRequest(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Accepted','Accepted'),
        ('Rejected','Rejected'),
    )

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')

    skill_offered = models.CharField(max_length=100)
    skill_requested = models.CharField(max_length=100)

    status = models.CharField(max_length=10, choices=STATUS, default='Pending')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} → {self.receiver}"

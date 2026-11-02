from django.db import models

class Complaint(models.Model):
    complaint_id = models.CharField(max_length=255, unique=True)
    complainant_user_id = models.PositiveBigIntegerField()
    category = models.CharField(max_length=50, choices=[
        ('hostel', 'Hostel'),
        ('academic', 'Academic'),
        ('maintenance', 'Maintenance'),
        ('network', 'Network'),
        ('mess', 'Mess'),
        ('other', 'Other'),
    ])
    description = models.TextField()
    priority = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], default='low')
    status = models.CharField(max_length=50, choices=[
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
        ('closed', 'Closed'),
    ], default='submitted')
    assigned_handler_id = models.PositiveBigIntegerField(null=True, blank=True)
    resolution_details = models.TextField(blank=True)
    rejection_reason = models.TextField(blank=True)
    is_escalated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ComplaintAttachment(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_size = models.PositiveIntegerField()
    file_type = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ComplaintProgress(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    actor_user_id = models.PositiveBigIntegerField()
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
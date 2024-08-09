from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # if a user is deleted, their post will also be deleted.

    def __str__(self):
        return self.title

class CMIssuesHeader(models.Model):
    id = models.IntegerField(primary_key=True)
    MIssueNo = models.CharField(max_length=50)
    MDate = models.CharField(max_length=50)
    MDescription = models.CharField(max_length=50)
    MComment = models.CharField(max_length=50)
    Reference = models.CharField(max_length=50)
    IssueNo = models.CharField(max_length=50)
    Posted = models.IntegerField()
    LastUser = models.CharField(max_length=50)
    LastMaintained = models.CharField(max_length=50)
    SubLocation = models.CharField(max_length=50)
    Contractor = models.CharField(max_length=50)
    MSite = models.CharField(max_length=50)
    TicketNo = models.CharField(max_length=50)
    IssueType = models.CharField(max_length=50)
    UserDepartment = models.CharField(max_length=50)
    SDUManager = models.CharField(max_length=50)
    ProcurementManager = models.CharField(max_length=50)
    CTO = models.CharField(max_length=50)
    RequestedBy = models.CharField(max_length=50)
    Destination = models.CharField(max_length=50)
    DeliveryDate = models.CharField(max_length=50)
    # MProject = models.CharField(max_length=50)
    # MYear = models.CharField(max_length=50)
    # MTask = models.CharField(max_length=50)
    # BTS = models.CharField(max_length=50)
    RequestedByTime = models.CharField(max_length=50)
    SDUManagerTime = models.CharField(max_length=50)
    ProcurementManagerTime = models.CharField(max_length=50)
    PostedToInventoryTime  = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.MIssueNo



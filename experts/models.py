from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ExpertComments(models.Model):
    cmtid = models.AutoField(primary_key=True)
    eid = models.IntegerField()
    eproblem = models.TextField(blank=True, null=True)
    ecomment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expert_comments'

    def __str__(self):
        # 默认的人们可读的对象表达方式
        return self.eproblem


class ExpertInfo(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=50)
    esex = models.CharField(max_length=2)
    emobile = models.CharField(max_length=50, blank=True, null=True)
    eemail = models.CharField(max_length=80, blank=True, null=True)
    etrade = models.CharField(max_length=150, blank=True, null=True)
    esubtrade = models.CharField(max_length=150, blank=True, null=True)
    ebirthday = models.DateField(blank=True, null=True)
    elandline = models.CharField(max_length=50, blank=True, null=True)
    elocation = models.CharField(max_length=150, blank=True, null=True)
    emsn = models.CharField(max_length=80, blank=True, null=True)
    eqq = models.CharField(max_length=50, blank=True, null=True)
    ephoto = models.CharField(max_length=20, blank=True, null=True)
    estate = models.IntegerField(blank=True, null=True)
    ecomefrom = models.TextField(blank=True, null=True)
    eremark = models.TextField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expert_info'
        ordering = ('-addtime',)

    def __str__(self):
        return self.ename
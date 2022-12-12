from django.db import models


# Create your models here.


class Registration(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    tg_id = models.IntegerField()
    school = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    test = models.IntegerField(null=True,blank=True,verbose_name="Result of test",default=0)
    region = models.CharField(max_length=50,null=True,blank=True)
    presentation = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, null=True, blank=True)


class Question(models.Model):
    Q = models.TextField()
    V1 = models.CharField(max_length=50, null=True, blank=True,name='V1')
    V2 = models.CharField(max_length=50, null=True, blank=True,name='V2')
    V3 = models.CharField(max_length=50, null=True, blank=True,name='V3')
    V4 = models.CharField(max_length=50, null=True, blank=True,name='V4')
    choices = (("V1",V1.name),("V2",V2.name),("V3",V3.name),("V4",V4.name))
    Answer  = models.CharField(max_length=50,choices=choices,null=True,blank=True)

class Question_ru(models.Model):
    Q = models.TextField()
    V1 = models.CharField(max_length=50, null=True, blank=True,name='V1')
    V2 = models.CharField(max_length=50, null=True, blank=True,name='V2')
    V3 = models.CharField(max_length=50, null=True, blank=True,name='V3')
    V4 = models.CharField(max_length=50, null=True, blank=True,name='V4')
    choices = (("V1",V1.name),("V2",V2.name),("V3",V3.name),("V4",V4.name))
    Answer  = models.CharField(max_length=50,choices=choices,null=True,blank=True)

class Result(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=30,null=True, blank=True)
    tg_id = models.IntegerField()
    quiz = models.IntegerField(null=True, blank=True)
    answer_id = models.IntegerField(null=True, blank=True)
    answer = models.CharField(max_length=30,null=True, blank=True)
    result = models.CharField(max_length=10,null=True, blank=True)
    time = models.DateTimeField(auto_now=True)

class Result_ru(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=30,null=True, blank=True)
    tg_id = models.IntegerField()
    quiz = models.IntegerField(null=True, blank=True)
    answer_id = models.IntegerField(null=True, blank=True)
    answer = models.CharField(max_length=30,null=True, blank=True)
    result = models.CharField(max_length=10,null=True, blank=True)
    time = models.DateTimeField(auto_now=True)

class Region(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Region_ru(models.Model):
    name = models.CharField(max_length=50)
    name_lotin = models.CharField(max_length=50,null=True,blank=True)
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    tg_id = models.IntegerField()
    time = models.DateTimeField(auto_now=True)


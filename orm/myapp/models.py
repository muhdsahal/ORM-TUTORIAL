from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date,timezone

# Create your models here.
class teacher(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    
    

class std(models.Model):
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    domain=models.CharField(max_length=50)
    position=models.CharField( max_length=50)

#bck100
class bck100(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    domain=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    salary=models.IntegerField()
    
#joining 
#one to one
class phone(models.Model):
    num=models.IntegerField()

#one to many
class course(models.Model):
    cou_name=models.CharField(max_length=50)

# many to many
class skill(models.Model):
    skill_name=models.CharField(max_length=50)

#joined tree table
class person(models.Model):
    name=models.CharField(max_length=50)
    person_no=models.OneToOneField(phone, on_delete=models.CASCADE)
    course_name=models.ForeignKey(course, on_delete=models.CASCADE)
    skill_name=models.ManyToManyField(skill)
    



#select releted 
class Author(models.Model):
    name=models.CharField(max_length=100)


class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)


#prefetch releted
class Owner(models.Model):
    name=models.CharField(max_length=100)

class bikes(models.Model):
    model=models.CharField(max_length=50)
    owner=models.ManyToManyField(Owner)

# table emp
class emp(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    dob=models.DateField()

# abstrst base model inheritance
class Baseitem(models.Model):
    title=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
        ordering=['title']

class itemA(Baseitem):
    content=models.TextField()

    class Meta(Baseitem.Meta):
        ordering=['-created']
    
class itemB(Baseitem):
    desc=models.CharField(max_length=200)

class itemC(Baseitem):
    review=models.CharField(max_length=200)

class itemD(Baseitem):
    slug=models.SlugField(max_length=255,unique=True)


# model table inheritance
class Vehicles(models.Model):
    make=models.CharField(max_length=100)
    year=models.IntegerField()

class Modific(Vehicles):
    Modific=models.CharField(max_length=100)
   

# proxy model  inheritence
class carmodel(models.Model):
    name=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

class carbooking(carmodel):
    class Meta:
        proxy=True
        ordering=['created']
    def Created_on(self):
        return timezone.now()-self.cr
    

# class Owner(models.Model):
#     name=models.CharField(max_length=100)

# class bikes(models.Model):
#     model=models.CharField(max_length=50)
#     owner=models.ManyToManyField(Owner)


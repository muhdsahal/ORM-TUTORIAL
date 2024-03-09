from django.shortcuts import render
# from .models import teacher

# Create your views here


# a=bck100.objects.filter(salary=59500).update(salary=F('salary')+8000)
# query= Q(name='sahal')& Q(age=22)
# a=bck100.objects.filter(query)

# a=bck100.objects.aggregate(sum=Sum('salary'))
# sum=a['sum']
# print(sum)

# a=bck100.objects.annnotate(avag=Avg('salary'))
#  for i in a: print(i.name,i.salary,i.avag)

# a=bck100.objects.raw('select * from myapp_bck100 where age > 20')
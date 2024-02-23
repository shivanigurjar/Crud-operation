from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import your_model
# Create your views here.
#this function will add new items and show all items
def first_(request):
    return render(request, 'base.html')
 
def home(request):
    if request.method =='POST':
     fm= StudentRegistration(request.POST)
     if fm.is_valid():
         nm = fm.cleaned_data['First_name']
         lm = fm.cleaned_data['Last_name']
         pw = fm.cleaned_data['Password']
         reg = your_model(First_name=nm,Last_name=lm,Password=pw)
         reg.save()
         fm= StudentRegistration()
         
    else:
     fm= StudentRegistration()
    stud = your_model.objects.all()
    return render(request, 'index.html',{'form':fm, 'stu':stud})
#this function will delete
def delete_data(request,ID):
    if request.method=='POST':
        pi = your_model.objects.get(pk=ID)
        pi.delete()
        return HttpResponseRedirect('/')
# this function will update/edit        
def update(request,ID):
    if request.method == 'POST':
        pi = your_model.objects.get(pk=ID)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
         pi = your_model.objects.get(pk=ID)
         fm = StudentRegistration(request.POST,instance=pi)
                
        
    return render(request,'update.html' , {'form': fm})    
    

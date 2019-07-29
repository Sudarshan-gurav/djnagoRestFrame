from django.shortcuts import render ,redirect
from django.http import HttpResponse
# from .forms import AllFeildForm
from .forms import AllFeilds_Form , AllFeildForm ,UserForm
from .models import AllFeilds_1
# Create your views here.
from . import forms
def home(request):
    data = AllFeilds_1.objects.all()
    context = {'data':data}
    return render(request,'home.html',context)


# def allfeilds(request):
#     form = AllFeildForm(request.POST)
#     if request.method == 'POST':
#         form = AllFeildForm(request.POST,request.FILES)
#         if form.is_valid():
#             sv = form.save()
#             # sv.save()
#             form = AllFeildForm()
#             return redirect('home')
#     return render(request,'index.html',{'forms':form})


def alldeilds_detail(request):
    form = AllFeilds_Form()    
    if request.method == 'POST':
        form = AllFeilds_Form(request.POST,request.FILES)
        if form.is_valid():
           form.save()
           return redirect('home')
        else:
           print('invalid') 
    return render(request,'index.html',{'forms':form})


def editField(request,pk):
    current = AllFeilds_1.objects.get(id=pk)
    form = AllFeilds_Form(instance=current)
    
    if request.method == 'POST':
        form = AllFeilds_Form(request.POST,instance=current)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('invalid')
    return render(request,'edit.html',{'form':form})

def deleteField(request,pk):
    current = AllFeilds_1.objects.get(id=pk)
    form = AllFeilds_Form(instance=current)
    context = {'form':form}
    if request.method == 'POST':
        current.delete()
        return redirect('home')
    return render(request,'delete.html',context)

def form_Forms(request):
    form = forms.UserForm(request.POST or None)
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            AllFeilds_1.objects.create(**form.cleaned_data)
            return redirect('homeform')
    return render(request,'form.html',{'forms':form})
    



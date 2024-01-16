from django.shortcuts import render
from django.views.generic import View
from django import forms
from math import pow

# Create your views here.


class OperationForm(forms.Form):
    num1=forms.CharField()
    num2=forms.CharField()





class PowerView(View):
    def get(self,request,*args,**kwargs):
        form=OperationForm()
        return render(request,"power.html",{"form":form}) 
    


class RegistrationForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField()
    password2=forms.CharField()


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
        else:
            print("form has error")

    

class LoginFrom(forms.Form):
    username=forms.CharField()
    password=forms.CharField()



class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginFrom()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginFrom(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(" form has errors")
        return render(request,"login.html",{"form":form})
    


class EmiForm(forms.Form):
    loan_amount=forms.IntegerField()
    tenure=forms.IntegerField()
    interest_rate=forms.IntegerField()


class EmiCalculatorView(View):
        def get(self,request,*args,**kwargs):
            form=EmiForm()
            return render(request,"emi.html",{"form":form})
        def post(self,request,*args,**kwargs):
            form=EmiForm(request.POST)

            if form.is_valid():
                print(form.cleaned_data)
                principal=form.cleaned_data.get("loan_amount")
                tenure=form.cleaned_data.get("tenure")
                roi=form.cleaned_data.get("interest_rate")
                n=tenure*12
                monthly_interest_rate=(roi/100)/12
                emi=(principal*monthly_interest_rate*pow(1+monthly_interest_rate,n)/(pow(1+monthly_interest_rate,n))-1)
                print(emi)

            else:
                print(" form has errors")
            return render(request,"emi.html",{"form":form})






class HelloWorldView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"helloword.html")
    


class Morning(View):
    def get(self,request,*args,**kwargs):
        return render(request,"morning.html")
    
class EveningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"evening.html")   
    

class NoonView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"noon.html")  

class NightView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"night.html")                      
    
class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addition.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        res=int(n1)+int(n2)
        print(res)
        return render(request,"addition.html",{"result":res})

class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        res=int(n1)-int(n2)
        print(res)
        return render(request,"sub.html",{"result":res})
    
class DivisionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"div.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        res=int(n1)/int(n2)
        print(res)
        return render(request,"div.html",{"result":res})
    
class ProductView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"product.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        res=int(n1)*int(n2)
        print(res)
        return render(request,"product.html",{"result":res})
    
class CubeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"cube.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        res=int(n1)*int(n1)*int(n1)
        print(res)
        return render(request,"cube.html",{"result":res})
    

class LeapYearView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"leapyear.html")
    def post(self,request,*args,**kwargs):
        year=int(request.POST.get("year"))

        if year %100==0 and year %400==0 or year %100!=0 and year %4==0:
            result="Leap year"
        else:
            result="not Leap year"
        return render(request,"leapyear.html",{"out":result})

class LongestWordView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"lword.html")
    def post(self,request,*args,**kwargs):
        words=request.POST.get("words").split(" ")
        result=max(words,key=lambda w:len(w))
        return render(request,"lword.html",{"out":result})
    
class ValidBracketParanthView(View):
    def post(self,request,*args,**kwargs):
        return render (request,"valid_brackets.html")
    def get(self,request,*args,**kwargs):
        bracket=request.POST.get("valid")






class ReapeatCharView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"repeatchar.html")
    def post(self,request,*args,**kwargs):
        word=request.POST.get("repeat")
        wc={}
        for ch in word:
            if ch in wc:
                wc[ch]+=1 
            else:
                wc[ch]=1 
        print(wc)
        return render(request,"repeatchar.html")       
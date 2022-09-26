from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
e=''
pwd=''

# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Qwerty1@",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="F_name":
                fn=value
            if key=="L_name":
                ln=value
            if key=="Sex":
                s=value
            if key=="Email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup.html')
from tkinter import *

operator=""
def btnClick(num):
    global operator
    operator+=str(num)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set(operator)

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal=Tk()
cal.title('CALCULATOR')
text_Input=StringVar()
textDisplay=Entry(cal,textvariable=text_Input,font=('arial',20,'bold'),bg='powder blue',bd=20,justify='right',insertwidth=4).grid(columnspan=4)

btn7=Button(cal,padx=16,bd=10,text='7',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=10,text='8',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=10,text='9',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick(9)).grid(row=1,column=2)
addition=Button(cal,padx=16,bd=10,text='+',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick("+")).grid(row=1,column=3)

#-----------------------------------------------------------------------------------------------------------------------------------------------

btn4=Button(cal,padx=16,bd=10,text='4',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=10,text='5',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=10,text='6',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick(6)).grid(row=2,column=2)
subtraction=Button(cal,padx=16,bd=10,text='-',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick("-")).grid(row=2,column=3)

#-----------------------------------------------------------------------------------------------------------------------------------------------

btn1=Button(cal,padx=16,bd=10,text='1',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=10,text='2',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=10,text='3',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick(3)).grid(row=3,column=2)
multiplication=Button(cal,padx=16,bd=10,text='*',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick("*")).grid(row=3,column=3)

#-----------------------------------------------------------------------------------------------------------------------------------------------

btn0=Button(cal,padx=16,bd=10,text='0',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear=Button(cal,padx=16,bd=10,text='C',font=('arial',20,'bold'),fg='black',bg='powder blue',command=btnClearDisplay).grid(row=4,column=1)
btnEquals=Button(cal,padx=16,bd=10,text='=',font=('arial',20,'bold'),fg='black',bg='powder blue',command=btnEqualsInput).grid(row=4,column=2)
Division=Button(cal,padx=16,bd=10,text='/',font=('arial',20,'bold'),fg='black',bg='powder blue',command=lambda:btnClick("/")).grid(row=4,column=3)



cal.mainloop()
#grid=column&row
#place=x&y
#pack=
#padx and pady for the width and height of the button

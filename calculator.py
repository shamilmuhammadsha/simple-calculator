from tkinter import *
def get_num(num):
    current=resultLabel['text']
    new=current+str(num)
    resultLabel.config(text=new)

def clear():
    resultLabel.config(text="")

window=Tk()
window.title("CALCULATOR")
window.geometry("280x400")
window.resizable(0,0)
window.iconbitmap("images/Calculatoricon.ico")
window.configure(background="#34ebc3")

resultLabel=Label(window,text="",bg="#34ebc3",foreground="black")
resultLabel.grid(row=0,columnspan=5,pady=5,padx=10,sticky="w")
resultLabel.config(font=("verdana",25,"bold"))

btn7=Button(window,text="7",bg="#355c58",fg="white",width=5,height=3,command=lambda:get_num(7))
btn7.grid(row=1,column=0)
btn7.config(font=("verdana",14))

btn8=Button(window,text="8",bg="#355c58",fg="white",width=5,height=3,command=lambda:get_num(8))
btn8.grid(row=1,column=1)
btn8.config(font=("verdana",14))

btn9=Button(window,text="9",bg="#355c58",fg="white",width=5,height=3,command=lambda:get_num(9))
btn9.grid(row=1,column=2)
btn9.config(font=("verdana",14))

btnplus=Button(window,text="+",bg="#355c58",fg="white",width=5,height=3)
btnplus.grid(row=1,column=3)
btnplus.config(font=("verdana",14))
#
btn4=Button(window,text="4",bg="#355c58",fg="white",width=5,height=3,command=lambda:get_num(4))
btn4.grid(row=2,column=0)
btn4.config(font=("verdana",14))

btn5=Button(window,text="5",bg="#355c58",fg="white",width=5,height=3,command=lambda:get_num(5))
btn5.grid(row=2,column=1)
btn5.config(font=("verdana",14))

btn6=Button(window,text="6",bg="#355c58",fg="white",width=5,height=3,command=lambda:get_num(6))
btn6.grid(row=2,column=2)
btn6.config(font=("verdana",14))

btnminus=Button(window,text="-",bg="#355c58",fg="white",width=5,height=3)
btnminus.grid(row=2,column=3)
btnminus.config(font=("verdana",14))
##
btn1=Button(window,text="1",bg="#355c58",fg="white",width=5,height=3,command=lambda:get_num(1))
btn1.grid(row=3,column=0)
btn1.config(font=("verdana",14))

btn2=Button(window,text="2",bg="#355c58",fg="white",width=5,height=3,command=lambda:get_num(2))
btn2.grid(row=3,column=1)
btn2.config(font=("verdana",14))

btn3=Button(window,text="3",bg="#355c58",fg="white",width=5,height=3,command=lambda:get_num(3))
btn3.grid(row=3,column=2)
btn3.config(font=("verdana",14))

btnmul=Button(window,text="x",bg="#355c58",fg="white",width=5,height=3)
btnmul.grid(row=3,column=3)
btnmul.config(font=("verdana",14))
###

btn0=Button(window,text="0",bg="#355c58",fg="white",width=5,height=3,command=lambda:get_num(0))
btn0.grid(row=4,column=0)
btn0.config(font=("verdana",14))

btnclear=Button(window,text="C",bg="#355c58",fg="white",width=5,height=3,command=lambda :clear())
btnclear.grid(row=4,column=1)
btnclear.config(font=("verdana",14))

btndiv=Button(window,text="/",bg="#355c58",fg="white",width=5,height=3)
btndiv.grid(row=4,column=2)
btndiv.config(font=("verdana",14))

btneq=Button(window,text="=",bg="#6f8580",fg="white",width=5,height=3)
btneq.grid(row=4,column=3)
btneq.config(font=("verdana",14))


window.mainloop()
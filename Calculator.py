from tkinter import *


window = Tk()
window.geometry('486x640')
window.title('Calculator')
photo = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-calculator-96.png')
window.iconphoto(False,photo)
window.resizable(width=False ,height=False)
window.configure(bg='white')

def btnclick(number):
    global operator 
    operator = operator+ str(number)
    Text_input.set(operator)

def btnclear():
    global operator
    operator = ""
    Text_input.set("")

def btnequal():
    global operator
    sumup = str(eval(operator))
    Text_input.set(sumup)
    operator = ""

operator = ""
Text_input = StringVar()
myframe_1 = Frame(window , bg="light yellow")
myframe_1.grid(row=0 , column=0)


photo_bg = PhotoImage(file = r'C:\Users\User\Desktop\py\Untitled.png')
photo_0 = PhotoImage(file = r'C:\Users\User\Desktop\py\0.png')
photo_1 = PhotoImage(file = r'C:\Users\User\Desktop\py\1.png')
photo_2 = PhotoImage(file = r'C:\Users\User\Desktop\py\2.png')
photo_3 = PhotoImage(file = r'C:\Users\User\Desktop\py\3.png')
photo_4 = PhotoImage(file = r'C:\Users\User\Desktop\py\4.png')
photo_5 = PhotoImage(file = r'C:\Users\User\Desktop\py\5.png')
photo_6 = PhotoImage(file = r'C:\Users\User\Desktop\py\6.png')
photo_7 = PhotoImage(file = r'C:\Users\User\Desktop\py\7.png')
photo_8 = PhotoImage(file = r'C:\Users\User\Desktop\py\8.png')
photo_9 = PhotoImage(file = r'C:\Users\User\Desktop\py\9.png')
photo_equal = PhotoImage(file=r'C:\Users\User\Desktop\py\equal.png')
photo_plus = PhotoImage(file=r'C:\Users\User\Desktop\py\plus.png')
photo_minus = PhotoImage(file=r'C:\Users\User\Desktop\py\minus.png')
photo_mul = PhotoImage(file=r'C:\Users\User\Desktop\py\mul.png')
photo_div = PhotoImage(file=r'C:\Users\User\Desktop\py\div.png')
photo_dot = PhotoImage(file=r'C:\Users\User\Desktop\py\dot.png')
photo_cl = PhotoImage(file=r'C:\Users\User\Desktop\py\cl.png')


Label_bg = Label(window, image=photo_bg)
Label_bg.place(x=2 , y=169)



numentry = Label(myframe_1 , bg="light yellow" , fg ='blue' , text=8 , width=19 ,height=3, relief=SUNKEN, textvariable=Text_input, font=("courler New",30 , "bold"))

numentry.grid(row=0 , column=0 , padx=5)
numentry.bind("")



myframe_2 = Frame(window , bg="light yellow")
myframe_2.grid(row=1 , column=0)


Button_0 = Button(window , image=photo_0 , command=lambda:btnclear(0))
Button_0.place(x=49 , y =510 , height=85 ,width=85)
Button_1 = Button(window , image=photo_1 , command=lambda:btnclick(1))
Button_1.place(x=49 , y =408 , height=85 ,width=85)
Button_2 = Button(window , image=photo_2 , command=lambda:btnclick(2))
Button_2.place(x=151 , y =408 , height=85 ,width=85)
Button_3 = Button(window , image=photo_3 , command=lambda:btnclick(3))
Button_3.place(x=253 , y =408 , height=85 ,width=85)
Button_4 = Button(window , image=photo_4 , command=lambda:btnclick(4))
Button_4.place(x=49 , y =305 , height=85 ,width=85)
Button_5 = Button(window , image=photo_5 , command=lambda:btnclick(5))
Button_5.place(x=151 , y =305 , height=85 ,width=85)
Button_6 = Button(window , image=photo_6 , command=lambda:btnclick(6))
Button_6.place(x=253 , y =305 , height=85 ,width=85)
Button_7 = Button(window , image=photo_7, command=lambda:btnclick(7))
Button_7.place(x=49 , y =202 , height=85 ,width=85)
Button_8 = Button(window , image=photo_8 , command=lambda:btnclick(8))
Button_8.place(x=151 , y =202 , height=85 ,width=85)
Button_9 = Button(window , image=photo_9 , command=lambda:btnclick(9))
Button_9.place(x=253 , y =202 , height=85 ,width=85)
Button_div = Button(window , image=photo_div, command=lambda: btnclick('/'))
Button_div.place(x=356 , y= 202 , height=85 , width=85)
Button_mul = Button(window , image=photo_mul, command=lambda: btnclick('*'))
Button_mul.place(x=356 , y= 304 , height=85 , width=85)
Button_minus = Button(window , image=photo_minus, command=lambda: btnclick('-'))
Button_minus.place(x=356 , y= 406 , height=85 , width=85)
Button_plus = Button(window , image=photo_plus, command=lambda: btnclick('+'))
Button_plus.place(x=356 , y= 509 , height=85 , width=85)
Button_equal = Button(window , image=photo_equal, command=lambda: btnequal())
Button_equal.place(x=254 , y= 509 , height=85 , width=85)
Button_dot = Button(window , image=photo_dot , command=lambda: btnclick('.'))
Button_dot.place(x=150 , y= 509 , height=85 , width=85)
Button_cl = Button(window , image=photo_cl, command=lambda: btnclear())
Button_cl.place(x=378 , y= 145, height=28 , width=40)
window.mainloop()
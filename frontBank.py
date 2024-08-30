from tkinter import  *

import backend

window = Tk()


def clear_list():
    list1.delete(0,END)

def fill_list(banks):
    for bank in banks:
        list1.insert(END, bank)


window.geometry("600x600")
window.title("bank")
photo = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-dollar-coin-64.png')
window.iconphoto(False, photo)
window.resizable(width=False, height=False)
photo_bg = PhotoImage(file=r'C:\Users\User\Desktop\py\Finance-amico_11zon.png')


photo_add = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-add-64.png')

photo_search = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-search-64.png')

photo_close = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-close-sign-64.png')
photo_view = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-eye-64.png')

photo_update = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-update-64.png')
photo_delete = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-close-64.png')
Label_bg = Label(window, image=photo_bg)
Label_bg.place(x=2, y=0)

label1 = Label(window, text="نام و نام خانوادگی")
label1.place(x=465 ,y=30)

label2 = Label(window, text="کد ملی")
label2.place(x=490 ,y=70)

label1 = Label(window, text="شماره حساب")
label1.place(x=480 , y=110)
label1 = Label(window, text="تلفن")
label1.place(x= 495 ,y=150)



Name_text = StringVar()
e1 = Entry(window, textvariable=Name_text)
e1.place(x=450,y=50)

Code_text = StringVar()
e2 = Entry(window, textvariable=Code_text)
e2.place(x=450 , y=90)

Number_text = StringVar()
e3 = Entry(window, textvariable=Number_text)
e3.place(x=450 , y=130)

Phone_text = StringVar()
e4 = Entry(window, textvariable=Phone_text)
e4.place(x=450 ,y=170)

list1 = Listbox(window, height=5, width=40)
list1.place(x= 40 , y=70)

sb1 = Scrollbar(window)
sb1.place(x=20, y=85)
list1.config(yscrollcommand = sb1.set)
sb1.config(command = list1.yview)

# global selected_bank


# def get_selected_row(event):
#     try:
#         global select_tuple
#         index=list1.curselection()
#         select_tuple=list1.get(index)
#         e1.delete(0,END)
#         e1.insert(END, select_tuple[0])
#         e2.delete(0,END)
#         e2.insert(END, select_tuple[1])
#         e3.delete(0,END)
#         e3.insert(END, select_tuple[2])
#         e4.delete(0,END)
#         e4.insert(END, select_tuple[3])
#     except IndexError:
#         pass




# list1.bind("<<listboxSelect>>", get_selected_row)

def view_command():
    clear_list()
    banks = backend.view()
    fill_list(banks)
d1 = Button(window, image=photo_view, command=lambda:view_command())
d1.place(x=434, y=506)

def search_command():
    clear_list()
    banks = backend.search(Name_text.get(), Code_text.get(), Number_text.get(), Phone_text.get())
    fill_list(banks)
d2 = Button(window, image=photo_search, command=lambda:search_command())
d2.place(x=504, y=506)


def add_command():
    backend.insert(Name_text.get() , Code_text.get() , Number_text.get() , Phone_text.get())
    view_command()

d3 = Button(window , image=photo_add , command=lambda:add_command())
d3.place(x=434, y=436)

# def update_command():
#     backend.update(select_tuple[0], Name_text.get(), Code_text.get(), Number_text.get(), Phone_text.get())
#     view_command()
#
# d4 = Button(window, image=photo_update, command=lambda:update_command())
# d4.place(x=428, y=500)

# def delete_command():
#     backend.delete(selected_bank[0])
#     view_command()


d5 = Button(window, image=photo_delete, command=lambda:list1.delete(0,'end'))
d5.place(x=504, y=436)

d6 = Button(window, image = photo_close, command=lambda: window.destroy())
d6.place(x=25, y=506)

window.mainloop()

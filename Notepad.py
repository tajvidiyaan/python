from tkinter import *
from tkinter import filedialog


window = Tk()
window.title('Notepad')
photo = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-notepad-96.png')
window.iconphoto(False,photo)
window.geometry('600x600')
window.resizable(width=False , height=False)



def new():
    Text_box.delete(1.0 , END)

def open():
    file = filedialog.askopenfile(mode="r" , filetypes=[('text file',"txt")])
    if file is not None:
        content = file.read()

    Text_box.insert(INSERT,content)

def save():
    open = filedialog.asksaveasfile(mode='w' , defaultextension='.txt')
    Text = str(Text_box.get(1.0 , END))
    open.write()
    open.close()


menubar = Menu(window)
window.config(menu = menubar , bg ='green')
file_menu = Menu(menubar ,tearoff=0)
menubar.add_cascade(label='File' , menu=file_menu)
# menubar.add_cascade(label="File" , menu= file_menu)

file_menu.add_command(label='New',command= new)
file_menu.add_command(label='Open',command= open)
file_menu.add_command(label='Save', command= save)
file_menu.add_separator()
file_menu.add_command(label='Exit' , command=window.destroy)
help_menu = Menu(menubar , tearoff= 0)
menubar.add_cascade(label="Help" , menu= help_menu)
help_menu.add_cascade(label='Help')
help_menu.add_command(label='about')


Text_box = Text(window , height='38', width= '75' ,wrap=WORD)
Text_box.place(x=0 , y=0)


window.mainloop()
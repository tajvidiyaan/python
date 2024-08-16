import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import PhotoImage


current_color = "black"



def start(event):
    global prev_x , prev_y
    prev_x , prev_y = event.x , event.y
    print(prev_x , prev_y)


def paint(event):
    global prev_x , prev_y
    x , y = event.x , event.y
    if prev_x and prev_y:
        canvas.create_line(prev_x , prev_y , x , y , fill=current_color , width=2)
    prev_x , prev_y = x , y


def color():
    global current_color
    color = askcolor()[1]
    if color:
        current_color = color



def clear():
    canvas.delete("all")
    

    
window = tk.Tk()
window.title('Paint')
photo = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-color-palette-96.png')
window.iconphoto(False,photo)



btn_frame = tk.Frame(window)
btn_frame.pack(padx=5 , pady=5)

photo_color = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-paint-palette-96.png')
color_btn = tk.Button(btn_frame , text="select color" , font=("Arial" , 15) , image=photo_color , command= color)
color_btn.grid(row=0 , column=0 , padx=5)


clear_color = PhotoImage(file=r'C:\Users\User\Desktop\py\icons8-broom-96.png')
clear_btn = tk.Button(btn_frame , text="clear" , font=("Arial" , 15) , image= clear_color , command=clear)
clear_btn.grid(row=0 , column=1 , padx=5)

canvas = tk.Canvas(window , bg="white" , width=900 , height=600)
canvas.pack(padx=5 , pady=5)


canvas.bind("<Button-1>" , start)
canvas.bind("<B1-Motion>" , paint)



window.mainloop()
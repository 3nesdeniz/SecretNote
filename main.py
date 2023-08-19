import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from base64 import b64encode, b64decode

def custom_encrypt(message, key):
    encrypted = []
    for i, char in enumerate(message):
        key_char = key[i % len(key)]
        encrypted_char = chr((ord(char) + ord(key_char)) % 256)
        encrypted.append(encrypted_char)
    return ''.join(encrypted)

def custom_decrypt(encrypted, key):
    decrypted = []
    for i, char in enumerate(encrypted):
        key_char = key[i % len(key)]
        decrypted_char = chr((ord(char) - ord(key_char)) % 256)
        decrypted.append(decrypted_char)
    return ''.join(decrypted)



Window = Tk()
Window.title("Secret Massage")
Window.minsize(width="400",height="800")

width=400
height = 800
x = 1920/2 -400/2
y = 1080/2 - 800/2
screen_width = Window.winfo_screenwidth()  # Width of the screen
screen_height = Window.winfo_screenheight() # Height of the screen
Window.geometry('%dx%d+%d+%d' % (width, height, x, y))









# Load the image
image=Image.open('indir.png')

# Resize the image in the given (width, height)
img=image.resize((100, 100))

# Conver the image in TkImage
my_img=ImageTk.PhotoImage(img)

# Display the image with label
label=Label(Window, image=my_img)
label.pack()
#Label
title_2= tkinter.Label(text="Enter Your Title",font=("Italic",13,"bold"))
title_2.place(x=140,y=170)
#ENTRY
title = tkinter.Entry(width=30)
title.place(x=100+12,y=200)

#TEXT
text_1=tkinter.Text(width=30,height=20)
text_1.place(x=84,y=250)

#Label2
title_3= tkinter.Label(text="Enter Your Text",font=("Italic",13,"bold"))
title_3.place(x=139,y=220)

#Entry2
master_key=tkinter.Entry(width=30,font=("Arial 11"))
master_key.place(x=86,y=620)

#Text
text_2=tkinter.Label(text="Enter Master Key",width=30,font=("Italic",13,"bold"))
text_2.place(x=55,y=600)
#FONKS

def get_all():
    values_of_test = text_1.get("1.0",END)
    key = master_key.get()
    maintitle=title.get()

    if len(values_of_test)==0 or len(key)==0 or len(maintitle)==0:
        messagebox.showerror(title="Empty Index",message="Please Enter All Index")

    else:

        values_of_test = custom_encrypt(values_of_test,key)

        with open("mysecret.txt","a") as data_file:
            data_file.write(f"\nTitle:{maintitle}\nText:{values_of_test}")

def dece():
    values_of_test = text_1.get("1.0", END)
    key = master_key.get()
    maintitle = title.get()
    if len(values_of_test)==0 or len(key)==0 or len(maintitle)==0:
        messagebox.showerror(title="Empty Index",message="Please Enter All Index")

    else:
        dec =custom_decrypt(values_of_test,key)
        text_1.delete("1.0",END)
        title.delete(0,END)
        master_key.delete(0,END)
        text_1.insert("1.0",dec)

#Button1

button_1=tkinter.Button(text="Save & Encryp",background="#FF5D5D",command=get_all)
button_1.place(x=162,y=650)
#button2

button_2=tkinter.Button(text="Decrypt",background="#7FFF5D",command=dece)
button_2.place(x=179,y=690)


Window.mainloop()

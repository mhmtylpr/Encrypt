import customtkinter
import base64
import os
from PIL import Image
from tkinter import messagebox
import random

PASSWORD="1"
FLEX_CHARAXTER="QWERTYYUIOPĞÜİŞLKJHGFDSAÇ<ÖZCNBVB,.!'^+%&//()=?"

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.geometry("400x600")
app.title("Encrypt")
app.maxsize(width=400,
            height=600)

def encrypte():

    if pass_entry.get()==PASSWORD:
        new_File = open(f"{entry.get()}.txt,", "a")
        text = textBox.get("1.0", "end-1c")
        bytes = text.encode("utf-8")
        base_encrypte = base64.b64encode(bytes)
        base_encrypte = base_encrypte.decode("utf-8")
        new_File.write(base_encrypte)
        entry.delete(0,"end")
        textBox.delete("1.0","end")
        pass_entry.delete(0,"end")
    else:
        message=messagebox.showinfo("Hata","Şifreyi Giriniz!!!")

def decrypte():
    try:
        if pass_entry.get()==PASSWORD:
            text = textBox.get("1.0", "end-1c")
            bytes = text.encode("utf-8")
            base_encrypte = base64.b64decode(bytes)
            base_encrypte = base_encrypte.decode("utf-8")
            textBox.delete("1.0","end")
            textBox.insert("0.0",base_encrypte)
            pass_entry.delete(0,"end")

        else:
            rest = random.randint(0, 20)
            rest = int(rest)
            text = textBox.delete("1.0", "end-1c")
            texxt = " "
            pass_entry.delete(0,"end")
            for i in range(1, rest):
                index = random.randint(2, 12)
                texxt += FLEX_CHARAXTER[index]
            textBox.insert("0.0",texxt)
    except:
        messagebox.showinfo("Hata","Çifreli bir metin giriniz...")

frame=customtkinter.CTkFrame(master=app,
                             width=390,
                             height=590)
frame.place(relx=0.5,
            rely=0.5,
            anchor=customtkinter.CENTER)
image_path = os.path.join(os.path.dirname(__file__), "Nuclear-Sign-PNG-File.png")
image = customtkinter.CTkImage(light_image=Image.open(image_path),
                               size=(50, 52))
image_label = customtkinter.CTkLabel(master=frame,
                                     image=image,
                                     text=" ")
image_label.place(relx=0.5,
                  rely=0.1,
                  anchor=customtkinter.CENTER)
entry=customtkinter.CTkEntry(master=frame,
                             width=200,
                             placeholder_text="Dosya adı",
                             font=("Microsoft YaHei",14,"normal"))
entry.place(relx=0.5,
            rely=0.2,
            anchor=customtkinter.CENTER)
textBox=customtkinter.CTkTextbox(master=frame,
                                 width=380,
                                 height=300,
                                 font=("Microsoft YaHei",14,"normal"))
textBox.place(relx=0.5,
              rely=0.5,
              anchor=customtkinter.CENTER)
pass_entry=customtkinter.CTkEntry(master=frame,
                                  width=200,
                                  placeholder_text="Şifreniz")
pass_entry.place(relx=0.5,
                 rely=0.8,
                 anchor=customtkinter.CENTER)
button_encrypt=customtkinter.CTkButton(master=frame,
                                       text="Encrypt",
                                       width=100,
                                       command=encrypte
                                       )
button_encrypt.place(relx=0.5,
                     rely=0.86,
                     anchor=customtkinter.CENTER)
button_decrypte=customtkinter.CTkButton(master=frame,
                                        text="Decrypt",
                                        width=100,
                                        fg_color="green",command=decrypte)
button_decrypte.place(relx=0.5,
                      rely=0.93,
                      anchor=customtkinter.CENTER)
app.mainloop()
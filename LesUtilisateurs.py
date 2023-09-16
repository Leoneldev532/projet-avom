import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
import os

# window 
root = ctk.CTk(fg_color="#13121F")
root.title('customtkinter app')
root.minsize(500,500)
width = 1000
height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

root.geometry(f"{width}x{height}+{x}+{y}")

def button_function():
    print("button pressed")



header = tk.Frame(root,bg="#0E0E18")
header.pack(side="left")
header.configure(height=height,width=300)

body = tk.Frame(root,bg="#ccc")
# body.grid(row=1,column=5,columnspan=3)
body.configure(height=height,width=800)


Logoplace = ctk.CTkLabel(header,width=300,height=45,text="recovery     ",font=("candara",25,"bold"),padx=14,pady=25)
Logoplace.grid(row=0,column=0)


btnplace = ctk.CTkFrame(header,width=300,height=240,bg_color="#13121F",fg_color="#13121F")
btnplace.grid(row=1,column=0,padx=14,pady=50)


utilisateurbtn = ctk.CTkButton(btnplace,width=300,height=55,corner_radius=30,text="utilisateurs",fg_color="#2B53E9",
                               font=("candara",17,"bold"),hover_color="#13124F",command=button_function)
utilisateurbtn.grid(row=1,column=0)


historiquebtn = ctk.CTkButton(btnplace,width=300,corner_radius=35, height=55,
hover_color="#13154F",text="historique",fg_color="#2B53E9",font=("candara",17,"bold"))
historiquebtn.grid(row=2,column=0,pady=14)  

Donneesbtn = ctk.CTkButton(btnplace,width=300,height=55,corner_radius=35, text="donnees",
hover_color="#13154F",fg_color="#2B53E9",font=("candara",17,"bold"))
Donneesbtn.grid(row=4,column=0)

sauvagardebtn = ctk.CTkButton(btnplace,width=300,height=55,corner_radius=35, text="sauvegarde",
hover_color="#13154F",fg_color="#2B53E9",font=("candara",17,"bold"))
sauvagardebtn.grid(row=5,column=0,pady=14)

recuperationbtn = ctk.CTkButton(btnplace,width=300,height=55,corner_radius=35, text="recuperation"
,hover_color="#13504F",fg_color="#2B53E9",font=("candara",17,"bold"))
recuperationbtn.grid(row=6,column=0,pady=14)

deconnexionbtn = ctk.CTkButton(btnplace,width=300,height=55,corner_radius=35, text="déconnexion"
,fg_color="#2B53E9",font=("candara",17,"bold"))
deconnexionbtn.grid(row=7,column=0,pady=14)



content = tk.Frame(root,bg="#1A1A38")
content.pack(side="left")
content.configure(height=height,width=700,pady=12,padx=28)


NameInterFace = ctk.CTkLabel(content,text="Les utilisateurs", font=("candara", 32,"bold"))
NameInterFace.grid(row=0,column=0,pady=10)

entetetableau = ctk.CTkFrame(content,bg_color="#1A1A38",height=60,width=600,border_width=15, border_color="#08082A",
                     corner_radius=8,fg_color="#08082A")
entetetableau.grid(row=1,column=0,columnspan=3)

Nomtxt = ctk.CTkLabel(entetetableau,text="Nom:",width=200,compound="left",anchor="w")
Nomtxt.grid(row=0,column=0,pady=4,padx=10)

Postetxt = ctk.CTkLabel(entetetableau,text="Poste:",width=200,compound="left",anchor="w")
Postetxt.grid(row=0,column=1,pady=4)

Actiontxt = ctk.CTkLabel(entetetableau,text="Action:",width=200,compound="left",anchor="w")
Actiontxt.grid(row=0,column=2,pady=4)


def addLigneUtilisateurs(nom,poste,numeroLigne):
    NomUser =  ctk.CTkLabel(entetetableau,text=nom,width=200,compound="left",anchor="w")
    NomUser.grid(row=numeroLigne,column=0,pady=4)

    PosteUser =  ctk.CTkLabel(entetetableau,text=poste,width=200,compound="left",anchor="w")
    PosteUser.grid(row=numeroLigne,column=1,pady=4)

    EditUser =  ctk.CTkButton(entetetableau,text=poste,width=200,compound="left",anchor="w")
    PosteUser.grid(row=numeroLigne,column=2,pady=4)
    
    
addLigneUtilisateurs("nom","poste555",2)




root.mainloop()

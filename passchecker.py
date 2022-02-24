#from AlgorytmPass import Algorytm
from tkinter import *
import os.path
import datetime
import csv
import secrets
import string





if os.path.exists("Hasla.csv"):
    pass
else:
    f = open("Hasla.csv", "w")

 

root = Tk()
print("Logs:")
root.title("Password Generator")
currenttime = datetime.datetime.now().replace(microsecond=0)
currenttimecsv = (f"Program opened at {currenttime}").split(",")
with open(r'Hasla.csv', "a") as f:
        writer = csv.writer(f)
        writer.writerow(currenttimecsv)
root.geometry("600x600")

e = Entry(root, width=600, borderwidth=2 )
e.pack()
e.insert(0, "Lenght of the password:")


def Exit():
    root.destroy()
    print("You have closed the program!")
r = StringVar()
Radiobutton(root, text= "Password without numbers", variable=r,value = "Pass without numbers").pack()
Radiobutton(root, text="Password without alphabet", variable=r, value = "Pass without alphabet").pack()
Radiobutton(root, text="Password without special characters", variable=r, value = "Pass without special characters").pack()
Radiobutton(root, text="Password with anything", variable=r, value = "Pass with everything").pack()
def Generate():
    Label(root, text = f"You choose the option: {str(r.get())}").pack()
    if str(r.get()) == "Pass without numbers":
            newWindow = Toplevel(root)
            newWindow.title("Pass")
            newWindow.geometry("200x200")
            try:
                for i in range(5):
                    alphabet = string.ascii_letters + string.punctuation
                    Pass = ''.join(secrets.choice(alphabet) for i in range(int(e.get())))
                    label = Label(newWindow, text = f"Password:{Pass}")
                    label.pack()
                    print("You just generated a password!")
            except(ValueError):
                print("Something wrong happened!")
                e.delete(0, END)
                e.insert(0, "Please, try again!")
                newWindow.destroy()


    elif str(r.get()) == "Pass without alphabet":
            newWindow = Toplevel(root)
            newWindow.title("Pass")
            newWindow.geometry("200x200")
            try:
                for i in range(5):
                    alphabet = string.digits + string.punctuation
                    Pass = ''.join(secrets.choice(alphabet) for i in range(int(e.get())))
                    label = Label(newWindow, text = f"Password: {Pass}")
                    label.pack()
                    print("You just generated a password!")
            except(ValueError):
                print("Something wrong happened!")
                e.delete(0, END)
                e.insert(0, "Please, try again!")
                newWindow.destroy()
    elif str(r.get()) =="Pass without special characters":
            newWindow = Toplevel(root)
            newWindow.title("Pass")
            newWindow.geometry("200x200")
            try:
                for i in range(5):
                    alphabet = string.ascii_letters + string.digits 
                    Pass = ''.join(secrets.choice(alphabet) for i in range(int(e.get())))
                    label = Label(newWindow, text = f"Password: {Pass}")
                    label.pack()
                    print("You just generated a password!")
            except(ValueError):
                print("Something wrong happened!")
                e.delete(0, END)
                e.insert(0, "Please, try again!")
                newWindow.destroy()

    elif str(r.get()) =="Pass with everything":
            newWindow = Toplevel(root)
            newWindow.title("Pass")
            newWindow.geometry("200x200")
            try:
                for i in range(5):
                    alphabet = string.ascii_letters + string.digits + string.punctuation 
                    Pass = ''.join(secrets.choice(alphabet) for i in range(int(e.get())))
                    label = Label(newWindow, text = f"Password: {Pass}")
                    label.pack()
                    print("You just generated a password!")
            except(ValueError):
                print("Something wrong happened!")
                e.delete(0, END)
                e.insert(0, "Please, try again!")
                newWindow.destroy()
def Algorytm():
    global newWindow
    global e1
    global liczby, cyfry, spacje
    lenght = len(e1.get()) # dlugosc hasla
    label1 = label = Label(newWindow, text = f"Lenght of the pass: {lenght}")
    label1.pack()
    liczby = sum(n.isdigit() for n in e1.get()) #sprawdza z ilu liczb sklada sie haslo
    cyfry = sum(n.isalpha() for n in e1.get()) #sprawdza z ilu cyfr sklada sie haslo
    label2 = Label(newWindow, text = f"Amount of numbers {liczby}")
    label2.pack()
    label3 = Label(newWindow, text = f"Amount of letters: {cyfry}")
    label3.pack()
    spacje = sum(n.isspace() for n in e1.get()) #sprawdza z ilu slow sklada sie haslo
    label4 = Label(newWindow, text = f"Amount of spaces: {spacje }")
    label4.pack()
   




def PassCheck():
    global newWindow
    global e1
    newWindow = Toplevel(root)
    newWindow.title("Pass Checker")
    newWindow.geometry("600x600")
    e1 = Entry(newWindow, width=600, borderwidth=2 )
    e1.pack()
    e1.insert(0, "Write down your pass:")
    Button(newWindow,text = "Start checking!", padx = 100, pady = 20, command = Checker).pack()

def Checker(): 
        
        Algorytm()
        if len(e1.get()) >= 20:
            label2 = Label(newWindow, text = "Overall grade: Excelent!")
            label2.pack()
            print("You just checked your password!")
      
        elif len(e1.get()) >= 15:
            label2 = Label(newWindow, text = "Overall grade: Great!")
            label2.pack()
            print("You just checked your password!")
        
        elif len(e1.get()) >= 10:
            label2 = Label(newWindow, text = "Overall grade: Good!")
            label2.pack()
            print("You just checked your password!")
        
        else:
            label2 = Label(newWindow, text = "Overall grade: Bad!")
            label2.pack()
            print("You just checked your password!")
        if len(e1.get()) ==0:
            print("An unexpected error has occured!")
            newWindow.destroy()

       




Generate = Button(root, text="Generate Password",background = "RED", foreground="white", padx = 101, pady = 20, command=Generate).pack()
Checking = Button(root, text="Password checker",background = "ORANGE", foreground="white", padx = 104, pady = 20, command=PassCheck).pack()
Exit = Button(root, text="Exit!",background = "GREEN", foreground="white", padx = 140, pady = 20,  command=Exit).pack()





root.mainloop()
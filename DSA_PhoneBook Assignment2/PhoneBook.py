from tkinter import *
import csv
from tkinter import messagebox

phonelist = []

# Time complexity for a WriteCSVFile function is O(n)
# This means that the running time increases at most linearly with the size of the input.
# We know that the CSV-reader creates an iterated over.
# All CSV-reader does is create access to the file to be read further along in the script. This should be O(1)
# This is because its constant time operation.
# The CSV-writer writes the the data to the file.
# This should be O(n) because it is a linear time operation.
# This should be O(n) because it is a linear time operation.

def ReadCSVFile():
    global header
    with open('StudentData.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            phonelist.append(row)
    set_select()
    print(phonelist)

# This time complexity of using a try-except block is O(n).
# This means if any exception throws, the exception handler took more time than it version of the code.


def WriteInCSVFile(phonelist):
    try:
        with open('StudentData.csv', 'w', newline='') as csv_file:
            writeobj = csv.writer(csv_file, delimiter=',')
            writeobj.writerow(header)
            for row in phonelist:
                writeobj.writerow(row)
    except PermissionError:
        print("Oooops, something went wrong.Please Try Agin!!")

# Time complexity for a whichSelected function is O(1)
# This means that it takes a constant time, like 14 nanoseconds, or three minutes no matter.
# The amount of data in the set

def WhichSelected():
    print("hello", len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])

# Time complexity for a AddDetail function is O(1)
# meaning we have a constant time for add detail to the phonebook.
def AddDetail():
    if E_First_name.get() != "" and E_last_name.get() != "" and E_contact.get() != "":
        phonelist.append([E_First_name.get() + ' ' + E_last_name.get(), E_contact.get()])
        print(phonelist)
        WriteInCSVFile(phonelist)
        set_select()
        EntryReset()
        messagebox.showinfo("Succesfully Added New Contact")

    else:
        messagebox.showerror("Error", "Please fill in the information")

# Time complexity for a UpdateDetail function is O(1)
# There is a constant time period for the deatil to be updated in the phone book.
def UpdateDetail():
    if E_First_name.get() and E_last_name.get() and E_contact.get():
        phonelist[WhichSelected()] = [E_First_name.get() + ' ' + E_last_name.get(), E_contact.get()]
        WriteInCSVFile(phonelist)
        messagebox.showinfo("Contact Sucessfully Updated")
        EntryReset()
        set_select()

    elif not (E_First_name.get()) and not (E_last_name.get()) and not (E_contact.get()) and not (
            len(select.curselection()) == 0):
        messagebox.showerror("Error", "Please fill the information")

    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name and \n press Display button")
        else:
            message1 = """To Display all information \n 
						  select row and press Display button\n.
						  """
            messagebox.showerror("Error", message1)

# Time complexity for a Entryreset function is O(1)
# with a constant time that data is entered in the entry box.
def EntryReset():
    E_First_name_var.set('')
    E_last_name_var.set('')
    E_contact_var.set('')

# Time complexity for a DeleteEntry function is O(1)
# The amount of the data in the set.
def DeleteEntry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'You Want to Delete Contact\n Which you selected')
        if result == True:
            del phonelist[WhichSelected()]
            WriteInCSVFile(phonelist)
            set_select()
    else:
        messagebox.showerror("Error", 'Please select the Contact')


def DisplayEntry():
    try:
        name, phone = phonelist[WhichSelected()]
        print(name.split(' '))
        E_First_name_var.set(name.split()[0])
        E_last_name_var.set(name.split()[1])
        E_contact_var.set(phone)
    except TypeError:
        print("An error occured, please try again!!")

# Time complexity for a set_select function is O(n)
# means that it takes a constant time, like 14 nanoseconds, or three minutes no matter.
# the amount of data in the set
def set_select():
    phonelist.sort(key=lambda record: record[1])
    select.delete(0, END)
    i = 0
    for name, phone in phonelist:
        i += 1
        select.insert(END, f"{i}  |    {name}   |   {phone}")


window = Tk()

Frame1 = LabelFrame(window, text="Enter the Contact Detail")
Frame1.grid(padx=15, pady=15)

Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0, column=0, padx=15, pady=15)

l_First_name = Label(Inside_Frame1, text="FirstName")
l_First_name.grid(row=0, column=0, padx=5, pady=5)
E_First_name_var = StringVar()

E_First_name = Entry(Inside_Frame1, width=30, textvariable=E_First_name_var)
E_First_name.grid(row=0, column=1, padx=5, pady=5)

l_last_name = Label(Inside_Frame1, text="LastName")
l_last_name.grid(row=1, column=0, padx=5, pady=5)
E_last_name_var = StringVar()
E_last_name = Entry(Inside_Frame1, width=30, textvariable=E_last_name_var)
E_last_name.grid(row=1, column=1, padx=5, pady=5)

l_contact = Label(Inside_Frame1, text="Contact")
l_contact.grid(row=2, column=0, padx=5, pady=5)
E_contact_var = StringVar()
E_contact = Entry(Inside_Frame1, width=30, textvariable=E_contact_var)
E_contact.grid(row=2, column=1, padx=5, pady=5)

Frame2 = Frame(window)
Frame2.grid(row=0, column=1, padx=15, pady=15, sticky=E)

Add_button = Button(Frame2, text="Add Detail", width=15, bg="#008000", fg="#FFFFFF", command=AddDetail)
Add_button.grid(row=0, column=0, padx=8, pady=8)

Update_button = Button(Frame2, text="Update Detail", width=15, bg="#008000", fg="#FFFFFF", command=UpdateDetail)
Update_button.grid(row=1, column=0, padx=8, pady=8)

Reset_button = Button(Frame2, text="Reset", width=15, bg="#008000", fg="#FFFFFF", command=EntryReset)
Reset_button.grid(row=2, column=0, padx=8, pady=8)


DisplayFrame = Frame(window)
DisplayFrame.grid(row=1, column=0, padx=15, pady=15)

scroll = Scrollbar(DisplayFrame, orient=VERTICAL)
select = Listbox(DisplayFrame, yscrollcommand=scroll.set, font=("Arial Bold", 10), bg="#282923", fg="#E7C855", width=40,
                 height=10, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
select.grid(row=0, column=0, sticky=W)
scroll.grid(row=0, column=1, sticky=N + S)


ActionFrame = Frame(window)
ActionFrame.grid(row=1, column=1, padx=15, pady=15, sticky=E)

Delete_button = Button(ActionFrame, text="Delete", width=15, bg="#D20000", fg="#FFFFFF", command=DeleteEntry)
Delete_button.grid(row=0, column=0, padx=5, pady=5, sticky=S)

Displaybutton = Button(ActionFrame, text="Display", width=15, bg="#000080", fg="#FFFFFF", command=DisplayEntry)
Displaybutton.grid(row=1, column=0, padx=5, pady=5)



ReadCSVFile()

window.mainloop()


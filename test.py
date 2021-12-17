import csv
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
# variables :


# Home app settings :
home = Tk()
home.geometry('900x700+300+50')
home.config(background='#000')
home.title('Home')
home.resizable(False, False)

# Variables :
datas = []
dic = dict({})

Name = StringVar()
Number = StringVar()
ids = []

with open('my_contacts.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    reader = csv.DictReader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(reader)
    datas = list_of_rows


# Tabs Functions :
ajout_Frame = Frame(width='900', height='700', bg='#3d405b')
contact_Frame = Frame(width='900', height='700', bg='#3d405b')
select = Listbox(ajout_Frame, height=12, bg='#fff', width=50)
fields = []

# functions :


def update_book():
    global img
    select.delete(0, END)
    for n in datas:
        for key, value in n.items():
            if key == "Name":
                select.insert(END, value)
                ids.append(value)
                break


# def add():
#     dic = {
#         "Name": Name.get(),
#         "Number": Number.get(),
#         "Address": addressEntry.get(1.0, "end-1c"),
#     }
#     datas.append(dic)
#     print(datas)
#     update_book()


def Scankey(event):
    select.delete(0, END)
    data = ids
    val = event.widget.get()
    print(val)

    if val != '':
        data = []
        for n in datas:
            for key, value in n.items():
                if key == "Name":
                    if val.lower() in value.lower():
                        data.append(value)
        select.delete(0, END)
        for item in data:
            if item in ids:
                # select.delete(END, item)
                select.insert(END, item)
    else:
        update_book()


def delete():
    selected = select.get(ANCHOR)
    for e in datas:
        for key, value in e.items():
            if key == "Name":
                if value == selected:
                    index = datas.index(e)
    for i in range(len(datas)):
        if datas[i]["Name"] == selected:
            del datas[i]
            break
    update_book()
    update_file()


def update_file():
    filename = 'my_contacts.csv'
    fields = ["Name", "Number", "Address", "img"]
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in datas:
            writer.writerow(item)


def containe():
    def ContactTab():
        def view(event):
            selected = select.get(ANCHOR)
            addressEntry.delete(1.0, "end")
            for e in datas:
                for key, value in e.items():
                    if key == "Name":
                        if value == selected:
                            selected_dic = e
                            break
            for key, value in selected_dic.items():
                if key == "Name":
                    Name.set(value)
                if key == "Number":
                    Number.set(value)
                if key == "Address":
                    addressEntry.insert(1.0, value)

        def modifier():
            selected = select.get(ANCHOR)
            for e in datas:
                for key, value in e.items():
                    if key == "Name":
                        if selected == value:
                            selected_dic = e
                            index = datas.index(e)
                            break
            selected_dic = {}
            selected_dic = {
                "Name": Name.get(),
                "Number": Number.get(),
                "Address": addressEntry.get(1.0, "end-1c")
            }
            datas[index] = selected_dic
            update_book()
            update_file()

    def ajoutTab():
        def update_book():
            select.delete(0, END)
            for n in datas:
                for key, value in n.items():
                    if key == "Name":
                        select.insert(END, value)
                        ids.append(value)
                        break

        def delete():
            selected = select.get(ANCHOR)
            for e in datas:
                for key, value in e.items():
                    if key == "Name":
                        if value == selected:
                            index = datas.index(e)
            for i in range(len(datas)):
                if datas[i]["Name"] == selected:
                    del datas[i]
                    break
            update_book()
            update_file()

        def modifier():
            selected = select.get(ANCHOR)
            for e in datas:
                for key, value in e.items():
                    if key == "Name":
                        if selected == value:
                            selected_dic = e
                            index = datas.index(e)
                            break
            selected_dic = {}
            selected_dic = {
                "Name": Name.get(),
                "Number": Number.get(),
                "Address": addressEntry.get(1.0, "end-1c")
            }
            datas[index] = selected_dic
            update_book()
            update_file()

        def add():

            dic = {
                "Name": Name.get(),
                "Number": Number.get(),
                "Address": addressEntry.get(1.0, "end-1c"),
            }
            f_types = [('Jpg Files', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            fields.append(filename)
            dic["img"] = filename
            datas.append(dic)
            print(datas)
            update_book()
            update_file()

        def reset():
            Name.set('')
            Number.set('')
            addressEntry.delete(1.0, "end")

        def view(event):
            selected = select.get(ANCHOR)
            nameValue = ''
            numberValue = ''
            addressValue = ''
            addressEntry.delete(1.0, "end")
            for e in datas:
                for key, value in e.items():
                    if key == "Name":
                        if value == selected:
                            selected_dic = e
                            break
            for key, value in selected_dic.items():
                if key == "Name":
                    Name.set(value)
                if key == "Number":
                    Number.set(value)
                if key == "Address":
                    addressEntry.insert(1.0, value)

        def Scankey(event):
            select.delete(0, END)
            data = ids
            val = event.widget.get()
            print(val)

            if val != '':
                data = []
                for n in datas:
                    for key, value in n.items():
                        if key == "Name":
                            if val.lower() in value.lower():
                                data.append(value)
                select.delete(0, END)
                for item in data:
                    if item in ids:
                        # select.delete(END, item)
                        select.insert(END, item)
            else:
                update_book()

        def contactTab():

            ajouterBtn.destroy()
            searchEntry.destroy()
            editBtn.destroy()
            selected = select.get(ANCHOR)
            select.destroy()
            # LabelTel.update()
            # LabelAddress.destroy()
            # LableName.destroy()
            # EntryName.destroy()
            # EntryTel.destroy()
            # addressEntry.destroy()
            ajout_Frame = Frame(width='900', height='700', bg='#3d405b')
            ajout_Frame.place(x=0, y=0)
            LableName = Label(ajout_Frame, text='Name :', font='arial 18 bold',
                              fg='#fff', bd=0, bg='#3d405b')
            LableName.place(x=380, y=280)
            EntryName = Entry(ajout_Frame, textvariable=Name, justify='center', font=12,
                              width=20, bg='#b8c3bc', bd=0)
            EntryName.place(x=300, y=320)
            LabelTel = Label(ajout_Frame, text='Telephone No° :',
                             font='arial 17 bold', fg='white', bg='#3d405b', bd=0)
            EntryTel = Entry(ajout_Frame, textvariable=Number, justify='center', font=15,
                             width=20, bg='#b8c3bc', bd=0)
            EntryTel.place(x=300, y=430)
            LabelTel.place(x=330, y=380)
            LabelAddress = Label(ajout_Frame, text='Address :', justify='center',
                                 font='arial 18 bold', fg='white', bg='#3d405b', bd=0)
            LabelAddress.place(x=370, y=480)
            addressEntry = Text(ajout_Frame, width=30, height=3,
                                fg='#000', bg='#b8c3bc', bd=0)
            addressEntry.place(x=300, y=550)
            addressEntry.delete(1.0, "end")
            backBtn = Button(ajout_Frame, text='Ajouter un contact', fg='#000', bd=0,
                             bg='#fca311', width=20, height='2', cursor='hand2', command=ajoutTab)
            backBtn.place(x=60, y=80)
            for e in datas:
                for key, value in e.items():
                    if key == "Name":
                        if value == selected:
                            selected_dic = e
                            break
            for key, value in selected_dic.items():
                if key == "Name":
                    Name.set(value)
                if key == "Number":
                    Number.set(value)
                if key == "Address":
                    addressEntry.insert(1.0, value)
                if key == "img":
                    img = Image.open(value)
                    img = img.resize((150, 150), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(ajout_Frame, image=img)
                    panel.image = img
                    panel.place(x=350, y=80)

        # Tab pour Ajouter des contact

        ajout_Frame = Frame(width='900', height='700', bg='#3d405b')
        ajout_Frame.place(x=0, y=0)
        LableName = Label(ajout_Frame, text='Name :', font='arial 18 bold',
                          fg='#fff', bd=0, bg='#3d405b')
        LableName.place(x=150, y=190)
        EntryName = Entry(ajout_Frame, textvariable=Name,
                          width=20, font=11, bg='#b8c3bc', bd=0)
        EntryName.place(x=60, y=235)
        LabelTel = Label(ajout_Frame, text='Telephone No° :',
                         font='arial 17 bold', fg='white', bg='#3d405b', bd=0)
        EntryTel = Entry(ajout_Frame, textvariable=Number,
                         width=20, font=11, bg='#b8c3bc', bd=0)
        EntryTel.place(x=60, y=350)
        LabelTel.place(x=90, y=300)
        LabelAddress = Label(ajout_Frame, text='Address :',
                             font='arial 18 bold', fg='white', bg='#3d405b', bd=0)
        LabelAddress.place(x=130, y=400)
        addressEntry = Text(ajout_Frame, width=30, height=3,
                            fg='#000', bg='#b8c3bc', bd=0)
        addressEntry.place(x=60, y=450)
        ajouterBtn = Button(ajout_Frame, text='+', font='arial 17 bold', fg='#000',
                            bg='#fca311', width=3, height='1', cursor='hand2', command=add)
        ajouterBtn.place(x=370, y=330)
        select = Listbox(ajout_Frame, height=28, bg='#b8c3bc', fg="#000", bd=0,
                         width=60, )
        select.place(x=500, y=130)
        select.bind('<Double-1>', view)
        searchEntry = Entry(ajout_Frame,
                            width=30, font=10, bg='#000', fg="#fff", bd=0)
        searchEntry.place(x=500, y=100)
        searchEntry.bind('<KeyRelease>', Scankey)
        # b1 = tk.Button(my_w, text='Upload File',
        #                width=20, command=lambda: upload_file())
        clearBtn = Button(ajout_Frame, text='Clear', fg='#000',
                          bg='#fca311', width=15, height=2, cursor='hand2', command=reset)
        clearBtn.place(x=120, y=550)
        profileBtn = Button(ajout_Frame, text='Aficher le Profile', fg='#000',
                            bg='#fca311', width=15, height=2, cursor='hand2', command=contactTab)
        profileBtn.place(x=120, y=600)
        editBtn = Button(ajout_Frame, text='Suprimer', fg='#000',
                         bg='#fca311', width=20, height=2, cursor='hand2', bd=0, command=delete)
        editBtn.place(x=620, y=610)

        update_book()
        update_file()
    ajoutTab()


containe()

# Home Frame :


# Home Declaration :

home.mainloop()

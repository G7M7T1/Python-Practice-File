import tkinter

root = tkinter.Tk()
root.title('Label Case')
root.iconbitmap('logo.ico')
root.geometry('500x500')
root.resizable(0, 0)
root.config(bg='blue')

# Widgets Here
name_label_1 = tkinter.Label(root, text="Hello World")
name_label_1.pack()

name_label_2 = tkinter.Label(root, text="Hello Tkinter", font=('Arial', 18, 'bold'), bg='blue', fg='#fff')
name_label_2.pack()

name_label_3 = tkinter.Label(root)
name_label_3.config(text="Hello Python", font=('Cambria', 36), bg='blue', fg="#fff")
name_label_3.pack(padx=10, pady=60)

name_label_4 = tkinter.Label(root, text="Good Day", bg='#000', fg='green')
name_label_4.config(font=('Arial', 26))
name_label_4.pack(pady=(0, 10), padx=20)

name_label_5 = tkinter.Label(root, text='Text 5')
name_label_5.pack(anchor='w', ipadx=30, ipady=10)

name_label_6 = tkinter.Label(root)
name_label_6.config(text="Fill X Text")
name_label_6.pack(fill='x', pady=(10, 20))

name_label_7 = tkinter.Label(root, text="Fill Y Text")
name_label_7.pack(fill='y', expand=True)


# Run Main Loop Here
root.mainloop()
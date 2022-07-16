import tkinter

root = tkinter.Tk()
root.title('Label Case')
root.iconbitmap('logo.ico')
root.geometry('400x400')
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
name_label_4.pack(pady=20, padx=20)


# Run Main Loop Here
root.mainloop()
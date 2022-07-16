import tkinter

# Define Windows
root = tkinter.Tk()
root.title("Window")
root.iconbitmap('logo.ico')
root.geometry('600x500')
root.resizable(0, 1)
root.config(bg='blue')

# Second Window
top = tkinter.Toplevel()
top.title('2rd Window')
top.config(bg='#123456')
top.geometry('300x300')
top.resizable(0, 0)
top.iconbitmap('logo.ico')

# Run root window main loop
root.mainloop()

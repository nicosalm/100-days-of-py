''' 
    Using tkinter to create a GUI in Python and the accept arguments and keyword arguments
'''

import tkinter as tk

# create a window
window = tk.Tk()

# set the title
window.title('GUI Demo')

# set the size
window.geometry('400x400')

# create a label
label = tk.Label(window, text='Hello World!', font=('Arial', 40))

# pack the label
label.pack()

# create a button
button = tk.Button(window, text='Click Me!', font=('Arial', 40))

# pack the button
button.pack()

# create a text entry
text_entry = tk.Entry(window, font=('Arial', 40))

# pack the text entry
text_entry.pack()

# now, let's create a function that will be called when the button is clicked

# create a function that will be called when the button is clicked
def button_clicked(*args, **kwargs):
    # print the text in the text entry
    print(text_entry.get())
    
# set the button's command to the function
button.config(command=button_clicked)

# run the main loop
window.mainloop()
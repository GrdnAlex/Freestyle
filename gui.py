import tkinter

#
# INITIALIZE A NEW GUI WINDOW
#

window = tkinter.Tk()

#
# INITIALIZE SOME USER INTERFACE COMPONENTS
#

# MESSAGE

my_message = tkinter.Message(text="Hi. Welcome to the restaurant chooser!", width=1000)

# ENTRY (TEXT INPUT) WITH LABEL

my_cuisine = tkinter.Label(text="Input your desired cuisine:")
cuisine_value = tkinter.StringVar()
cuisine = tkinter.Entry(textvariable=cuisine_value)
#
my_zip = tkinter.Label(text="Input your zip code:")
zip_value = tkinter.StringVar()
zip = tkinter.Entry(textvariable=zip_value)
#
my_label = tkinter.Label(text="Input something here:")
entry_value = tkinter.StringVar()
my_entry = tkinter.Entry(textvariable=entry_value)

# RADIO BUTTONS

my_radio_label = tkinter.Label(text="Please select one of the following options:")
my_radio_value = tkinter.StringVar()
my_radio_a = tkinter.Radiobutton(text="Option A", value="A", variable=my_radio_value)
my_radio_b = tkinter.Radiobutton(text="Option B", value="B", variable=my_radio_value)
my_radio_c = tkinter.Radiobutton(text="Option C", value="C", variable=my_radio_value)

# CHECKBUTTONS

my_checkbox_group_label = tkinter.Label(text="Please check one or more of the following boxes:")
my_checkbox_a_val = tkinter.StringVar()
my_checkbox_a = tkinter.Checkbutton(text="Box A", variable=my_checkbox_a_val)
my_checkbox_b_val = tkinter.StringVar()
my_checkbox_b = tkinter.Checkbutton(text="Box B", variable=my_checkbox_b_val)
my_checkbox_c_val = tkinter.StringVar()
my_checkbox_c = tkinter.Checkbutton(text="Box C", variable=my_checkbox_c_val)

# LISTBOX (DROPDOWN SELECT)

my_select_label = tkinter.Label(text="Please select an item from the dropdown:")
my_select = tkinter.Listbox()
my_select.insert(1, "First Item")
my_select.insert(2, "Second Item")
my_select.insert(3, "Third Item")
my_select.insert(4, "Fourth Item")
my_select.insert(5, "Fifth Item")
my_select.insert(6, "Sixth Item")

# BUTTON

def handle_button_click():
    print("------------------------------")
    print("NICE. YOU CLICKED THE BUTTON")
    print("THE ENTRY'S INPUT VALUE IS:", my_entry.get())
    print("THE SELECTED RADIO BUTTON'S VALUE IS:", my_radio_value.get())
    print("THE CHECKBOX ON/OFF VALUES FOR A, B, C, RESPECTIVELY, ARE:", [my_checkbox_a_val.get(), my_checkbox_b_val.get(), my_checkbox_c_val.get()])
    print("THE SELECTED DROPDOWN ITEM IS:", my_select.get(my_select.curselection()))

my_button = tkinter.Button(text="Click Me", command=handle_button_click)

#
# BIND THE INDIVIDUAL COMPONENTS TO THE GUI WINDOW (PACK)
# ... THEN LAUNCH THE GUI WINDOW (MAINLOOP)
#

my_message.pack()

my_label.pack()
my_entry.pack()

my_radio_label.pack()
my_radio_a.pack()
my_radio_b.pack()
my_radio_b.pack()

my_checkbox_group_label.pack()
my_checkbox_a.pack()
my_checkbox_b.pack()
my_checkbox_c.pack()

my_select_label.pack()
my_select.pack()

my_button.pack()

window.mainloop()
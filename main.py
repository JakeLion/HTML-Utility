#import the necesarry stuff
import tkinter
from tkinter import*
from tkinter import Tk, Frame, Menu, messagebox, filedialog, PhotoImage, Label, Button, Entry
import datetime


#define and basic window details
root = Tk()
root.title('HTML Utility')
root.resizable(False, False)



#sets the window icon. Error logging section doesnt work at the moment.
try:
    i1 = PhotoImage(file = 'icon.png')
    root.iconphoto(True, i1)
except FileNotFoundError:
    now = datetime.now()
    currentt = now.strftime('%H:%M %p')
    with open('errors.log', 'a+') as logger:
        logger.write(f'[{current_date}][{currentt}]:fileNotFoundError:python failed to find icon image (icon.png) for window:cause:user may have deleted file or application was not installed properly:fix:try reinstalling program if issue persists\n')
        logger.close()


#defines all text entries and their labels, aswell as positions them.
title_lab = Label(root, text='Title:')
title_lab.grid(row=0, column=0)
title_ent = Entry(root)
title_ent.grid(row=0, column=1)

head_lab = Label(root, text='Heading:')
head_lab.grid(row=0, column=2)
head_ent = Entry(root)
head_ent.grid(row=0, column=3)

des_lab = Label(root, text='Description:')
des_lab.grid(row=1, column=2)
des_ent = Entry(root)
des_ent.grid(row=1, column=3)

subhead_lab = Label(root, text='Subheading:')
subhead_lab.grid(row=1, column=0)
subhead_ent = Entry(root)
subhead_ent.grid(row=1, column=1)

auth_lab = Label(root, text='Page Author:')
auth_lab.grid(row=2, column=0)
auth_ent = Entry(root)
auth_ent.grid(row=2, column=1)

txt_c_lab = Label(text='Text align:')
txt_c_lab.grid(row=2, column=2)
txt_c_ent = Entry(root)
txt_c_ent.grid(row=2, column=3)

par_lab = Label(root, text='Paragraph:')
par_lab.grid(row=3, column=2)
par_ent = Entry(root)
par_ent.grid(row=3, column=3)

key_lab = Label(root, text='Keywords:')
key_lab.grid(row=3, column=0)
key_ent = Entry(root)
key_ent.grid(row=3, column=1)

hyl_lab = Label(root, text='Link')
hyl_lab.grid(row=4, column=0)
hyl_ent = Entry(root)
hyl_ent.grid(row=4, column=1)

hyln_lab = Label(root, text='Link Name')
hyln_lab.grid(row=4, column=2)
hyln_ent = Entry(root)
hyln_ent.grid(row=4, column=3)



#export file funciton
def export():
    f = filedialog.asksaveasfilename(initialdir='/', title='Save document', filetypes=(('HTML file(*.html)', '*.html'), ))
    f = open(f, 'w')
    f.write(f'<html lang="en">\n<head>\n<meta name="description" content="{des_ent.get()}">\n<meta name="keywords" content="{key_ent.get()}">\n<!--Page Author: {auth_ent.get()}-->\n<title>{title_ent.get()}</title>\n</head>\n<body style="text-align:{txt_c_ent.get()};">\n<h1>{head_ent.get()}</h1>\n<h3>{subhead_ent.get()}</h3>\n<p>{par_ent.get()}</p>\n<br>\n<br>\n<a href="{hyl_ent.get()}">{hyln_ent.get()}</a>\n<br><br><br><br><br><hr><footer>\n<h3>Created for {auth_ent.get()} by <a href="https://jakesystems.us/">HTML Utility</a></h3>\n<footer>\n</body\n</html>')



exp = Button(root, text='Export', command=export)
exp.grid(row=35, column=0)

#Save this, its a note for future features

#low = Button(root, text='-', command=root.iconify)
#low.grid(row=35, column=1)


#variable = StringVar(root)
#variable.set("one") # default value

#w = OptionMenu(root, variable, "one", "two", "three")
#w.pack()

#root.overrideredirect(1)

#initialize the root
root.mainloop()

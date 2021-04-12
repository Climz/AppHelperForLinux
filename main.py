from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Button
from PIL import ImageTk, Image


window = Tk()
window.title("AppHelper")

chk_state = IntVar() # Значение по умолчанию
window.minsize("200","100")


def addapp():
	with open ("appfile.txt", "a") as f:
		f.write("F")
def letsgo():
	print(cb.get())
	for i in range(app_list_len):
		print(IntVar_list[i].get())

app_list = []
with open ("appfile.txt", "r") as f:
	l = f.read()
	l = l.replace("\n",",")
	app_list = l.split(",")

# app_list = ["flameshot", "git", "htop", "pip", "qttools5-dev",
# "qttools5-dev-tools", "obs-studio", "neofetch", "latte-dock", 
# "google-chrome-stable", "discord", "spotify-client", "postgresql", 
# "default-jre", "default-jdk", "gimp", "libreoffice", "python3-tk", "inkscape"]

app_list_len = len(app_list)

IntVar_list = []
Checkbutton_list = []
Checkbutton_label_list = []
for i in range(app_list_len):
	IntVar_list.append(IntVar())
	Checkbutton_list.append(Checkbutton(window, variable=IntVar_list[i]))
	Checkbutton_label_list.append(Label(window, text=app_list[i]))


for i in range(app_list_len):

	Checkbutton_list[i].grid(column=1, row=i+1, sticky=W)

	Checkbutton_label_list[i].grid(column=2, row=i+1, sticky=W)

# for i in app_list:
# 	row_num = app_list.index(i)
# 	print(row_num)
	

# 	chk = Checkbutton(window, variable=IntVar_list[app_list.index(i)], onvalue=1, offvalue=0, command=F)
# 	chk.grid(column=1, row=row_num+1, sticky=W)
	
# 	label = Label(window, text=i)
# 	label.grid(column=2, row=row_num+1, sticky=W)

# 	print(chk, label)


cb = Combobox(window, values=["Archlinux", "Ubuntu"], width=10)
cb.grid(column=3, row=2)

label = Label(window, text="Choose dist")
label.grid(column=3, row=1, sticky=W)

#Last button to start proces
final_button = Button(window, text="Let's go", command=letsgo)
final_button.grid(column=3, row=3)

addapp_button = Button(window, text="Add app", command=addapp)
addapp_button.grid(column=3, row=4)


# chk1 = Checkbutton(window)
# chk1.grid(column=1, row=1)
# chk2 = Checkbutton(window)
# chk2.grid(column=1, row=2)
# chk3 = Checkbutton(window)
# chk3.grid(column=1, row=3)
# chk4 = Checkbutton(window)
# chk4.grid(column=1, row=4)

# label1 = Label(window, text="HTOP")
# label1.grid(column=2, row=1)
# label2 = Label(window, text="Flameshot")
# label2.grid(column=2, row=2)
# label3 = Label(window, text="GIT")
# label3.grid(column=2, row=3)
# label4 = Label(window, text="Latte-dock")
# label4.grid(column=2, row=4)

window.mainloop()
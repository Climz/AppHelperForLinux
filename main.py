from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Button
from PIL import ImageTk, Image


window = Tk()
window.title("AppHelper")

chk_state = IntVar() # Значение по умолчанию
window.minsize("200","100")

def addapp(awe):
	with open("appfile.txt", "a") as f:
		f.write(awe.get() + "\n")


def F():
	pass


def addapp_button():
	# with open ("appfile.txt", "a") as f:
	# 	f.write("F")
	addapp_window = Tk()
	addapp_window.title("Add app")

	addapp_window_entry = Entry(addapp_window)
	addapp_window_entry.grid(column=1, columnspan=2, row=1)

	addapp_window_button_ADD = Button(addapp_window, text="Add", command= lambda: addapp(addapp_window_entry))
	addapp_window_button_ADD.grid(column=1, row=2)

	addapp_window_button_CANCEL = Button(addapp_window, text="Cancel", command=addapp_window.quit)
	addapp_window_button_CANCEL.grid(column=2, row=2)

	addapp_window.mainloop()



def letsgo():
	what_download_list = []
	for i in range(app_list_len):
		IntVar_list_v = IntVar_list[i].get()
		print(app_list[i] + "\t" + str(IntVar_list_v))
		if IntVar_list_v == 1:
			what_download_list.append(app_list[i])
	print(what_download_list)
app_list = []
with open ("appfile.txt", "r") as f:
	l = f.read()
	l = l.replace("\n",",")
	app_list = l.split(",")

# app_list = ["flameshot", "git", "htop", "pip", "qttools5-dev",
# "qttools5-dev-tools", "obs-studio", "neofetch", "latte-dock", 
# "google-chrome-stable", "discord", "spotify-client", "postgresql", 
# "default-jre", "default-jdk", "gimp", "libreoffice", "python3-tk", "inkscape"]
app_list.pop()
app_list_len = len(app_list)

IntVar_list = []
Checkbutton_list = []
Checkbutton_label_list = []
for i in range(app_list_len):
	IntVar_list.append(IntVar())
	Checkbutton_list.append(Checkbutton(window, variable=IntVar_list[i]))
	Checkbutton_label_list.append(Label(window, text=app_list[i]))

last_i = 0
for i in range(app_list_len):
	if i >= 19 and i <= 39:
		Checkbutton_list[i].grid(column=3, row=i-18, sticky=W)
		last_i = 4
		Checkbutton_label_list[i].grid(column=4, row=i-18, sticky=W)
	else:
		Checkbutton_list[i].grid(column=1, row=i+1, sticky=W)
		last_i = 2
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
cb.grid(column=last_i+2, row=2, padx=50, sticky=W+E)

label = Label(window, text="Choose dist")
label.grid(column=last_i+2, row=1, sticky=W, padx=50)

#Last button to start proces
final_button = Button(window, text="Let's go", command=letsgo)
final_button.grid(column=last_i+2, row=3, padx=50, sticky=W+E)

addapp_button = Button(window, text="Add app", command=addapp_button)
addapp_button.grid(column=last_i+2, row=4, padx=50, sticky=W+E)


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
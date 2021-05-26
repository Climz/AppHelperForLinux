from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Button
import os
import json


with open('another_appfile.json', 'r') as f:
    another_appfile = json.load(f)


window = Tk()
window.title("AppHelper")
chk_state = IntVar()
app_frame = Frame()
menu_frame = Frame()
app_frame.pack(side=LEFT, fill=BOTH)
menu_frame.pack(side=LEFT, fill=Y)


def addapp(ae):
	# Добавить регулярные выражения
	with open("appfile.txt", "a") as f:
		f.write(ae.get() + "\n")
	ae.delete(0, END)


def addapp_cancel(entry, add, cancel):
	global addapp_button_current_state
	entry.grid_remove()
	add.grid_remove()
	cancel.grid_remove()
	addapp_button_current_state = False


def F():
	pass


def select_all():
	if another_Checkbutton_list[0].winfo_viewable():
		for i in IntVar_list:
			i.set(1)
		for i in another_IntVar_list:
			i.set(1)
	else:
		for i in IntVar_list:
			i.set(1)


def deselect_all():
	if another_Checkbutton_list[0].winfo_viewable():
		for i in IntVar_list:
			i.set(0)
		for i in another_IntVar_list:
			i.set(0)
	else:
		for i in IntVar_list:
			i.set(0)


def show_another():
	if another_Checkbutton_list[0].winfo_viewable():
		for i in range(another_app_list_len):
			another_Checkbutton_list[i].grid_remove()
			another_Checkbutton_label_list[i].grid_remove()
	else:
		for i in range(another_app_list_len):
			another_Checkbutton_list[i].grid(column=another_last_column_num, row=i+1, sticky=W)
			another_Checkbutton_label_list[i].grid(column=another_last_column_num+1, row=i+1, sticky=W)


def addapp_button():
	global addapp_button_current_state
	if addapp_button_current_state:
		addapp_entry.grid_remove()
		addapp_button_ADD.grid_remove()
		addapp_button_CANCEL.grid_remove()
		addapp_button_current_state = False
	else:
		addapp_entry.grid(column=last_column_num+3, row=6, columnspan=last_column_num+4, padx=(50,0), sticky=W+E)
		addapp_button_ADD.grid(column=last_column_num+3, row=7, padx=(50,0), sticky=W+E)
		addapp_button_CANCEL.grid(column=last_column_num+4, row=7, sticky=W+E)
		addapp_button_current_state = True
		

def letsgo():
	what_download_list = []
	another_what_download_list = []
	what_distr = distr_cb.get()

	for i in range(app_list_len):
		IntVar_list_v = IntVar_list[i].get()
		print(app_list[i] + "\t" + str(IntVar_list_v))
		if IntVar_list_v == 1:
			what_download_list.append(app_list[i])
	print(" ".join(what_download_list))

	for i in range(another_app_list_len):
		another_IntVar_list_v = another_IntVar_list[i].get()
		print(another_app_list[i] + "\t" + str(another_IntVar_list_v))
		if another_IntVar_list_v == 1:
			another_what_download_list.append(another_app_list[i])
	print(" ".join(another_what_download_list))

	if what_distr == "Archlinux":
		os.system("sudo pacman -S " + " ".join(what_download_list))
	elif what_distr == "Ubuntu":
		os.system("sudo apt install " + " ".join(what_download_list))
		for i in another_what_download_list:
			for j in another_appfile[i]:
				if "cd" in j:
					os.chdir(j[3:])
				else:
					os.system(j)
# 1. Скачать
# 1.1 Взять название скаченного файла
# 2. chmod a+x VM*
# 3. sudo ./VM*

app_list = []
with open ("appfile.txt", "r") as f:
	l = f.read()
	l = l.replace("\n",",")
	app_list = l.split(",")


import tkinter.font as tkFont
fontStyle = tkFont.Font(size=8)

app_list.pop()
app_list_len = len(app_list)
IntVar_list = []
Checkbutton_list = []
Checkbutton_label_list = []
for i in range(app_list_len):
	IntVar_list.append(IntVar())
	Checkbutton_list.append(Checkbutton(master=app_frame, variable=IntVar_list[i]))
	Checkbutton_label_list.append(Label(master=app_frame, text=app_list[i].capitalize()))


last_column_num = 0
for i in range(app_list_len):
	if i >= 19 and i <= 39:
		Checkbutton_list[i].grid(column=3, row=i-18, sticky=W)
		last_column_num = 4
		Checkbutton_label_list[i].grid(column=4, row=i-18, sticky=W)
	else:
		Checkbutton_list[i].grid(column=1, row=i+1, sticky=W)
		last_column_num = 2
		Checkbutton_label_list[i].grid(column=2, row=i+1, sticky=W)


### For another apps
another_last_column_num = 1 + last_column_num
another_IntVar_list = []
another_Checkbutton_list = []
another_Checkbutton_label_list = []
another_app_list = []
with open ("another_appfile.json", "r") as f:
	l = json.load(f)
	# l = l.replace("\n",",")
	for i in l:
		another_app_list.append(i)


another_app_list_len = len(another_app_list)
for i in range(another_app_list_len):
	another_IntVar_list.append(IntVar())
	another_Checkbutton_list.append(Checkbutton(master=app_frame, variable=another_IntVar_list[i]))
	another_Checkbutton_label_list.append(Label(master=app_frame, text=another_app_list[i]))
##

distr_list = ["Archlinux", "Ubuntu"]
distr_cb = Combobox(master=menu_frame, values=distr_list, width=10)
distr_cb.set(distr_list[1])
distr_cb.grid(column=last_column_num+3, columnspan=last_column_num+4, row=2, padx=(50,0), sticky=W+E)

label = Label(master=menu_frame, text="Choose dist")
label.grid(column=last_column_num+3, columnspan=last_column_num+4, row=1, padx=(50,0))

#Last button to start proces
final_button = Button(master=menu_frame, text="Let\'s go", command=letsgo)
final_button.grid(column=last_column_num+3, row=3, padx=(50,0), sticky=W+E)

addapp_button_current_state = False
addapp_button = Button(master=menu_frame, text="Add app", command=addapp_button)
addapp_button.grid(column=last_column_num+4, row=3, sticky=W+E)

select_all_button = Button(master=menu_frame, text="Select all", command=select_all)
select_all_button.grid(column=last_column_num+3, row=4, padx=(50,0), sticky=W+E)

deselect_all_button = Button(master=menu_frame, text="Deselect all", command=deselect_all)
deselect_all_button.grid(column=last_column_num+4, row=4, sticky=W+E)

another_button = Button(master=menu_frame, text="Another", command=show_another)
another_button.grid(column=last_column_num+3, row=5,padx=(50,0))

#Add button func
addapp_entry = Entry(master=menu_frame, fg="#000000", bg="#FFFFFF")
addapp_entry.grid(column=last_column_num+3, row=6, columnspan=last_column_num+4, padx=(50,0), sticky=W+E)
addapp_button_ADD = Button(master=menu_frame, text="Add", command=lambda: addapp(addapp_entry))
addapp_button_ADD.grid(column=last_column_num+3, row=7, padx=(50,0), sticky=W+E)
addapp_button_CANCEL = Button(master=menu_frame, text="Cancel", command=lambda: addapp_cancel(addapp_entry,addapp_button_ADD,addapp_button_CANCEL))
addapp_button_CANCEL.grid(column=last_column_num+4, row=7, sticky=W+E)
addapp_entry.grid_remove()
addapp_button_ADD.grid_remove()
addapp_button_CANCEL.grid_remove()

window.mainloop()

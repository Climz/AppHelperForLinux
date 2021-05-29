from tkinter import *
from tkinter.ttk import Combobox, Checkbutton
import os
import json
import re

# Этот участок кода был создан для корректной работы команды cd в функции lets go
with open('another_appfile.json', 'r') as f:
    another_appfile = json.load(f)


window = Tk()
window.title("AppHelper")
chk_state = IntVar()
app_frame = Frame()
menu_frame = Frame()
app_frame.pack(side=LEFT, fill=BOTH)
menu_frame.pack(side=LEFT, fill=Y)


addapp_another_addcommand_list = []
def addapp_another_addcommand(ace):
	addapp_command = ace.get()
	if not re.search("[\t\n]", addapp_command) and len(addapp_command) != 0:
		addapp_another_addcommand_list.append(addapp_command)
		ace.delete(0, END)
	else:
		print("Type command")


def addapp_another_cancel():
	global addapp_button_another_current_state
	addapp_command_entry.grid_remove()
	addapp_command_add.grid_remove()
	addapp_command_cancel.grid_remove()
	addapp_button_another_current_state = False


def addapp_piplib():
	global addapp_button_another_current_state
	global addapp_button_piplib_current_state
	if addapp_button_piplib_current_state:
		addapp_button_piplib_current_state = False
		addapp_button_piplib.config(text = "PL")
	else:
		addapp_command_entry.grid_remove()
		addapp_command_add.grid_remove()
		addapp_command_cancel.grid_remove()
		addapp_button_another_current_state = False
		addapp_button_piplib_current_state = True
		addapp_button_piplib.config(text = "PL(Active)")
		addapp_button_anotherapp.config(text = "AA")



def addapp_another():
	# Если вот это true, значит меню добавления команды активно
	global addapp_button_another_current_state
	global addapp_button_piplib_current_state
	if addapp_button_another_current_state:
		addapp_command_entry.grid_remove()
		addapp_command_add.grid_remove()
		addapp_command_cancel.grid_remove()
		addapp_button_another_current_state = False
		addapp_button_anotherapp.config(text = "AA")
	else:
		addapp_command_entry.grid(column=last_column_num+5, row=9, columnspan=last_column_num+4, padx=(50,0), sticky=W+E)
		addapp_command_add.grid(column=last_column_num+5, row=10, padx=(50,0), sticky=W+E)
		addapp_command_cancel.grid(column=last_column_num+6, row=10, sticky=W+E)
		addapp_button_another_current_state = True
		addapp_button_piplib_current_state = False
		addapp_button_piplib.config(text = "PL")
		addapp_button_anotherapp.config(text = "AA(Active)")


def addapp(ae):
	# Добавить регулярные выражения
	global addapp_button_another_current_state
	global addapp_button_piplib_current_state
	addapp_name = ae.get()
	
	parser = re.search("[^-A-Za-z0-9\\.\\=]", addapp_name)
	if not re.search("[\t\\s\n""]", addapp_name) and len(addapp_name) != 0:
		if parser == None:
			# В данный момент добавляется another приложение
			if addapp_button_another_current_state and not addapp_button_piplib_current_state: 
				addapp_another_dict = {}
				addapp_another_addcommand_list.append(addapp_command_entry.get())
				addapp_another_dict[addapp_name] = addapp_another_addcommand_list
				with open("another_appfile_test.json", "r+") as f:
					data = json.load(f)
					data.update(addapp_another_dict)
					f.seek(0)
					json.dump(data, f)
				ae.delete(0, END)
				addapp_command_entry.delete(0, END)
			elif not addapp_button_another_current_state and addapp_button_piplib_current_state:
				with open("pip_lib.txt", "a") as f:
					f.write(addapp_name.lower() + "\n")
				ae.delete(0, END)
			else:
				with open("appfile.txt", "a") as f:
					f.write(addapp_name.lower() + "\n")
				ae.delete(0, END)
		else:
			print("Found", parser.group())
	else:
		print("Found something character")


def addapp_cancel(entry, add, cancel):
	global addapp_button_current_state
	global addapp_button_another_current_state

	entry.grid_remove()
	add.grid_remove()
	cancel.grid_remove()
	addapp_command_entry.grid_remove()
	addapp_command_add.grid_remove()
	addapp_command_cancel.grid_remove()
	addapp_button_anotherapp.grid_remove()
	addapp_button_current_state = False
	addapp_button_another_current_state = False


def f():
	pass


def select_all():
	
	if another_Checkbutton_list[0].winfo_viewable() and piplib_Checkbutton_list[0].winfo_viewable():
		for i in IntVar_list:
			i.set(1)
		for i in another_IntVar_list:
			i.set(1)
		for i in piplib_IntVar_list:
			i.set(1)
	elif another_Checkbutton_list[0].winfo_viewable():
		for i in IntVar_list:
			i.set(1)
		for i in another_IntVar_list:
			i.set(1)
	elif piplib_Checkbutton_list[0].winfo_viewable():
		for i in IntVar_list:
			i.set(1)
		for i in piplib_IntVar_list:
			i.set(1)
	else:
		for i in IntVar_list:
			i.set(1)


def deselect_all():
	if another_Checkbutton_list[0].winfo_viewable() and piplib_Checkbutton_list[0].winfo_viewable():
		for i in IntVar_list:
			i.set(0)
		for i in another_IntVar_list:
			i.set(0)
		for i in piplib_IntVar_list:
			i.set(0)
	elif another_Checkbutton_list[0].winfo_viewable():
		for i in IntVar_list:
			i.set(0)
		for i in another_IntVar_list:
			i.set(0)
	elif piplib_Checkbutton_list[0].winfo_viewable():
		for i in IntVar_list:
			i.set(0)
		for i in piplib_IntVar_list:
			i.set(0)
	else:
		for i in IntVar_list:
			i.set(0)


def show_piplib():
	if piplib_Checkbutton_list[0].winfo_viewable():
		for i in range(piplib_app_list_len):
			piplib_Checkbutton_list[i].grid_remove()
			piplib_Checkbutton_label_list[i].grid_remove()
			if not kostyl_flag:
				if another_Checkbutton_list[0].winfo_viewable():
					print("Before",window.winfo_geometry())
					window.minsize(int(win_size_another[:3]), int(win_size_another[4:]))
					window.maxsize(int(win_size_another[:3]), int(win_size_another[4:]))
					print("After",window.winfo_geometry())
				else:
					print("Before",window.winfo_geometry())
					window.minsize(int(win_size_nothing[:3]), int(win_size_nothing[4:]))
					window.maxsize(int(win_size_nothing[:3]), int(win_size_nothing[4:]))
					print("After",window.winfo_geometry())
	else:
		for i in range(piplib_app_list_len):
			piplib_Checkbutton_list[i].grid(column=piplib_last_column_num, row=i+1, sticky=W)
			piplib_Checkbutton_label_list[i].grid(column=piplib_last_column_num+1, row=i+1, sticky=W)
			if not kostyl_flag:
				if another_Checkbutton_list[0].winfo_viewable():
					print("Before",window.winfo_geometry())
					window.minsize(int(win_size_all[:3]), int(win_size_all[4:]))
					window.maxsize(int(win_size_all[:3]), int(win_size_all[4:]))
					print("After",window.winfo_geometry())
				else:
					print("Before",window.winfo_geometry())
					window.minsize(int(win_size_piplib[:3]), int(win_size_piplib[4:]))
					window.maxsize(int(win_size_piplib[:3]), int(win_size_piplib[4:]))
					print("After",window.winfo_geometry())


def show_another():
	if another_Checkbutton_list[0].winfo_viewable():
		for i in range(another_app_list_len):
			another_Checkbutton_list[i].grid_remove()
			another_Checkbutton_label_list[i].grid_remove()
			if not kostyl_flag:
				if piplib_Checkbutton_list[0].winfo_viewable():
					print("Before",window.winfo_geometry())
					window.minsize(int(win_size_piplib[:3]), int(win_size_piplib[4:]))
					window.maxsize(int(win_size_piplib[:3]), int(win_size_piplib[4:]))
					window.update()
					print("After",window.winfo_geometry())
				else:
					print("Before",window.winfo_geometry())
					window.minsize(int(win_size_nothing[:3]), int(win_size_nothing[4:]))
					window.maxsize(int(win_size_nothing[:3]), int(win_size_nothing[4:]))
					window.update()
					print("After",window.winfo_geometry())
	else:
		for i in range(another_app_list_len):
			another_Checkbutton_list[i].grid(column=another_last_column_num, row=i+1, sticky=W)
			another_Checkbutton_label_list[i].grid(column=another_last_column_num+1, row=i+1, sticky=W)
			if not kostyl_flag:
				if piplib_Checkbutton_list[0].winfo_viewable():
					print("Before",window.winfo_geometry())
					window.minsize(int(win_size_all[:3]), int(win_size_all[4:]))
					window.maxsize(int(win_size_all[:3]), int(win_size_all[4:]))
					window.update()
					print("After",window.winfo_geometry())
					
				else:
					print("Before",window.winfo_geometry())
					window.minsize(int(win_size_another[:3]), int(win_size_another[4:]))
					window.maxsize(int(win_size_another[:3]), int(win_size_another[4:]))
					window.update()
					print("After",window.winfo_geometry())


def addapp_button():
	global addapp_button_current_state
	global addapp_button_another_current_state
	global addapp_button_piplib_current_state
	

	if addapp_button_current_state:
		addapp_entry.grid_remove()
		addapp_button_ADD.grid_remove()
		addapp_button_CANCEL.grid_remove()
		addapp_button_anotherapp.grid_remove()
		addapp_command_entry.grid_remove()
		addapp_command_add.grid_remove()
		addapp_command_cancel.grid_remove()
		addapp_button_anotherapp.grid_remove()
		addapp_button_piplib.grid_remove()
		addapp_button_current_state = False
		addapp_button_another_current_state = False
		addapp_button_piplib.config(text = "PL")
		addapp_button_anotherapp.config(text = "AA")
	else:
		addapp_entry.grid(column=last_column_num+5, row=6, columnspan=last_column_num+4, padx=(50,0), sticky=W+E)
		addapp_button_ADD.grid(column=last_column_num+5, row=7, padx=(50,0), sticky=W+E)
		addapp_button_CANCEL.grid(column=last_column_num+6, row=7, sticky=W+E)
		addapp_button_anotherapp.grid(column=last_column_num+5, row=8, padx=(50,0), sticky=W+E)
		addapp_button_piplib.grid(column=last_column_num+6, row=8, sticky=W+E)

		addapp_button_current_state = True
		

def letsgo():
	what_download_list = []
	another_what_download_list = []
	piplib_what_download_list = []
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

	for i in range(piplib_app_list_len):
		piplib_IntVar_list_v = piplib_IntVar_list[i].get()
		print(piplib_app_list[i] + "\t" + str(piplib_IntVar_list_v))
		if piplib_IntVar_list_v == 1:
			piplib_what_download_list.append(piplib_app_list[i])
	print(" ".join(piplib_what_download_list))

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

	# Pip libries
	if piplib_what_download_list == []:
		pass
	else:
		os.system("pip3 install " + " ".join(what_download_list))

# 1. Скачать
# 1.1 Взять название скаченного файла
# 2. chmod a+x VM*
# 3. sudo ./VM*

app_list = []
with open ("appfile.txt", "r") as f:
	l = f.read()
	l = l.replace("\n",",")
	app_list = l.split(",")


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
###

### Pip libriares
piplib_last_column_num = 2 + another_last_column_num
piplib_IntVar_list = []
piplib_Checkbutton_list = []
piplib_Checkbutton_label_list = []
piplib_app_list = []
with open ("pip_lib.txt", "r") as f:
	l = f.read()
	l = l.replace("\n",",")
	piplib_app_list = l.split(",")

piplib_app_list.pop()
piplib_app_list_len = len(piplib_app_list)
for i in range(piplib_app_list_len):
	piplib_IntVar_list.append(IntVar())
	piplib_Checkbutton_list.append(Checkbutton(master=app_frame, variable=piplib_IntVar_list[i]))
	piplib_Checkbutton_label_list.append(Label(master=app_frame, text=piplib_app_list[i]))

###

distr_list = ["Archlinux", "Ubuntu"]
distr_cb = Combobox(master=menu_frame, values=distr_list, width=10)
distr_cb.set(distr_list[1])
distr_cb.grid(column=last_column_num+5, columnspan=last_column_num+4, row=2, padx=(50,0), sticky=W+E)

label = Label(master=menu_frame, text="Choose dist")
label.grid(column=last_column_num+5, columnspan=last_column_num+4, row=1, padx=(50,0))

#Last button to start proces
final_button = Button(master=menu_frame, text="Let\'s go", command=letsgo,
	width=7, height=1)
final_button.grid(column=last_column_num+5, row=3, padx=(50,0), sticky=W+E)

addapp_button_current_state = False
addapp_button = Button(master=menu_frame, text="Add app", command=addapp_button,
	width=7, height=1, activebackground="#555555")
addapp_button.grid(column=last_column_num+6, row=3, sticky=W+E)

select_all_button = Button(master=menu_frame, text="Select all", command=select_all,
	width=7, height=1, activebackground="#555555")
select_all_button.grid(column=last_column_num+5, row=4, padx=(50,0), sticky=W+E)

deselect_all_button = Button(master=menu_frame, text="Deselect all", command=deselect_all,
	width=7, height=1, activebackground="#555555")
deselect_all_button.grid(column=last_column_num+6, row=4, sticky=W+E)

another_button = Button(master=menu_frame, text="Another", command=show_another,
	width=7, height=1, activebackground="#555555")
another_button.grid(column=last_column_num+5, row=5,padx=(50,0), sticky=W+E)

piplib_button = Button(master=menu_frame, text="Pip lib", command=show_piplib,
	width=7, height=1, activebackground="#555555")
piplib_button.grid(column=last_column_num+6, row=5, sticky=W+E)
# Add app

addapp_entry = Entry(master=menu_frame, fg="#000000", bg="#FFFFFF")
addapp_entry.grid(column=last_column_num+5, row=6, columnspan=last_column_num+4, padx=(50,0), sticky=W+E)
addapp_button_ADD = Button(master=menu_frame, text="Add", command=lambda: addapp(addapp_entry),
	width=7, height=1, activebackground="#555555")
addapp_button_ADD.grid(column=last_column_num+5, row=7, padx=(50,0), sticky=W+E)
addapp_button_CANCEL = Button(master=menu_frame, text="Cancel", command=lambda: addapp_cancel(addapp_entry,addapp_button_ADD,addapp_button_CANCEL),
	width=7, height=1, activebackground="#555555")
addapp_button_CANCEL.grid(column=last_column_num+6, row=7, sticky=W+E)

## Add another app 
addapp_button_another_current_state = False
addapp_button_anotherapp = Button(master=menu_frame, text="AA", command=addapp_another,
	width=7, height=1, activebackground="#555555")
addapp_button_anotherapp.grid(column=last_column_num+5, row=8, padx=(50,0), sticky=W+E)
addapp_button_piplib_current_state = False
addapp_button_piplib = Button(master=menu_frame, text="PL", command=addapp_piplib,
	width=7, height=1, activebackground="#555555")
addapp_button_piplib.grid(column=last_column_num+6, row=8, sticky=W+E)

addapp_command_current_state = False
addapp_command_entry = Entry(master=menu_frame, fg="#000000", bg="#FFFFFF")
addapp_command_entry.grid(column=last_column_num+5, row=9, columnspan=last_column_num+4, padx=(50,0), sticky=W+E)
addapp_command_add = Button(master=menu_frame, text="Add", command=lambda: addapp_another_addcommand(addapp_command_entry),
	width=7, height=1, activebackground="#555555")
addapp_command_add.grid(column=last_column_num+5, row=10, padx=(50,0), sticky=W+E)
addapp_command_cancel = Button(master=menu_frame, text="Cancel", command=addapp_another_cancel,
	width=7, height=1, activebackground="#555555")
addapp_command_cancel.grid(column=last_column_num+6, row=10, sticky=W+E)
###



##

#
addapp_entry.grid_remove()
addapp_button_ADD.grid_remove()
addapp_button_CANCEL.grid_remove()
addapp_button_anotherapp.grid_remove()
addapp_command_entry.grid_remove()
addapp_command_add.grid_remove()
addapp_command_cancel.grid_remove()
addapp_button_piplib.grid_remove()


kostyl_flag = True
win_size_nothing, win_size_all, win_size_another, win_size_piplib = str(), str(), str(), str()
def kostyl():
	global win_size_nothing, win_size_all, win_size_another, win_size_piplib
	window.update()
	win_size_nothing = window.winfo_geometry() # Без всего
	show_another() 
	show_piplib()
	window.update()
	win_size_all = window.winfo_geometry() # Со всеми
	show_piplib()
	window.update()
	win_size_another = window.winfo_geometry() # Another
	show_another()
	show_piplib()
	window.update()
	win_size_piplib = window.winfo_geometry() # Pip lib
	show_piplib()
	win_size_nothing = win_size_nothing[:7]
	win_size_all = win_size_all[:7]
	win_size_another = win_size_another[:7]
	win_size_piplib = win_size_piplib[:7]
	print(f"Nothing {win_size_nothing}\nAll {win_size_all}\nAnother {win_size_another}\nPiplib {win_size_piplib}")



kostyl()
kostyl_flag = False
window.minsize(int(win_size_nothing[:3]), int(win_size_nothing[4:]))
window.maxsize(int(win_size_nothing[:3]), int(win_size_nothing[4:]))
window.mainloop()


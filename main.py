from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Button
from PIL import ImageTk, Image
import os


window = Tk()
window.title("AppHelper")

chk_state = IntVar()
window.minsize("200","100")

def addapp(ae):
	with open("appfile.txt", "a") as f:
		f.write(ae.get() + "\n")
	ae.delete(0, END)


def addapp_cancel(entry, add, cancel):
	entry.grid_remove()
	add.grid_remove()
	cancel.grid_remove()


def F():
	pass


def select_all():
	for i in IntVar_list:
		i.set(1)


def deselect_all():
	for i in IntVar_list:
		i.set(0)


def addapp_button():
	# addapp_window = Tk()
	# addapp_window.title("Add app")

	# addapp_window_entry = Entry(addapp_window)
	# addapp_window_entry.grid(column=1, columnspan=2, row=1)

	# addapp_window_button_ADD = Button(addapp_window, text="Add", command= lambda: addapp(addapp_window_entry))
	# addapp_window_button_ADD.grid(column=1, row=2)

	# addapp_window_button_CANCEL = Button(addapp_window, text="Cancel", command=addapp_window.quit)
	# addapp_window_button_CANCEL.grid(column=2, row=2)

	# addapp_window.mainloop()

	addapp_entry = Entry(window, fg="#000000", bg="#FFFFFF")
	addapp_entry.grid(column=last_i+2, row=5, columnspan=last_i+3, padx=(50,0), sticky=W+E)
	addapp_button_ADD = Button(window, text="Add", command=lambda: addapp(addapp_entry))
	addapp_button_ADD.grid(column=last_i+2, row=6, padx=(50,0), sticky=W+E)
	addapp_button_CANCEL = Button(window, text="Cancel", command=lambda: addapp_cancel(addapp_entry,addapp_button_ADD,addapp_button_CANCEL))
	addapp_button_CANCEL.grid(column=last_i+3, row=6, sticky=W+E)



def letsgo():
	what_download_list = []
	what_distr = distr_cb.get()
	for i in range(app_list_len):
		IntVar_list_v = IntVar_list[i].get()
		print(app_list[i] + "\t" + str(IntVar_list_v))
		if IntVar_list_v == 1:
			what_download_list.append(app_list[i])
	print(" ".join(what_download_list))
	if what_distr == "Archlinux":
		os.system("sudo pacman -S " + " ".join(what_download_list))
	elif what_distr == "Ubuntu":
		os.system("sudo apt install " + " ".join(what_download_list))


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


distr_list = ["Archlinux", "Ubuntu"]
distr_cb = Combobox(window, values=distr_list, width=10)
distr_cb.set(distr_list[0])
distr_cb.grid(column=last_i+2, columnspan=last_i+3, row=2, padx=(50,0), sticky=W+E)

label = Label(window, text="Choose dist")
label.grid(column=last_i+2, columnspan=last_i+3, row=1, padx=(50,0))

#Last button to start proces
final_button = Button(window, text="Let's go", command=letsgo)
final_button.grid(column=last_i+2, row=3, padx=(50,0), sticky=W+E)

addapp_button = Button(window, text="Add app", command=addapp_button)
addapp_button.grid(column=last_i+3, row=3, sticky=W+E)

select_all_button = Button(window, text="Select all", command=select_all)
select_all_button.grid(column=last_i+2, row=4, padx=(50,0), sticky=W+E)

deselect_all_button = Button(window, text="Deselect all", command=deselect_all)
deselect_all_button.grid(column=last_i+3, row=4, sticky=W+E)


window.mainloop()
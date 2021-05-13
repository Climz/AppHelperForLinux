from tkinter import *
import tkinter.font as tkFont
window=Tk()
for i in range(3):
	for j in range(3):
		window.grid_columnconfigure(j, weight=0)
		window.grid_rowconfigure(i, weight=0)
fontStyle = tkFont.Font(size=20)
label = Label(window, text="F", font=fontStyle)
label1 = Label(window, text="F", font=fontStyle)
label2 = Label(window, text="F", font=fontStyle)
label.grid()
label1.grid()
label2.grid()
window.geometry("300x300")
window.mainloop()
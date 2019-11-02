#!/usr/bin/env python3
from tkinter import *
import tkinter.messagebox

print("Image Scraper v.0.0.0")


#class ScraperButtons:
#
#	def __init__(self, master):
#		frame = Frame(master)
#		frame.pack()
#		self.print_button = Button(frame, text = "Print", command = self.printHelp)
#		self.print_button.pack(side = LEFT)
#		self.quit_button = Button(frame, text = "Quit", command = frame.quit)
#		self.quit_button.pack(side = LEFT)
#
#	def printHelp(self):
#		print("Image Scraper 2")

def defaultFunction():
	print("Image Scraper v.0.0.0")

root = Tk()
root.title("Image Scraper v.0.0.0")
root.geometry("640x480")

main_menu = Menu(root)
root.config(menu = main_menu)
file_menu = Menu(main_menu)
main_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Open", command = defaultFunction)
file_menu.add_command(label = "New" , command = defaultFunction)
file_menu.add_command(label = "Search", command = defaultFunction)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = defaultFunction)
edit_menu = Menu(main_menu)
main_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Resize", command = defaultFunction)
edit_menu.add_command(label = "Select", command = defaultFunction)
options_menu = Menu(main_menu)
main_menu.add_cascade(label = "Options", menu = options_menu)
options_menu.add_command(label = "Current File", command = defaultFunction)
options_menu.add_command(label = "Current Directory", command = defaultFunction)

main_frame = Frame(root)
main_frame.pack_propagate(False)
main_frame.pack(fill = BOTH, expand = True)
#main_frame.grid(row = 0, column = 0)

status_bar = Label(root, text = "Ready", bd = 1, relief = SUNKEN, anchor = W)
status_bar.pack(side = BOTTOM, fill = X)
#status_bar.grid(row = 1, column = 0, sticky = S)

search_label = Label(main_frame, text = "Search Term: ")
#search_label.pack(side = RIGHT)
search_entry = Entry(main_frame)
#search_entry.pack(side = RIGHT)
search_button = Button(main_frame, text = "Search", command = defaultFunction)
#search_button.pack(side = RIGHT)
pause_button = Button(main_frame, text = "Pause", command = defaultFunction)
#pause_button.pack(side = RIGHT)
cancel_button = Button(main_frame, text = "Cancel", command = defaultFunction)
#cancel_button.pack(side = RIGHT)
search_label.grid(row = 0, sticky = E)
search_entry.grid(row = 0, column = 1, columnspan = 2)
search_button.grid(row = 1, column = 0)
pause_button.grid(row = 1, column = 1)
cancel_button.grid(row = 1, column = 2)

root.mainloop()

#root = Tk()

#s = ScraperButtons(root) 

#tkinter.messagebox.showinfo("Warning", "Application loaded.")
#myAnswer = tkinter.messagebox.askquestion("Warning", "Would you like to quit the application?")
#if myAnswer == 'yes':
#	defaultFunction()

#main_toolbar = Frame(root, bg = "blue")
#insert_button = Button(main_toolbar, text = "Insert Image", command = defaultFunction)
#insert_button.pack(side = LEFT, padx = 2, pady = 2)
#print_button = Button(main_toolbar, text = "Print", command = defaultFunction)
#print_button.pack(side = LEFT, padx = 2, pady = 2)
#main_toolbar.pack(side = TOP, fill = X)

#image_canvas = Canvas(root, width = 200, height = 100)
#image_canvas.pack()
#first_line = image_canvas.create_line(0, 0, 200, 50) #(x_start, y_start, x_end, y_end)
#second_line = image_canvas.create_line(0, 100, 200, 50, fill = "red")
#first_box = image_canvas.create_rectangle(25, 25, 130, 60, fill = "green")
#image_canvas.delete(first_line)
#image_canvas.delete(ALL)

#image_photo = PhotoImage(file = "picture.png")
#image_label = Label(root, image = image_photo)
#image_label.pack()

#first_label = Label(root, text = "Image Scraper")
#first_label.pack()

#top_frame = Frame(root)
#top_frame.pack()

#bottom_frame = Frame(root)
#bottom_frame.pack(side = BOTTOM)

#button_1 = Button(top_frame, text = "Button 1", fg = "red")
#button_2 = Button(top_frame, text = "Button 2", fg = "blue")
#button_3 = Button(top_frame, text = "Button 3", fg = "green")
#button_4 = Button(bottom_frame, text = "Button 4", fg = "purple")
#button_1.pack(side = LEFT)
#button_2.pack(side = LEFT)
#button_3.pack(side = LEFT)
#button_4.pack(side = BOTTOM)

#second_label = Label(root, text = "One", bg = "red", fg = "white")
#second_label.pack()
#third_label = Label(root, text = "Two", bg = "green", fg = "black")
#third_label.pack(fill = X)
#fourth_label = Label(root, text = "Three", bg = "blue", fg = "white")
#fourth_label.pack(side = LEFT, fill = Y)

#fifth_label = Label(root, text = "Name")
#sixth_label = Label(root, text = "Password")
#first_entry = Entry(root)
#second_entry = Entry(root)
#fifth_label.grid(row = 0, sticky = E)
#sixth_label.grid(row = 1, sticky = E)
#first_entry.grid(row = 0, column = 1)
#second_entry.grid(row = 1, column = 1)
#first_checkbutton = Checkbutton(root, text = "Keep me logged in")
#first_checkbutton.grid(columnspan = 2)

#def printHelp():
#	print("Image Scraper - aerobautics@gmail.com")
#
#def printHelpTwo(event):
#	print("Image Scraper - aerobautics@gmail.com")
#
#button_5 = Button(root, text = "Help", command = printHelp)  
#button_5.pack()
#button_6 = Button(root, text = "Help 2")
#button_6.bind("<Button-1>", printHelpTwo)  
#button_6.pack()

#def leftClick(event):
#	print("Left")
#
#def middleClick(event):
#	print("Middle")
#
#def rightClick(event):
#	print("Right")
#
#frame = Frame(root, width = 300, height = 250)
#frame.bind("<Button-1>", leftClick)
#frame.bind("<Button-2>", middleClick)
#frame.bind("<Button-3>", rightClick)
#frame.pack()

#root.mainloop()

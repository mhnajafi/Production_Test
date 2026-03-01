import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import array as arr
import threading
from functools import partial

from tests import *
from ranges import *
from checks import *

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)

		self.attributes('-fullscreen', True)
		#self.configure(bg='white')

		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, TestPage, TimeoutPage,SetPage):

			frame = F(container, self,)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()



def test_page(controller):
	controller.show_frame(TestPage)
	for button in Button_list:
			button["state"] = NORMAL
			button.configure(bg = "azure2",activebackground = "azure2")
	for check in Check_list:
		check["state"] = NORMAL
	Button_list[18]["text"]="Start"
	Serial_label[1]=""
	Serial_label[0].config(text = "SN: ")




# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		#self['background']='#856ff8'
		# label of frame Layout 2
		label = tk.Label(self, text ="Tester Program", font = LARGEFONT)
		label.place(x=xx(3), y=yy(3))


		button1 = tk.Button(self, text ="Test page",bg = "azure2",width=ww(20),height=hh(50),
			command = lambda : test_page(controller))
		button1.place(x=xx(10), y=yy(20))


		button2 = tk.Button(self, text ="Set Timeouts",bg = "azure2",width=ww(20),height=hh(20),
			command = lambda : controller.show_frame(TimeoutPage))
		button2.place(x=xx(40), y=yy(20))


		button3 = tk.Button(self, text ="Set ranges",bg = "azure2",width=ww(20),height=hh(20),
			command = lambda : controller.show_frame(SetPage))
		button3.place(x=xx(40), y=yy(50))
		
		
		# exit_btn = tk.Button(self, text ="Exit",bg = "azure2",width=ww(6),height=hh(10),
		# 	command = lambda : exit())
		# exit_btn.place(x=xx(0), y=yy(90))
		


# second window frame page1
class TestPage(tk.Frame):
	
	def __init__(self, parent, controller):
		global Test_list
		tk.Frame.__init__(self, parent)
		
		# label = tk.Label(self, text ="Test page:", font = LARGEFONT)
		# label.place(x=xx(20), y=yy(3))


		Label_list=["Program","Serial Number","Supply","Outputs","Inputs/Zones","Audio"
		,"Dummy","Short Circuits","Battery","GSM","operator","Function 1"
		,"Function 2","Function3","Temperature","Remote","Sound GSM2","Factory Set"]


		cnt=0
		for label in Label_list:
			Button_list.append(tk.Button(self, text =label,bg = "azure2",width=ww(10),height=hh(20),
				command = partial(Test_Start,cnt)))
			Check_list.append( tk.Button(self, text ="Check  >",bg = "azure2",width=ww(10),height=hh(3),
				command = partial(Test_Check,cnt)))
			cnt=cnt+1
		
		for j in range(0,3):
			for k in range(0,6):
				Button_list[k+(j*6)].place(x=xx(4+16*k), y=yy(14+j*28))
				Check_list[k+(j*6)].place(x=xx(4+16*k), y=yy(34+j*28))

		

		Serial_label.append(tk.Label(self, text ="SN: ",bg = "azure2",font = MEDIUMFONT))
		Serial_label[0].place(x=xx(15), y=yy(5))
		Serial_label.append("")


		Button_list.append(tk.Button(self, text ="Start",bg = 
		"azure2",width=ww(10),height=hh(6),
				command = Start_Stop))
		Button_list[18].place(x=xx(52), y=yy(3))


		label_NONE = tk.Label(self, text =" No Result ",bg="azure2",font = MEDIUMFONT)
		label_NONE.place(x=xx(70), y=yy(2))

		label_PEND = tk.Label(self, text ="In Progress",bg="orange",font = MEDIUMFONT)
		label_PEND.place(x=xx(70), y=yy(7))

		label_BAD = tk.Label(self, text ="  Not Pass ",bg="red",font = MEDIUMFONT)
		label_BAD.place(x=xx(85), y=yy(7))

		label_OK = tk.Label(self, text ="     Pass     ",bg="green",font = MEDIUMFONT)
		label_OK.place(x=xx(85), y=yy(2))


		Exit_Button = tk.Button(self, text ="Home",bg = "azure2",width=ww(6),height=hh(6),
			command = lambda : controller.show_frame(StartPage))
		Exit_Button.place(x=xx(4), y=yy(3))

		



# third window frame page2
class TimeoutPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		

		config = configparser.ConfigParser()
		config.read('config.ini')

		Label_list1=["power switch:","holtek program:","Read power:","short circuit:","microphone:","zone:"]
		Label_list2=["key:","dummy load:","output:","siren:","Audio:"]
		Labels=[]

		name_label_1=tk.Label(self, text ="Action               	   Timeout",bg="gray",font = MEDIUMFONT)
		name_label_1.place(x=xx(3), y=yy(20)) 
		cnt=0
		for label in Label_list1:
			Labels.append(tk.Label(self, text =label,font = MEDIUMFONT))
			Labels[cnt].place(x=xx(3), y=yy(25+cnt*8))
			Spin_list_timeouts.append(tk.Spinbox(self,width=ww(6),font=MEDIUMFONT))
			Spin_list_timeouts[cnt].place(x=xx(25), y=yy(25+cnt*8))			
			Spin_list_timeouts[cnt].insert(0,config.get("timeouts",("time_"+str(cnt))))
			cnt=cnt+1
		
		
		os1=50
		cnt2=0
		name_label_2=tk.Label(self, text ="Action                  	   Timeout",bg="gray",font = MEDIUMFONT)
		name_label_2.place(x=xx(3+os1), y=yy(20)) 
		for label in Label_list2:
			Labels.append(tk.Label(self, text =label,font = MEDIUMFONT))
			Labels[cnt].place(x=xx(3+os1), y=yy(25+cnt2*8))
			Spin_list_timeouts.append(tk.Spinbox(self,width=ww(6),font=MEDIUMFONT))
			Spin_list_timeouts[cnt].place(x=xx(25+os1), y=yy(25+cnt2*8))			
			Spin_list_timeouts[cnt].insert(0,config.get("timeouts",("time_"+str(cnt))))
			cnt=cnt+1
			cnt2=cnt2+1


		Save_Button=tk.Button(self, text ="Save",bg = 
		"azure2",width=ww(15),height=hh(7),
			command = Save_timeouts)
		Save_Button.place(x=xx(42), y=yy(3))

		Exit_Button = tk.Button(self, text ="Home",bg = "azure2",width=ww(6),height=hh(5),
			command = lambda : controller.show_frame(StartPage))
		Exit_Button.place(x=xx(5), y=yy(3))
		
		
		
# third window frame page2
class SetPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		config = configparser.ConfigParser()
		config.read('config.ini')

		Label_list1=["V 13.5:","V 4.0:","V 5.0:","V 3.3_1:","V 3.3_2:","V 15.0:","V AC:",
			   "V BAT:","V Dummy:"]
		Label_list2=["Zone 1:","Zone 2:","Zone 3:","Zone 4:","Zone 5:",
			   "Out 1:","Out 2:","Out 3:","Out 4:"]
		Label_list3=["Siren:","Holtek 1:","Holtek 2:","SP sig 1:","SP sig 2:",
			   "SP pre 1:","SP pre 2:"]
		
		Labels=[]

		name_label_1=tk.Label(self, text ="Point            Min            Max",
						bg="gray",font = MEDIUMFONT)
		name_label_1.place(x=xx(3), y=yy(12)) 
		cnt=0
		for label in Label_list1:
			Labels.append(tk.Label(self, text =label,font = MEDIUMFONT))
			Labels[cnt].place(x=xx(3), y=yy(18+cnt*8))
			Spin_list_ranges_min.append(tk.Spinbox(self,width=ww(6),font=MEDIUMFONT))
			Spin_list_ranges_min[cnt].place(x=xx(15), y=yy(18+cnt*8))
			Spin_list_ranges_max.append(tk.Spinbox(self,width=ww(6),font=MEDIUMFONT))
			Spin_list_ranges_max[cnt].place(x=xx(25), y=yy(18+cnt*8))
			try:
				Spin_list_ranges_min[cnt].insert(0,config.get("ranges",("min_"+str(cnt))))			
			except:
				Spin_list_ranges_min[cnt].insert(0,"0")
			try:
				Spin_list_ranges_max[cnt].insert(0,config.get("ranges",("max_"+str(cnt))))
			except:
				Spin_list_ranges_max[cnt].insert(0,"1000")
			cnt=cnt+1

		
		os1=34
		name_label_2=tk.Label(self, text ="Point            Min            Max",
						bg="gray",font = MEDIUMFONT)
		name_label_2.place(x=xx(os1+3), y=yy(12)) 
		cnt2=0
		for label in Label_list2:
			Labels.append(tk.Label(self, text =label,font = MEDIUMFONT))
			Labels[cnt].place(x=xx(os1+3), y=yy(18+cnt2*8))
			Spin_list_ranges_min.append(tk.Spinbox(self,width=ww(6),font=MEDIUMFONT))
			Spin_list_ranges_min[cnt].place(x=xx(os1+13), y=yy(18+cnt2*8))
			Spin_list_ranges_max.append(tk.Spinbox(self,width=ww(6),font=MEDIUMFONT))
			Spin_list_ranges_max[cnt].place(x=xx(os1+23), y=yy(18+cnt2*8))
			try:
				Spin_list_ranges_min[cnt].insert(0,config.get("ranges",("min_"+str(cnt))))			
			except:
				Spin_list_ranges_min[cnt].insert(0,"0")
			try:
				Spin_list_ranges_max[cnt].insert(0,config.get("ranges",("max_"+str(cnt))))
			except:
				Spin_list_ranges_max[cnt].insert(0,"1000")
			cnt=cnt+1
			cnt2=cnt2+1

		os1=68
		name_label_3=tk.Label(self, text ="Point            Min            Max",
						bg="gray",font = MEDIUMFONT)
		name_label_3.place(x=xx(os1+3), y=yy(12)) 
		cnt2=0
		for label in Label_list3:
			Labels.append(tk.Label(self, text =label,font = MEDIUMFONT))
			Labels[cnt].place(x=xx(os1+3), y=yy(18+cnt2*8))
			Spin_list_ranges_min.append(tk.Spinbox(self, width=ww(6),font=MEDIUMFONT))
			Spin_list_ranges_min[cnt].place(x=xx(os1+13), y=yy(18+cnt2*8))
			Spin_list_ranges_max.append(tk.Spinbox(self, width=ww(6),font=MEDIUMFONT))
			Spin_list_ranges_max[cnt].place(x=xx(os1+23), y=yy(18+cnt2*8))
			try:
				Spin_list_ranges_min[cnt].insert(0,config.get("ranges",("min_"+str(cnt))))	
			except:
				Spin_list_ranges_min[cnt].insert(0,"0")
			try:		
				Spin_list_ranges_max[cnt].insert(0,config.get("ranges",("max_"+str(cnt))))
			except:
				Spin_list_ranges_max[cnt].insert(0,"1000")

			cnt=cnt+1
			cnt2=cnt2+1

		Labels.append(tk.Label(self, text ="Phone:",font = MEDIUMFONT))
		Labels[cnt].place(x=xx(os1+3), y=yy(20+cnt2*8))
		Phone_entry.append(tk.Entry(self, width=ww(14),font=MEDIUMFONT))
		Phone_entry[0].place(x=xx(os1+13), y=yy(20+cnt2*8))
		try:
			Phone_entry[0].insert(0,config.get("ranges",("phone")))
		except:
			Phone_entry[0].insert(0,"09394444444")



		Save_Button=tk.Button(self, text ="Save",bg = 
		"azure2",width=ww(15),height=hh(7),
			command = Save_ranges)
		Save_Button.place(x=xx(42), y=yy(3))

		Exit_Button = tk.Button(self, text ="Home",bg = "azure2",width=ww(6),height=hh(5),
			command = lambda : controller.show_frame(StartPage))
		Exit_Button.place(x=xx(5), y=yy(3))



GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_Ras2Holtek_1, GPIO.OUT) 
GPIO.setup(GPIO_Ras2Holtek_2, GPIO.OUT)  
GPIO.setup(GPIO_H_ExtTrigger, GPIO.OUT)  
GPIO.setup(GPIO_H_check_out, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(GPIO_ESP_EN ,GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(GPIO_ESP_RST, GPIO.IN, pull_up_down=GPIO.PUD_UP)   

init_scale()
app = tkinterApp()
app.mainloop()




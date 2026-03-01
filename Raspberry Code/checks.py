#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
import threading
import os
import time
import json



from ranges import *
from tests import *


Test_Tread=threading.Thread()


def Create_Frame(str):
	global LARGEFONT
	top = tk.Tk()
	top.title("Check test result")
	top.attributes('-fullscreen',True)
	back_btn = tk.Button(top, text ="Back",bg = "azure2",width=ww(6),height=hh(10),
				command = lambda : top.destroy())
	back_btn.place(x=xx(5), y=yy(90))	
	label = tk.Label(top, text =str, font = LARGEFONT)
	label.place(x=xx(3), y=yy(3))	
	return top


def Test_Check(index):

	if index >1 and Serial_label[1]=="":
		# messagebox.showinfo("Error!", "You must do the SerialNumber test first!")
		# return
		Serial_label[1]="device1"
		Serial_label[0].config(text = "SN: "+Serial_label[1])
	Test_check_list[index]()



def Program_c():
	global MEDIUMFONT

	fr=Create_Frame("Program test results:")
	Label_list1=["Holtek 1:","Holtek 2:","ESP:","STM:"]
	Labels=[]
	values=[]
	

	config = configparser.ConfigParser()  
	config.read('results.ini')

	program_value=config.get(Serial_label[1],"program_value")
	program_result=config.get(Serial_label[1],"program_result")

	program_result=json.loads(program_result)
	program_value=json.loads(program_value)


	cnt=0

	for label in Label_list1:
		Labels.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		Labels[cnt].place(x=xx(3), y=yy(23+cnt*8))

		if program_result[cnt]==1:
			values.append(tk.Label(fr, text =program_value[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[cnt].place(x=xx(23), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =program_value[cnt],font = MEDIUMFONT,bg="red"))
			values[cnt].place(x=xx(23), y=yy(23+cnt*8))
		cnt=cnt+1

	fr.mainloop()


def Supply_c():
	global MEDIUMFONT
	fr=Create_Frame("Power supply test results:")

	Label_list1=["V 13.5:","V 4.0:","V 5.0:","V 3.3_1:","V 3.3_2:","V 15.0:","V AC:",
			   "V BAT:"]
	Labels=[]
	values=[]
	cnt=0

	config = configparser.ConfigParser()  
	config.read('results.ini')

	v=config.get(Serial_label[1],"supply_value")
	r=config.get(Serial_label[1],"supply_result")
	read_power_results=json.loads(r)
	read_power_values=json.loads(v)


	for label in Label_list1:
		Labels.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		Labels[cnt].place(x=xx(3), y=yy(13+cnt*8))

		if read_power_results[cnt]==1:

			values.append(tk.Label(fr, text =read_power_values[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[cnt].place(x=xx(15), y=yy(13+cnt*8))
		else:
			values.append(tk.Label(fr, text =read_power_values[cnt],font = MEDIUMFONT,bg="red"))
			values[cnt].place(x=xx(15), y=yy(13+cnt*8))
		cnt=cnt+1
	fr.mainloop()


def SerialNumber_c():
	print("hi")
	


def Outputs_c():
	global MEDIUMFONT
	fr=Create_Frame("Outputs test results:")

	Label_list1=["Output 1:","Output 2:","Output 3:","Output 4:"]
	Labels=[]
	values=[]
	cnt=0

	config = configparser.ConfigParser()  
	config.read('results.ini')

	v=config.get(Serial_label[1],"output_value")
	r=config.get(Serial_label[1],"output_result")
	read_power_results=json.loads(r)
	read_power_values=json.loads(v)


	for label in Label_list1:
		Labels.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		Labels[cnt].place(x=xx(3), y=yy(13+cnt*8))

		if read_power_results[cnt]==1:

			values.append(tk.Label(fr, text =read_power_values[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[cnt].place(x=xx(15), y=yy(13+cnt*8))
		else:
			values.append(tk.Label(fr, text =read_power_values[cnt],font = MEDIUMFONT,bg="red"))
			values[cnt].place(x=xx(15), y=yy(13+cnt*8))
		cnt=cnt+1
	fr.mainloop()



def InputsZones_c():
	global MEDIUMFONT
	fr=Create_Frame("Zone/Input test results:")

	Label_list1=["Zone 1:","Zone 2:","Zone 3:","Zone 4:","Zone 5:"]
	
	Labels=[]
	values=[]
	values2=[]
	cnt=0

	config = configparser.ConfigParser()  
	config.read('results.ini')

	value_stm=config.get(Serial_label[1],"zone_value_stm")
	result_stm=config.get(Serial_label[1],"zone_result_stm")
	value_esp=config.get(Serial_label[1],"zone_value_esp")
	result_esp=config.get(Serial_label[1],"zone_result_esp")

	stm_results=json.loads(result_stm)
	stm_values=json.loads(value_stm)

	esp_values=json.loads(value_esp)
	esp_results=json.loads(result_esp)


	l1=tk.Label(fr, text ="STM",font = MEDIUMFONT)
	l1.place(x=xx(15), y=yy(15))
	
	l2=tk.Label(fr, text ="ESP",font = MEDIUMFONT)
	l2.place(x=xx(30), y=yy(15))


	for label in Label_list1:
		Labels.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		Labels[cnt].place(x=xx(3), y=yy(23+cnt*8))

		if stm_results[cnt]==1:
			values.append(tk.Label(fr, text =stm_values[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[cnt].place(x=xx(15), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =stm_values[cnt],font = MEDIUMFONT,bg="red"))
			values[cnt].place(x=xx(15), y=yy(23+cnt*8))

		if esp_results[cnt]==1:
			values2.append(tk.Label(fr, text =esp_values[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values2[cnt].place(x=xx(30), y=yy(23+cnt*8))
		else:
			values2.append(tk.Label(fr, text =esp_values[cnt],font = MEDIUMFONT,bg="red"))
			values2[cnt].place(x=xx(30), y=yy(23+cnt*8))
		
		cnt=cnt+1
	fr.mainloop()
	
	


def Audio_c():
	fr=Create_Frame("Audio test results:")

	Label_list1=["SP1 F1:","SP1 F2:","SP1 F3:","SP2 F1:","SP2 F2:","SP2 F3:"]
	
	Labels=[]
	cols=[]

	cnt=0

	config = configparser.ConfigParser()  
	config.read('results.ini')

	values_esp=config.get(Serial_label[1],"Audio_values_esp")
	values_stm_holtek=config.get(Serial_label[1],"Audio_values_holtek")
	values_stm_signal=config.get(Serial_label[1],"Audio_values_signal")
	values_stm_present=config.get(Serial_label[1],"Audio_values_present")
	values_stm_speaker=config.get(Serial_label[1],"Audio_values_speaker")
	values_stm_siren=config.get(Serial_label[1],"Audio_values_siren")

	results_esp=config.get(Serial_label[1],"Audio_result_esp")
	results_stm_holtek=config.get(Serial_label[1],"Audio_result_holtek")
	results_stm_signal=config.get(Serial_label[1],"Audio_result_signal")
	results_stm_present=config.get(Serial_label[1],"Audio_result_present")
	results_stm_speaker=config.get(Serial_label[1],"Audio_result_speaker")
	results_stm_siren=config.get(Serial_label[1],"Audio_result_siren")

	result_user=config.get(Serial_label[1],"Audio_result_user")


	values_esp=json.loads(values_esp)
	values_stm_holtek=json.loads(values_stm_holtek)
	values_stm_signal=json.loads(values_stm_signal)
	values_stm_present=json.loads(values_stm_present)
	values_stm_speaker=json.loads(values_stm_speaker)
	values_stm_siren=json.loads(values_stm_siren)

	results_esp=json.loads(results_esp)
	results_stm_holtek=json.loads(results_stm_holtek)
	results_stm_signal=json.loads(results_stm_signal)
	results_stm_present=json.loads(results_stm_present)
	results_stm_speaker=json.loads(results_stm_speaker)
	results_stm_siren=json.loads(results_stm_siren)

	result_user=json.loads(result_user)


	col_list=["ESP","Holtek","Signal","Present","Speaker","Operator"]

	cnt=0
	for label in col_list:
		cols.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		cols[cnt].place(x=xx(15+cnt*14), y=yy(15))
		cnt=cnt+1


	values=[]

	cnt=0	
	ind=0
	for label in Label_list1:
		Labels.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		Labels[cnt].place(x=xx(3), y=yy(23+cnt*8))
		col=0

		if results_esp[cnt]==1:
			values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))

		col=col+1
		ind=ind+1


		if results_stm_holtek[cnt]==1:
			values.append(tk.Label(fr, text =values_stm_holtek[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =values_stm_holtek[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))

		col=col+1
		ind=ind+1

		if results_stm_signal[cnt]==1:
			values.append(tk.Label(fr, text =values_stm_signal[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =values_stm_signal[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))

		col=col+1
		ind=ind+1

		if results_stm_present[cnt]==1:
			values.append(tk.Label(fr, text =values_stm_present[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =values_stm_present[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))

		col=col+1
		ind=ind+1

		if results_stm_speaker[cnt]==1:
			values.append(tk.Label(fr, text =values_stm_speaker[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =values_stm_speaker[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))

		col=col+1
		ind=ind+1
		if result_user[cnt]==1:
			values.append(tk.Label(fr, text ="Yes",font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text ="No",font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))

		col=col+1
		ind=ind+1
		cnt=cnt+1


	Labels.append(tk.Label(fr, text ="Siren:",font = MEDIUMFONT))
	Labels[cnt].place(x=xx(3), y=yy(23+cnt*8))
	col=0

	if results_esp[cnt]==1:
		values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="lightgreen"))
		values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))
	else:
		values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="red"))
		values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))

	col=col+2
	ind=ind+1

	if results_stm_siren[0]==1:
		values.append(tk.Label(fr, text =values_stm_siren[0],font = MEDIUMFONT,bg="lightgreen"))
		values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))
	else:
		values.append(tk.Label(fr, text =values_stm_signal[0],font = MEDIUMFONT,bg="red"))
		values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))

	col=col+3
	ind=ind+1

	if result_user[cnt]==1:
		values.append(tk.Label(fr, text ="Yes",font = MEDIUMFONT,bg="lightgreen"))
		values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))
	else:
		values.append(tk.Label(fr, text ="No",font = MEDIUMFONT,bg="red"))
		values[ind].place(x=xx(15+col*14), y=yy(23+cnt*8))
	
	

	fr.mainloop()




def Dummy_c():
	global MEDIUMFONT
	fr=Create_Frame("Dummy test results:")

	Label_list1=["Dummy 1","Dummy 2"]
	Labels=[]
	values=[]
	

	config = configparser.ConfigParser()  
	config.read('results.ini')

	values_stm1=config.get(Serial_label[1],"Dummy_value_stm_1")
	results_stm1=config.get(Serial_label[1],"Dummy_result_stm_1")
	values_stm2=config.get(Serial_label[1],"Dummy_value_stm_2")
	results_stm2=config.get(Serial_label[1],"Dummy_result_stm_2")

	values_stm1=json.loads(values_stm1)
	results_stm1=json.loads(results_stm1)
	values_stm2=json.loads(values_stm2)
	results_stm2=json.loads(results_stm2)

	cnt=0
	ind=0


	l1=tk.Label(fr, text ="Vb1",font = MEDIUMFONT)
	l1.place(x=xx(23), y=yy(15))
	
	l2=tk.Label(fr, text ="Vb2",font = MEDIUMFONT)
	l2.place(x=xx(43), y=yy(15))

	for label in Label_list1:
		Labels.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		Labels[cnt].place(x=xx(3), y=yy(23+cnt*8))

		if results_stm1[cnt]==1:
			values.append(tk.Label(fr, text =values_stm1[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(23+cnt*20), y=yy(23))
		else:
			values.append(tk.Label(fr, text =values_stm1[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(23+cnt*20), y=yy(23))

		ind=ind+1
		if results_stm2[cnt]==1:
			values.append(tk.Label(fr, text =values_stm2[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(23+cnt*20), y=yy(32))
		else:
			values.append(tk.Label(fr, text =values_stm2[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(23+cnt*20), y=yy(32))
		
		cnt=cnt+1
		ind=ind+1


	fr.mainloop()



def ShortCircuits_c():
	global MEDIUMFONT
	fr=Create_Frame("Short circuit test results:")

	Label_list1=["speaker1","speaker2","external voltage","siren","battery"]
	Labels=[]
	values=[]
	

	config = configparser.ConfigParser()  
	config.read('results.ini')

	values_stm=config.get(Serial_label[1],"shortcircuit_value_stm")
	results_stm=config.get(Serial_label[1],"shortcircuit_result_stm")
	values_esp=config.get(Serial_label[1],"shortcircuit_value_esp")
	results_esp=config.get(Serial_label[1],"shortcircuit_result_esp")

	values_stm=json.loads(values_stm)
	results_stm=json.loads(results_stm)
	values_esp=json.loads(values_esp)
	results_esp=json.loads(results_esp)

	cnt=0
	ind=0


	l1=tk.Label(fr, text ="STM",font = MEDIUMFONT)
	l1.place(x=xx(23), y=yy(15))
	
	l2=tk.Label(fr, text ="ESP",font = MEDIUMFONT)
	l2.place(x=xx(43), y=yy(15))


	for label in Label_list1:
		Labels.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		Labels[cnt].place(x=xx(3), y=yy(23+cnt*8))

		if results_stm[cnt]==1:
			values.append(tk.Label(fr, text =values_stm[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(23), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =values_stm[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(23), y=yy(23+cnt*8))

		ind=ind+1
		if results_esp[cnt]==1:
			values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(43), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(43), y=yy(23+cnt*8))
		cnt=cnt+1
		ind=ind+1

	fr.mainloop()
	


def Battery_c():
	global MEDIUMFONT
	fr=Create_Frame("Battery test results:")

	Label_list1=["Battery in","Battery out"]
	Labels=[]
	values=[]
	

	config = configparser.ConfigParser()  
	config.read('results.ini')

	values_stm=config.get(Serial_label[1],"battery_value_stm")
	results_stm=config.get(Serial_label[1],"battery_result_stm")
	values_esp=config.get(Serial_label[1],"battery_value_esp")
	results_esp=config.get(Serial_label[1],"battery_result_esp")

	values_stm=json.loads(values_stm)
	results_stm=json.loads(results_stm)
	values_esp=json.loads(values_esp)
	results_esp=json.loads(results_esp)

	cnt=0
	ind=0


	l1=tk.Label(fr, text ="STM",font = MEDIUMFONT)
	l1.place(x=xx(23), y=yy(15))
	
	l2=tk.Label(fr, text ="ESP",font = MEDIUMFONT)
	l2.place(x=xx(43), y=yy(15))

	l3=tk.Label(fr, text ="Precentage",font = MEDIUMFONT)
	l3.place(x=xx(63), y=yy(15))

	for label in Label_list1:
		Labels.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		Labels[cnt].place(x=xx(3), y=yy(23+cnt*8))

		if results_stm[cnt]==1:
			values.append(tk.Label(fr, text =values_stm[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(23), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =values_stm[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(23), y=yy(23+cnt*8))

		ind=ind+1
		if results_esp[cnt]==1:
			values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(43), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(43), y=yy(23+cnt*8))
		cnt=cnt+1
		ind=ind+1
	
	values.append(tk.Label(fr, text =values_esp[2],font = MEDIUMFONT,bg="yellow"))
	values[ind].place(x=xx(63), y=yy(23))

	fr.mainloop()
	


def GSM_c():
	global MEDIUMFONT
	fr=Create_Frame("Short circuit test results:")

	Label_list1=["init:","get time:","SMS:","Call:"]
	Labels=[]
	values=[]
	

	config = configparser.ConfigParser()  
	config.read('results.ini')

	values_stm=config.get(Serial_label[1],"gsm_values_stm")
	results_stm=config.get(Serial_label[1],"gsm_results_stm")
	values_esp=config.get(Serial_label[1],"gsm_values_esp")
	results_esp=config.get(Serial_label[1],"gsm_results_esp")
	results_user=config.get(Serial_label[1],"gsm_results_user")



	values_stm=json.loads(values_stm)
	results_stm=json.loads(results_stm)
	values_esp=json.loads(values_esp)
	results_esp=json.loads(results_esp)
	results_user=json.loads(results_user)

	cnt=0
	ind=0


	l1=tk.Label(fr, text ="ESP:",font = MEDIUMFONT)
	l1.place(x=xx(23), y=yy(15))
	
	l2=tk.Label(fr, text ="Operator:",font = MEDIUMFONT)
	l2.place(x=xx(43), y=yy(15))

	l2=tk.Label(fr, text ="STM:",font = MEDIUMFONT)
	l2.place(x=xx(63), y=yy(15))


	for label in Label_list1:
		Labels.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		Labels[cnt].place(x=xx(3), y=yy(23+cnt*8))

		if results_esp[cnt]==1:			
			values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(23), y=yy(23+cnt*8))
		else:			
			values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(23), y=yy(23+cnt*8))

		if cnt>1:
			ind=ind+1
			if results_user[cnt-2]==1:
				values.append(tk.Label(fr, text ="Yes",font = MEDIUMFONT,bg="lightgreen"))
				values[ind].place(x=xx(43), y=yy(23+cnt*8))
			else:
				values.append(tk.Label(fr, text ="No",font = MEDIUMFONT,bg="red"))
				values[ind].place(x=xx(43), y=yy(23+cnt*8))
		cnt=cnt+1
		ind=ind+1
	
	cnt=cnt-1
	if results_stm[0]==1:
		values.append(tk.Label(fr, text =values_stm[0],font = MEDIUMFONT,bg="lightgreen"))
		values[ind].place(x=xx(63), y=yy(23+cnt*8))
	else:
		values.append(tk.Label(fr, text =values_stm[0],font = MEDIUMFONT,bg="red"))
		values[ind].place(x=xx(63), y=yy(23+cnt*8))

	fr.mainloop()


	



def operator_c():
	global MEDIUMFONT
	fr=Create_Frame("Short circuit test results:")

	Label_list1=["LED on:","LED off:","7Segment:","Key:"]
	Labels=[]
	values=[]
	

	config = configparser.ConfigParser()  
	config.read('results.ini')

	values_stm=config.get(Serial_label[1],"operator_values_stm")
	results_stm=config.get(Serial_label[1],"operator_results_stm")
	values_esp=config.get(Serial_label[1],"operator_value_esp")
	results_esp=config.get(Serial_label[1],"operator_results_esp")
	results_user=config.get(Serial_label[1],"operator_results_user")


	values_stm=json.loads(values_stm)
	results_stm=json.loads(results_stm)
	values_esp=json.loads(values_esp)
	results_esp=json.loads(results_esp)
	results_user=json.loads(results_user)

	cnt=0
	ind=0


	l1=tk.Label(fr, text ="Operator",font = MEDIUMFONT)
	l1.place(x=xx(23), y=yy(15))
	
	l2=tk.Label(fr, text ="ESP",font = MEDIUMFONT)
	l2.place(x=xx(43), y=yy(15))

	l2=tk.Label(fr, text ="STM",font = MEDIUMFONT)
	l2.place(x=xx(63), y=yy(15))


	for label in Label_list1:
		Labels.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		Labels[cnt].place(x=xx(3), y=yy(23+cnt*8))

		if results_user[cnt]==1:
			values.append(tk.Label(fr, text ="Yes",font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(23), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text ="No",font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(23), y=yy(23+cnt*8))

		ind=ind+1
		if results_esp[cnt]==1:
			values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[ind].place(x=xx(43), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =values_esp[cnt],font = MEDIUMFONT,bg="red"))
			values[ind].place(x=xx(43), y=yy(23+cnt*8))
		cnt=cnt+1
		ind=ind+1
	
	cnt=cnt-1
	if results_stm[0]==1:
		values.append(tk.Label(fr, text =values_stm[0],font = MEDIUMFONT,bg="lightgreen"))
		values[ind].place(x=xx(63), y=yy(23+cnt*8))
	else:
		values.append(tk.Label(fr, text =values_stm[0],font = MEDIUMFONT,bg="red"))
		values[ind].place(x=xx(63), y=yy(23+cnt*8))

	fr.mainloop()
	


def Function1_c():
	print("hi")



def Function2_c():
	print("hi")



def Function3_c():
	print("hi")



def Temperature_c():
	print("hi")



def Remote_c():
	print("hi")



def SoundGSM2_c():
	print("hi")



def FactorySet_c():
	global MEDIUMFONT

	fr=Create_Frame("Factory test results:")
	Label_list1=["Time read:","Save serial:","File set:"]
	Labels=[]
	values=[]
	

	config = configparser.ConfigParser()  
	config.read('results.ini')

	factory_value=config.get(Serial_label[1],"factory_value")
	factory_result=config.get(Serial_label[1],"factory_result")

	factory_result=json.loads(factory_result)
	factory_value=json.loads(factory_value)


	cnt=0

	for label in Label_list1:
		Labels.append(tk.Label(fr, text =label,font = MEDIUMFONT))
		Labels[cnt].place(x=xx(3), y=yy(23+cnt*8))

		if factory_result[cnt]==1:
			values.append(tk.Label(fr, text =factory_value[cnt],font = MEDIUMFONT,bg="lightgreen"))
			values[cnt].place(x=xx(23), y=yy(23+cnt*8))
		else:
			values.append(tk.Label(fr, text =factory_value[cnt],font = MEDIUMFONT,bg="red"))
			values[cnt].place(x=xx(23), y=yy(23+cnt*8))
		cnt=cnt+1

	fr.mainloop()





Test_check_list=[Program_c,SerialNumber_c,Supply_c,Outputs_c,InputsZones_c,Audio_c
,Dummy_c,ShortCircuits_c,Battery_c,GSM_c,operator_c,Function1_c
,Function2_c,Function3_c,Temperature_c,Remote_c,SoundGSM2_c,FactorySet_c]


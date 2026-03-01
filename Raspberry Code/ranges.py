import configparser
from tkinter import messagebox

Spin_list_ranges_min = []
Spin_list_ranges_max = []
Spin_list_timeouts=[]
Phone_entry=[]


def Save_ranges():

    if(messagebox.askokcancel("Save ranges", "Do you Want to Save?")):
        # Create an instance of the ConfigParser class
        config = configparser.ConfigParser()  
        config.read('config.ini')

        try:
            config.add_section("ranges")
        except:
            pass
        
        cnt=0
        for min in Spin_list_ranges_min:
            option="min_"+str(cnt)
            config.set("ranges",option,min.get())
            cnt+=1

        cnt=0
        for max in Spin_list_ranges_max:
            option="max_"+str(cnt)
            config.set("ranges",option,max.get())
            cnt+=1

        config.set("ranges","phone",Phone_entry[0].get())
            
        # Saving changes
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        
        messagebox.showinfo("notice","Configurations Saved Successfully!")


def Save_timeouts():

    if(messagebox.askokcancel("Save timeouts", "Do you Want to Save?")):
        # Create an instance of the ConfigParser class
        config = configparser.ConfigParser() 
        config.read('config.ini') 

        try:
            config.add_section("timeouts")
        except:
            pass

        cnt=0

        for tim in Spin_list_timeouts:
            option="time_"+str(cnt)
            config.set("timeouts",option,tim.get())
            cnt+=1

            
        # Saving changes
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        
        messagebox.showinfo("notice","Configurations Saved Successfully!")
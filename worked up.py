# Unit GUI Assignment 
# brayden patershuk 
# Date: 5/25/2022 
# GUI age calculator 
#https://www.spriters-resource.com/ds_dsi/marioluigipartners/sheet/44758/

Jan=1
Feb=2
Mar=3
Apr=4
May=5
Jun=6
Jul=7
Aug=8
Sep=9
Oct=10
Nov=11
Dec=12

def echo(event):
    if month.get() == "Month":
        print("error - Enter a valid month")  


    else:
        print(entry.get(),year.get(),month.get(),day.get())
        AGE=int(Cyear.get())-int(year.get())
        if int(month.get()) > int(Cmonth.get()):
            if int(Cday.get())>int(day.get()):
                AGE-=1
                print('your age is',AGE)
            else:    
                print('your age is',AGE)
            
        else:    
            print('your age is',AGE)


   


from tkinter import  *      # std tkinter package
from tkinter import ttk     # ttk module 

root=Tk()
root.title("AGE CALCULATOR")
root.geometry("760x100+500+400")
root.attributes('-topmost', 1)


mo="dec"

lbl_Title=ttk.Label(root,text="NAME",justify=LEFT).pack(side=LEFT)

entry=ttk.Entry(root,width=10, justify=LEFT) 
entry.pack(side=LEFT)
entry.focus_set()

btn_Echo=ttk.Button(root,text="Submit")

btn_Echo.bind("<Button-1>",echo)
btn_Echo.pack(side=RIGHT,anchor='se')

lbl_Title=ttk.Label(root,text="year",justify=LEFT).pack(side=LEFT)
year=ttk.Entry(root,width=4, justify=LEFT) 
year.pack(side=LEFT)
year.focus_set()
#this whole thing is so bad
month = StringVar()
combobox = ttk.Combobox(root, textvariable = month, width=10)
combobox.pack(side=LEFT,padx=20)
combobox.config(values = (Jan, Feb, Mar, Apr, May, Jun,
                          Jul, Aug, Sep, Oct, Nov, Dec))

month.set('Month')   


combobox.bind('<<ComboboxSelected>>')   


lbl_Title=ttk.Label(root,text="day",justify=LEFT).pack(side=LEFT)
day=ttk.Entry(root,width=4, justify=LEFT) 
day.pack(side=LEFT)
day.focus_set()

lbl_Title=ttk.Label(root,text="current year",justify=LEFT).pack(side=LEFT)
Cyear=ttk.Entry(root,width=4, justify=LEFT) 
Cyear.pack(side=LEFT)
Cyear.focus_set()

#this was strange
lbl_Title=ttk.Label(root,text="current day",justify=LEFT).pack(side=LEFT)
Cday=ttk.Entry(root,width=4, justify=LEFT) 
Cday.pack(side=LEFT)
Cday.focus_set()

#dont know if this needed to be a combo box?
Cmonth = StringVar()
combobox = ttk.Combobox(root, textvariable = Cmonth, width=10)
combobox.pack(side=LEFT,padx=20)
combobox.config(values = (Jan, Feb, Mar, Apr, May, Jun,
                          Jul, Aug, Sep, Oct, Nov, Dec))

Cmonth.set('current Month')   


combobox.bind('<<ComboboxSelected>>')   


lblMsg = ttk.Label(root, text = "TIME FOR FUN")
lblMsg.pack(side=RIGHT)

logo=PhotoImage(file = './baby luigi.png') 
lblMsg.config(image = logo)    

root.mainloop()             # enter the event loop

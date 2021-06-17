import tkinter
import os

mainWindow = tkinter.Tk()
mainWindow.title("Grid Demo")
mainWindow.geometry('600x420-8-200')
mainWindow['padx'] = 8

photo = tkinter.PhotoImage(file = 'yeahboi.png')

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo", bg='black', font=10, fg='white')
label.grid(row=0, column=0, columnspan=3)

label2 = tkinter.Label(
    image=photo
)
label2.place(x=-40, y=-40)

mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken', bg='black', fg='white')

# FILE LIST WITH SCROLLBAR
for zone in os.listdir('C:/Users/laksh/Downloads'):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='NSW', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# FRAME FOR RADIO BUTTONS
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details",
                                 bd=3, labelanchor='n',
                                 relief='groove')
optionFrame.grid(row=1, column=2, sticky='NE')

rbValue = tkinter.IntVar()
rbValue.set(1)

#Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue,
                             indicatoron=0, width=10)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue,
                             indicatoron=0, width=10)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue,
                             indicatoron=0, width=10)
radio1.grid(column=0, row=0, sticky='w')
radio2.grid(column=0, row=1, sticky='w')
radio3.grid(column=0, row=2, sticky='w')
optionFrame['padx'] = 5

#   WIDGET TO DISPLAY THE RESULT
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='NE')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='SE')

#   FRAME FOR THE TIME SPINNERS
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='NEW')
#   TIME SPINNERS
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=2, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=2, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=":").grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=":").grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

#   FRAME FOR THE DATE SPINNERS
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='NEW')
#   DATE LABELS
dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")
dayLabel.grid(row=0, column=0, sticky='W')
monthLabel.grid(row=0, column=1, sticky='W')
yearLabel.grid(row=0, column=2, sticky='W')
#   DATE SPINNERS
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May",
                                                        "Jun", "Jul", "Aug", "Sep", "Oct",
                                                        "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

#   END BUTTONS
okButton = tkinter.Button(mainWindow, text="OK")
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.quit)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()

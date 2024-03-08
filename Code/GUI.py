# import datetime
import tkinter as tk
from tkinter import ttk
from GoogleAPI import getCalendarEvents
from ParseData import ParseList


# pass ParseData in as argument for class
class HabitApp:

    # Initializes the Tkinter window
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.title('Habit App')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        # Creating title for window
        self.text = ttk.Label(self.mainframe, text='Change Your Habits, Change Your Life!', background='white',
                              font=("Brass Mono", 13))
        self.text.grid(row=0, column=0)

        # Creates instruction for the user to either add event or view report of future tasks
        self.events_label = ttk.Label(self.mainframe, text='Select an Option', background='white',
                                      font=("Brass Mono", 10))
        self.events_label.grid(row=1, column=2, columnspan=1, pady=10, sticky='NWES')

        # Creates buttons which when clicks runs function in HabitApp class
        self.report_button = ttk.Button(self.mainframe, text='Event Report', command=self.report)
        self.report_button.grid(row=3, column=1, pady=10)

        #Function was not listed in our documentation but wanted to add some other feature ideas for app
        self.add_event_button = ttk.Button(self.mainframe, text='Add Event', command=self.add_event)
        self.add_event_button.grid(row=3, column=3, pady=10)

        self.root.mainloop()
        return

    # report function will generate a new window to generate all tasks
    """Apologises we had planned on generate the data in a tasks for the day, tasks for the week
     and tasks for the month format but lost track of time and was more complicated than we initially thought"""
    def report(self):
        report_window = tk.Toplevel(self.root)
        report_window.title("Event Report")
        report_frame = tk.Frame(report_window)
        report_frame.pack()

        # Print all Events from Dll in the Event Report window
        for index, event in enumerate(Dll):
            event_label = ttk.Label(report_frame, text=f"{index + 1}, {event.getName()}, {event.getDateTime()}")
            event_label.pack()

        # Creates button to close window
        close_button = ttk.Button(report_frame, text="Close", command=report_window.destroy)
        close_button.pack()

    def add_event(self):
        print("Still in development")


# Grabs GoogleData list from GoogleAPI class
GoogleData = getCalendarEvents()

# Uses ParseList Function from ParseData class to parse GoogleData list and store in Event objects in a DoublyLinkedList
Dll = ParseList(GoogleData)

#Runs class to open HabitApp GUI
HabitApp()

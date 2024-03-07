#from ParseData import main
import tkinter as tk
from tkinter import ttk


# pass ParseData in as argument for class
class HabitApp():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x300')
        self.root.title('Habit App')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        self.text = ttk.Label(self.mainframe, text='Change Your Habits, Change Your Life!', background='white', font=("Brass Mono", 13))
        self.text.grid(row=0, column=0)

        self.events_label = ttk.Label(self.mainframe, text='Events:', background='white', font=("Brass Mono", 10))
        self.events_label.grid(row=1, column=0, pady=10, sticky='NWES')

        # ParseData object goes here, but only with (name, time) arguments in the text area
        self.events_brief = ttk.Label(self.mainframe, text='googleData(name, date)', background='white', font=("Brass Mono", 10))
        self.events_brief.grid(row=2, column=0, pady=10, sticky='NWES')

        self.report_button = ttk.Button(self.mainframe, text='Event Report', command=self.report)
        self.report_button.grid(row=3, column=0, pady=10)
        self.root.mainloop()
        return

    def report(self):
        # ParseData object goes in the print statement
        print("googleData")


if __name__ == '__main__':
    HabitApp()

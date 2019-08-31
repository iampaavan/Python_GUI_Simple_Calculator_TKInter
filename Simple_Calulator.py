from tkinter import *


class Calculator:

    def __init__(self, my_attr):
        self.my_attr = my_attr
        my_attr.title('My Basic Python Calculator')

        # create screen widget
        self.screen = Text(my_attr, state='disabled', width=30, height=3, background='yellow', foreground='blue')

        # position screen in window
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.screen.configure(state='normal')

        # initialize screen as empty
        self.equation = ''

        # create buttons using createButton method
        button_1 = self.createButton(7)
        button_2 = self.createButton(8)
        button_3 = self.createButton(9)
        button_4 = self.createButton(u"\u232B", None)
        button_5 = self.createButton(4)
        button_6 = self.createButton(5)
        button_7 = self.createButton(6)
        button_8 = self.createButton(u"\u00F7")
        button_9 = self.createButton(1)
        button_10 = self.createButton(2)
        button_11 = self.createButton(3)
        button_12 = self.createButton('*')
        button_13 = self.createButton('.')
        button_14 = self.createButton(0)
        button_15 = self.createButton('+')
        button_16 = self.createButton('-')
        button_17 = self.createButton('=', None, 34)

        # buttons stored in a list
        buttons = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12,
                  button_13, button_14, button_15, button_16, button_17]

        # initialize the counter
        count = 0

        # arrange buttons with grid manager
        for row in range(1, 5):
            for column in range(4):
                buttons[count].grid(row=row, column=column)
                count += 1

        # arrange '=' button at the bottom
        buttons[16].grid(row=5, column=0, columnspan=4)

    def createButton(self, value, write=True, width=7):
        # function creates a button, and takes one compulsory argument, the value that should be on the button
        return Button(self.my_attr, text=value, command=lambda:self.click(value, write), width=width)

    def click(self, text, write):
        # this function handles what happens when you click a button
        # 'write' argument if True means the value 'value' should be written on the screen,
        # if None, should not be written

        if write is None:
            # Only evaluate code when there is an equation to be evaluated
            if text == '=' and self.equation:
                # replace the unicode value of division ./. with python division (/) using regex
                self.equation = re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                print(answer)
                self.clear_screen()
                self.insert_screen(answer, newline=True)

            elif text == u"\u232B":
                self.clear_screen()

        else:
            # add text to the screen
            self.insert_screen(text)

    def clear_screen(self):
        # to clear screen
        # set the equation to empty before deleting screen
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END, value)

        # record every value inserted in the screen
        self.equation += str(value)
        self.screen.configure(state='disabled')


my_tkinter = Tk()
calc_gui = Calculator(my_tkinter)
my_tkinter.mainloop()


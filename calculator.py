from tkinter import * #python version 3.11.1
from tkinter import messagebox #importing message box to show error message

cal = Tk()
cal.geometry("312x394") #size of the calculator 
cal.resizable(0, 0)
cal.title("Calculator") #title of the application 

def click_button(item):
    global expression
    inputText.set(inputText.get() + (str(item)))  # Concatenates the clicked button's value to the expression

def clear_button():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])  # Removes the last character from the expression

def clear_all():
    inputText.set("")  # Clears the entire expression

def equal_button():
    result = ""
    try:
        result = eval(inputText.get())  # Evaluates the expression and stores the result
        inputText.set(result)  # Displays the result in the input field
    except:
        result = "_ERROR_"
        messagebox.showerror("Invalid Input", "Please enter a valid arithmetic expression.")

expression = ""  # Stores the arithmetic expression
inputText = StringVar()  # Variable to store the text displayed in the input field

# Create a frame for the input field
inputFrame = Frame(cal, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="blue", highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 19), textvariable=inputText, width=50, fg="black", bg="white", bd=0, justify=RIGHT) # Create an entry field for the input
inputField.grid(row=0, column=0)
inputField.pack(ipady=19)

# Button Frame
button_frame = Frame(cal, width=312, height=272.5, bg="grey")
button_frame.pack()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Buttons>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# First row
clearall = Button(button_frame, text="C", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: clear_all()).grid(row=1, column=0, padx=1, pady=1)
l_bracket = Button(button_frame, text="(", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: click_button("(")).grid(row=1, column=1, padx=1, pady=1)
r_bracket = Button(button_frame, text=")", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: click_button(")")).grid(row=1, column=2, padx=1, pady=1)
clear = Button(button_frame, text="<", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=lambda: clear_button()).grid(row=1, column=3, padx=1, pady=1)
#Second_row
power = Button(button_frame, text = "^", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("**")).grid(row = 2, column = 0, padx = 1, pady = 1)
pie = Button(button_frame, text = "π", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(3.1415)).grid(row = 2, column = 1, padx = 1, pady = 1)
exp  = Button(button_frame, text = "e", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(2.7182)).grid(row = 2, column = 2, padx = 1, pady = 1)
divide_= Button(button_frame, text = "/", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("/")).grid(row = 2, column = 3, padx = 1, pady = 1)

#Third_row
seven = Button(button_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(7)).grid(row = 3, column = 0, padx = 1, pady = 1)
eight = Button(button_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(8)).grid(row = 3, column = 1, padx = 1, pady = 1)
nine = Button(button_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(9)).grid(row = 3, column = 2, padx = 1, pady = 1)
multiply = Button(button_frame, text = "*", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("*")).grid(row = 3, column = 3, padx = 1, pady = 1)

#Fourth_row
four = Button(button_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(4)).grid(row = 4, column = 0, padx = 1, pady = 1)
five = Button(button_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(5)).grid(row = 4, column = 1, padx = 1, pady = 1)
six = Button(button_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(6)).grid(row = 4, column = 2, padx = 1, pady = 1)
minus = Button(button_frame, text = "-", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("-")).grid(row = 4, column = 3, padx = 1, pady = 1)

#Fifth_row
one = Button(button_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(1)).grid(row = 5, column = 0, padx = 1, pady = 1)
two = Button(button_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(2)).grid(row = 5, column = 1, padx = 1, pady = 1)
three = Button(button_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(3)).grid(row = 5, column = 2, padx = 1, pady = 1)
plus = Button(button_frame, text = "+", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("+")).grid(row = 5, column = 3, padx = 1, pady = 1)

#Sixth_row
point = Button(button_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(".")).grid(row = 6, column = 0, padx = 1, pady = 1)
zero = Button(button_frame, text = "0", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(0)).grid(row = 6, column = 1, padx = 1, pady = 1)
equals = Button(button_frame, text = "=", fg = "crimson", width = 21, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: equal_button()).grid(row = 6, column = 2, columnspan = 2, padx = 1, pady = 1)
 
cal.mainloop()                    
from tkinter import *
from tkinter import messagebox

class my_calculator:
    def __init__(self,root):
        self.root=root
        self.root.title("Calculator")
        self.root.geometry('350x420')

        self.expression=''
        self.txtinput=StringVar()

        ent_display=Entry(self.root,bd=7,bg='light blue',textvariable=self.txtinput,relief=SUNKEN,justify=RIGHT,font=('times new roman',25,'bold'))
        ent_display.grid(row=0,columnspan=4)

        btn9=Button(self.root,text='9',bd=15,font=('times new roman',15,'bold'),bg='orange',\
                    command=lambda :self.btn_click(9))
        btn9.grid(row=1,padx=10,pady=10)

        btn8 = Button(self.root, text='8', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click(8))
        btn8.grid(row=1, column=1, padx=10, pady=10)

        btn7= Button(self.root, text='7', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click(7))
        btn7.grid(row=1,column=2, padx=10, pady=10)

        btn6 = Button(self.root, text='6', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click(6))
        btn6.grid(row=2,column=0, padx=10, pady=10)

        btn5 = Button(self.root, text='5', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click(5))
        btn5.grid(row=2,column=1, padx=10, pady=10)

        btn4 = Button(self.root, text='4', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click(4))
        btn4.grid(row=2, column=2, padx=10, pady=10)

        btn3 = Button(self.root, text='3', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click(3))
        btn3.grid(row=3, column=0, padx=10, pady=10)

        btn2 = Button(self.root, text='2', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click(2))
        btn2.grid(row=3, column=1, padx=10, pady=10)

        btn1 = Button(self.root, text='1', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click(1))
        btn1.grid(row=3, column=2, padx=10, pady=10)

        btn0= Button(self.root, text='0', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                     command=lambda :self.btn_click(0))
        btn0.grid(row=4, column=0, padx=10, pady=10)

        btndive= Button(self.root, text='/', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click('/'))
        btndive.grid(row=4, column=1, padx=10, pady=10)

        btnequal = Button(self.root, text='=', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_equal())
        btnequal.grid(row=4, column=2, padx=10, pady=10)

        btnAC= Button(self.root, text='Clear', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_clr())
        btnAC.grid(row=1,column=3, padx=10, pady=10)

        btnsub = Button(self.root, text='-', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click('-'))
        btnsub.grid(row=2,column=3, padx=10, pady=10)

        btnmulti = Button(self.root, text='*', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click('*'))
        btnmulti.grid(row=3,column=3, padx=10, pady=10)

        btnADD = Button(self.root, text='+', bd=15, font=('times new roman', 15, 'bold'), bg='orange',\
                    command=lambda :self.btn_click('+'))
        btnADD.grid(row=4,column=3, padx=10, pady=10)

    def btn_click(self,number):
        self.expression=self.expression+str(number)
        self.txtinput.set(self.expression)

    def btn_equal(self):
        try:
            cal=str(eval(self.expression))
            self.txtinput.set(cal)
            self.expression=''
        except:
            messagebox.showerror("Invalid Input", "Please enter a valid arithmetic expression.")

    def btn_clr(self):
        self.txtinput.set('')
        self.expression=''


tk=Tk()
my_calculator(tk)
mainloop()

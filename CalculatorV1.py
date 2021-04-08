#!/usr/bin/env python


#Make the Window:

from tkinter import Button, Label, Entry, Tk, Grid, END
import math
root = Tk()
root.title("Calculator")

#Make the input box:

e = Entry(root, width =35, borderwidth=5, bg = 'blue', fg = 'white')
e.grid(row=0, column=0, columnspan = 3, padx =10, pady=10)

#Make the button functions:

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))
    
def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num 
    global mat
    mat = 'addition'
    f_num = float(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num 
    global mat
    mat = 'subtraction'
    f_num = float(first_number)
    e.delete(0, END)

def button_mult():
    first_number = e.get()
    global f_num 
    global mat
    mat = 'multiplication'
    f_num = float(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num 
    global mat
    mat = 'division'
    f_num = float(first_number)
    e.delete(0, END)

def button_sqr():
    first_number = e.get()
    global sqr_num
    sqr_num = int((first_number))
    e.delete(0, END)
    try:
        e.insert(0, math.sqrt(sqr_num))
    except ValueError:
        if sqr_num < 0:
            raise ZeroDivisionError + e.insert(0, "Cannot find square rool of negative number")
    
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if mat == 'addition':
        e.insert(0, f_num + float(second_number))
    
    elif mat == 'subtraction':
        e.insert(0, f_num - float(second_number))
    
    elif mat == 'multiplication':
        e.insert(0, f_num * float(second_number))
    
    elif mat == 'division':
        try:
            e.insert(0, f_num / float(second_number))
        except ZeroDivisionError:
            if f_num == 0:
                raise ZeroDivisionError + e.insert(0, "Not a number")
            else:
                raise ZeroDivisionError + e.insert(0, "Zero Division Error")
        
 
def button_decimal():
    e.insert(1, '.')



    

#Define Buttons

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), fg = 'blue')
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2), fg = 'blue')
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3), fg = 'blue')
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4), fg = 'blue')
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5), fg = 'blue')
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6), fg = 'blue')
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7), fg = 'blue')
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8), fg = 'blue')
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9), fg = 'blue')
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0), fg = 'blue')


buttonequal = Button(root, text='=', padx=40, pady=20, command=button_equal, fg = 'red')
buttonclear = Button(root, text='C', padx=40, pady=20, command=button_clear, fg = 'red')
buttondec = Button(root, text = '.', padx=40, pady=20, command=button_decimal, fg = 'red')

buttonadd = Button(root, text='+', padx=40, pady=20, command=button_add, fg = 'red')
buttonsub = Button(root, text='-', padx=40, pady=20, command=button_sub, fg = 'red')
buttonmult = Button(root, text='x', padx=40, pady=20, command=button_mult, fg = 'red')
buttondiv = Button(root, text='/', padx=40, pady=20, command=button_div, fg = 'red')
buttonsqr = Button(root, text='√', padx=40, pady=20, command=button_sqr, fg='red' )

#Put the Buttons on the screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

buttonadd.grid(row=5, column=0)
buttonsub.grid(row=6, column = 0)
buttonmult.grid(row=6, column = 1)
buttondiv.grid(row=6, column = 2)


buttonclear.grid(row=4, column = 2) 
buttondec.grid(row=4, column = 1)
buttonsqr.grid(row=5, column=1)
buttonequal.grid(row=5, column=2)


#Delete anything that may linger in the entry box:

e.delete(0, END)

#Make the loop: 

root.mainloop()



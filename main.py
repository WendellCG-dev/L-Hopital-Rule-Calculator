from sympy import symbols, diff, limit, sympify,  oo
import time
from tkinter import * 

# Function to perform L'Hopital's Rule
def Calculator():
    start_time = time.time() # start timer

    x = symbols('x')# set x as a mathematical variable
    func1 = numerator.get() # get numerator from user input
    func2 = denominator.get() # get denominator from user input
    lim_val = limit_input.get() # get limit value from user input

    try:
        # Convert user input to sympy expressions
        func1 = sympify(func1)
        func2 = sympify(func2)
        lim_val = sympify(lim_val)
    except:
        ans.set("Invalid Input") # set answer to invalid input
        return 

    try:
        # Calculate derivatives
        deriv_num = diff(func1, x)
        deriv_den = diff(func2, x)
        final_value = limit(deriv_num / deriv_den, x, lim_val)
        
    except Exception as e:
        ans.set("Error") # set answer to error
        print(f"Error: {e}") # print error
        return

    end_time = time.time()
    time_taken = end_time - start_time # calculate time taken

    ans.set(str(final_value)) # set answer to final value
    duration.set(str(round(time_taken, 5))) # set duration to time taken

# Create GUI
root = Tk()
root.config(bd=15 )
root.title("L'Hopital Calculator")

numerator= StringVar()
denominator= StringVar()
ans= StringVar()
limit_input= StringVar()
duration = StringVar()

Label(root, text="").pack()
Label(root, text="LIMIT (x -> ?)").pack()
Entry(root, justify="center", textvariable= limit_input).pack() 
Label(root, text="NUMERATOR").pack()
Entry(root, justify="center", textvariable= numerator).pack() 
Label(root, text="DENOMINATOR").pack()
Entry(root, justify="center", textvariable= denominator).pack() 
Label(root, text="ANSWER").pack()
Entry(root, justify="center", textvariable= ans, state="disabled", fg="black").pack()
Label(root, text="").pack()
Label(root, text="DURATION").pack()
Entry(root, justify="center", textvariable= duration, state="disabled", fg="black").pack()
Button(root, text="CALCULATE", command=Calculator).pack()

root.mainloop()

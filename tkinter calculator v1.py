import tkinter as tk

window = tk.Tk()
window.title('Claculator')

numbers = ['0']
action = ['null']

### FUNCTIONS ###

# OUTPUT

def output_update(text):
    value = lbl_output['text']
    if len(numbers)==1:
        if numbers[0]=='0':
            value = value[:-1]
            numbers.clear()
        elif numbers[0]=='clear':
            value = ''
            numbers.clear()
    numbers.append(text)
    lbl_output['text'] = value+str(text)

def output_clear():
    numbers.clear()
    numbers.append('0')
    action[0] = 'null'
    lbl_output['text'] = '0'
    lbl_holder['text'] = ''

def switch_prefix():
    value = lbl_output['text']
    if numbers[0] == 'clear':
        value = '0'
        numbers.clear()
        numbers.append('0')
    try:
        if value[0] == '-': value = value[1:]
        else: value = '-'+value
    except: value = '-'
    lbl_output['text'] = value

def dot():
    value = lbl_output['text']+'.'
    numbers.append('.')
    c=0
    for x in value:
        if x == '.': c+=1
    if c>1: value = value[:-1]
    else:
        try:
            null=str(value[len(value)-2])
            try: null=float(value[len(value)-2])
            except: value = value[:-1]+'0.'
        except: value = '0.'
    lbl_output['text'] = value

def backspace():
    value = lbl_output['text']
    value = value[:-1]
    if numbers[0] == 'clear':
        numbers.clear()
        numbers.append('0')
        value = '0'
    else: numbers.pop()
    if value=='' or value=='-':value+='0';numbers.append('0')
    lbl_output['text'] = value

def pi():
    numbers.clear()
    for i in "3.1415926535897932384626433832795":
        numbers.append(i)
    lbl_output['text'] = "3.1415926535897932384626433832795"


# OPERATORS

def equals():
    value = lbl_output['text']
    holder = lbl_holder['text']
    if holder[0] == '√':
        holder = holder[1:]
    holder = holder.split()
    try: number = holder[0]
    except: return
    
    if action[0] == 'add':
        try: value = float(number) + float(value)
        except: return
    if action[0] == 'sub':
        try: value = float(number) - float(value)
        except: return
    if action[0] == 'mul':
        try: value = float(number) * float(value)
        except: return
    if action[0] == 'div':
        try: value = float(number) / float(value)
        except: return
    if action[0] == 'root':
        try: value = float(number)**(1/float(value))
        except: return
    if action[0] == 'pow':
        try: value = float(number)**(float(value))
        except: return
    
    action[0] = 'null'
    holder = ''
    numbers.clear()
    numbers.append('clear')
    value = str(value)
    if value[len((value))-2]+value[len(value)-1] == '.0':
        value = value[:-2]
    lbl_output['text'] = str(value)
    lbl_holder['text'] = str(holder)

def addition():
    value = lbl_output['text']
    holder = lbl_holder['text']
    if len(holder) > 0:
        equals()
        value = lbl_output['text']
    action[0] = 'add'
    holder = f"{value} +"
    value = '0'
    numbers.clear()
    numbers.append('0')
    lbl_output['text'] = value
    lbl_holder['text'] = holder

def subtraction():
    value = lbl_output['text']
    holder = lbl_holder['text']
    if len(holder) > 0:
        equals()
        value = lbl_output['text']
    action[0] = 'sub'
    holder = f"{value} -"
    value = '0'
    numbers.clear()
    numbers.append('0')
    lbl_output['text'] = value
    lbl_holder['text'] = holder

def multiplication():
    value = lbl_output['text']
    holder = lbl_holder['text']
    if len(holder) > 0:
        equals()
        value = lbl_output['text']
    action[0] = 'mul'
    holder = f"{value} ×"
    value = '0'
    numbers.clear()
    numbers.append('0')
    lbl_output['text'] = value
    lbl_holder['text'] = holder

def division():
    value = lbl_output['text']
    holder = lbl_holder['text']
    if len(holder) > 0:
        equals()
        value = lbl_output['text']
    action[0] = 'div'
    holder = f"{value} ÷"
    value = '0'
    numbers.clear()
    numbers.append('0')
    lbl_output['text'] = value
    lbl_holder['text'] = holder

def root():
    value = lbl_output['text']
    holder = lbl_holder['text']
    if len(holder) > 0:
        equals()
        value = lbl_output['text']
    action[0] = 'root'
    holder = f"√{value}"
    value = '0'
    numbers.clear()
    numbers.append('0')
    lbl_output['text'] = value
    lbl_holder['text'] = holder

def power():
    value = lbl_output['text']
    holder = lbl_holder['text']
    if len(holder) > 0:
        equals()
        value = lbl_output['text']
    action[0] = 'pow'
    holder = f"{value} ^"
    value = '0'
    numbers.clear()
    numbers.append('0')
    lbl_output['text'] = value
    lbl_holder['text'] = holder

def factorial():
    value = lbl_output['text']
    holder = lbl_holder['text']
    if len(holder) > 0:
        equals()
        value = lbl_output['text']
    n = 1
    for i in range(int(value)):
        i+=1
        n = n*i
    n = n+(float(value)-int(value))
    value = str(n)
    holder = ''
    numbers.clear()
    numbers.append('clear')
    if value[len((value))-2]+value[len(value)-1] == '.0':
        value = value[:-2]
    lbl_output['text'] = str(value)
    lbl_holder['text'] = str(holder)


### WINDOW ###

output = tk.Frame(
    master=window
)
panel = tk.Frame(
    master=window
)

lbl_holder = tk.Label(
    master=output,
    text='',
    width=20,
    height=4,
    bg='gray'
)
lbl_holder.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

lbl_output = tk.Label(
    master=output,
    text='0',
    width=20,
    height=4,
    bg='silver'
)
lbl_output.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

panel.columnconfigure([1, 2, 3, 4], weight=1, minsize=50)
panel.rowconfigure([1, 2, 3, 4, 5, 6], weight=1, minsize=50)


### BUTTONS ###

# NUMBERS

class panel_button:
    def __init__(self, text, row, column):
        self.text = text
        self.frame = tk.Frame(
            master=panel
        )
        self.frame.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
        self.button = tk.Button(
            master=self.frame,
            text=text,
            width=20,
            height=4,
            command=self.method
        )
        self.button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
    def method(self):
        output_update(self.text)

button1 = panel_button('1', 3, 1)
button2 = panel_button('2', 3, 2)
button3 = panel_button('3', 3, 3)

button4 = panel_button('4', 4, 1)
button5 = panel_button('5', 4, 2)
button6 = panel_button('6', 4, 3)

button7 = panel_button('7', 5, 1)
button8 = panel_button('8', 5, 2)
button9 = panel_button('9', 5, 3)

button0 = panel_button('0', 6, 2)

dot_frame = tk.Frame(
    master=panel
)
dot_frame.grid(row=6, column=3, padx=5, pady=5, sticky='nsew')
dot_button = tk.Button(
    master=dot_frame,
    text='.',
    width=20,
    height=4,
    command=dot
)
dot_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)


# UTILITY

clear_frame = tk.Frame(
    master=panel
)
clear_frame.grid(row=1, column=3, padx=5, pady=5, sticky='nsew')
clear_button = tk.Button(
    master=clear_frame,
    text='Clear',
    width=20,
    height=4,
    command=output_clear
)
clear_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

backspace_frame = tk.Frame(
    master=panel
)
backspace_frame.grid(row=1, column=4, padx=5, pady=5, sticky='nsew')
backspace_button = tk.Button(
    master=backspace_frame,
    text='Back',
    width=20,
    height=4,
    command=backspace
)
backspace_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

switch_prefix_frame = tk.Frame(
    master=panel
)
switch_prefix_frame.grid(row=6, column=1, padx=5, pady=5, sticky='nsew')
switch_prefix_button = tk.Button(
    master=switch_prefix_frame,
    text='+/-',
    width=20,
    height=4,
    command=switch_prefix
)
switch_prefix_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)


# OPERATORS

equals_frame = tk.Frame(
    master=panel
)
equals_frame.grid(row=6, column=4, padx=5, pady=5, sticky='nsew')
equals_button = tk.Button(
    master=equals_frame,
    text='=',
    width=20,
    height=4,
    command=equals
)
equals_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

addition_frame = tk.Frame(
    master=panel
)
addition_frame.grid(row=5, column=4, padx=5, pady=5, sticky='nsew')
addition_button = tk.Button(
    master=addition_frame,
    text='+',
    width=20,
    height=4,
    command=addition
)
addition_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

subtraction_frame = tk.Frame(
    master=panel
)
subtraction_frame.grid(row=4, column=4, padx=5, pady=5, sticky='nsew')
subtraction_button = tk.Button(
    master=subtraction_frame,
    text='-',
    width=20,
    height=4,
    command=subtraction
)
subtraction_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

multiplication_frame = tk.Frame(
    master=panel
)
multiplication_frame.grid(row=3, column=4, padx=5, pady=5, sticky='nsew')
multiplication_button = tk.Button(
    master=multiplication_frame,
    text='×',
    width=20,
    height=4,
    command=multiplication
)
multiplication_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

division_frame = tk.Frame(
    master=panel
)
division_frame.grid(row=2, column=4, padx=5, pady=5, sticky='nsew')
division_button = tk.Button(
    master=division_frame,
    text='÷',
    width=20,
    height=4,
    command=division
)
division_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

root_frame = tk.Frame(
    master=panel
)
root_frame.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')
root_button = tk.Button(
    master=root_frame,
    text='√',
    width=20,
    height=4,
    command=root
)
root_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

power_frame = tk.Frame(
    master=panel
)
power_frame.grid(row=2, column=2, padx=5, pady=5, sticky='nsew')
power_button = tk.Button(
    master=power_frame,
    text='^',
    width=20,
    height=4,
    command=power
)
power_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

factorial_frame = tk.Frame(
    master=panel
)
factorial_frame.grid(row=2, column=3, padx=5, pady=5, sticky='nsew')
factorial_button = tk.Button(
    master=factorial_frame,
    text='!n',
    width=20,
    height=4,
    command=factorial
)
factorial_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

pi_frame = tk.Frame(
    master=panel
)
pi_frame.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
pi_button = tk.Button(
    master=pi_frame,
    text='π',
    width=20,
    height=4,
    command=pi
)
pi_button.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)


output.pack(fill=tk.BOTH, expand=True)
panel.pack(fill=tk.BOTH, expand=True)
window.mainloop()

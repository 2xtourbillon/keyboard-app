from distutils.command.config import config
import tkinter as tk

# initialize keyboard app
Keyboard_App = tk.Tk()

# 10 buttons per row
keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '='
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'DEL',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"'
        'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '!', 'TAB',
        'SPACE']

curBut = [-1, -1]
buttonL = [[]]

# text input
entry = tk.Text(Keyboard_App, width=97, height=8)
entry.grid(row=0, columnspan=15)

# var's for area where buttons will be created
varRow = 1
varColumn = 0

# left arrow key
def leftKey(event):
    if curBut == [-1, -1]: #no key has been clicks
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        curBut[:] = [0, 10]
        buttonL[0][10].configure(highlightbackground='red')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackgroun='red')
        curBut[:] = [curBut[0], (curBut[1]-1)%11]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    buttonL[curBut[0]][curBut[1]].focus_set()

# right arrow key
def rightKey(event):
    if curBut == [-1, -1]: #no key has been clicks
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        curBut[:] = [0, 0]
        buttonL[0][0].configure(highlightbackground='red')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackgroun='red')
        curBut[:] = [curBut[0], (curBut[1]+1)%11]
        buttonL[curBut[0]][curBut[1]].configure(highlighbackground='red')
    buttonL[curBut[0]][curBut[1]].focus_set()

# up arrow key
def upKey(event):
    if curBut == [-1, -1]: #no key has been clicks
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBut[0] == 0: 
        buttonL[curBut[0]][curBut[1]].configure(highlightbackgroun='red')
        curBut[:] = [(curBut[0]-1)%5, 0]
        buttonL[curBut[0]][curBut[1]].configure(highlighbackground='red')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        curBut[:] = [(curBut[0]-1)%5, 5]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        curBut[:] = [(curBut[0]-1)%5, curBut[1]]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    buttonL[curBut[0]][curBut[1]].focus_set()

# down arrow key
def downKey(event):
    if curBut == [-1, -1]: #no key has been clicks
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBut[0] == 3: 
        buttonL[curBut[0]][curBut[1]].configure(highlightbackgroun='red')
        curBut[:] = [(curBut[0]+1)%5, 0]
        buttonL[curBut[0]][curBut[1]%11].configure(highlighbackground='red')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        curBut[:] = [(curBut[0]-1)%5, 5]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        curBut[:] = [(curBut[0]+1)%5, curBut[1]]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    buttonL[curBut[0]][curBut[1]].focus_set()


def select(value, x, y):
    if curBut != [-1, -1]: # not equal to intial val
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        buttonL[curBut[0]][curBut[1]].configure(highlightcolor='red')
    curBut[:] = [x, y]
    buttonL[x][y].configure(highlightbackground='red')
    buttonL[x][y].configure(highlightcolor='red')

    if value == 'DEL':
        input_val = entry.get('1.0', 'end-2c')
        entry.delete('1.0', 'end')
        entry.insert('1.0', input_val, 'end')
    elif value == 'SPACE':
        entry.insert('insert', ' ')
    elif value == 'TAB':
        entry.insert('insert', '    ')
    else:
        entry.insert('end', value)


# creating the buttons
for button in keys:
    # adding keys in not "SPACE" barr
    if button != "SPACE":
        but = tk.Button(Keyboard_App, text=button, width=5, bg='black', fg='white', 
                     highlightthickness=4, activebackground='gray', 
                     activeforeground='red', highlightcolor='red', relief='raised',
                     padx=12, pady=4, bd=4, 
                     command=lambda x=button, i=varRow-1, j=varColumn: select(x, i, j))
        but.bind('<Return>', lambda event, x=button, i=varRow-1, j=varColumn: select(x, i, j))
        buttonL[varRow-1].append(but)
        but.grid(row=varRow, column=varColumn)
    
    # adding "SPACE" bar
    if button == 'SPACE':
        but = tk.Button(Keyboard_App, text=button, width=60, bg='black', fg='white', 
                     highlightthickness=4, activebackground='gray65', 
                     activeforeground='red', highlightcolor='red', relief='raised',
                     padx=4, pady=4, bd=4, 
                     command=lambda x=button, i=varRow-1, j=varColumn: select(x, i, j))
        but.bind('<Return>', lambda event, x=button, i=varRow-1, j=varColumn: select(x, i, j))
        buttonL[varRow-1].append(but)
        but.grid(row=6, columnspan=16)
    
    # incrementing rows and columns
    varColumn += 1
    if varColumn > 10:
        varColumn = 0
        varRow += 1
        buttonL.append([])

# Binding arrow keys
Keyboard_App.bind('<Left>', leftKey)
Keyboard_App.bind('<Right>', rightKey)
Keyboard_App.bind('<Up>', upKey)
Keyboard_App.bind('<Down>', downKey)

"""
window
cavnas
    def __init__(self):
        self.letter = None
        self.create_canvas()
        self.create_keys()
        self.cursor_position = None

    def type_letter(letter):
        cursor_position = self.letter
        cursor += 1

    def create_keyboard(self):
        for i in range(len(keys)-1):
            paste button(text=keys[i], command=type)
        
"""

Keyboard_App.mainloop()
import tkinter as tk

Keyboard_App = tk.Tk()

keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '='
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'DEL',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"'
        'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '!', 'TAB',
        'SPACE']

curBut = [-1, -1]
buttonL = [[]]

# text input
entry = tk.Text(Keyboard_App, wdith=97, height=8)
entry.grid(row=0, columnspan=15)

# var's for area where buttons will be created
varRow = 1
varColumn = 0

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
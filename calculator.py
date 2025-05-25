from tkinter import *
import customtkinter as ctk


class Main(ctk.CTk):

    # Set the position of the center_screen 
    def position_center_screen(self, width:int, height:int):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width/2)-(width/2))
        y = int((screen_height/2)-(height/2))

        return f'{width}x{height}+{x}+{y}'
    

    def __init__(self):

        super().__init__()

        # System settings
        ctk.set_appearance_mode('dark')

        # App frame
        self.title('Calculator')
        self.geometry(self.position_center_screen(300, 370))
        self.configure(bg_color='#242424')
        self.iconbitmap(bitmap='C:/Users/vladi/Desktop/apps/calculator/icon.ico')

        # Font
        self.font = ctk.CTkFont(family='Roboto', 
                                size=16, 
                                weight='normal'
        )

        # Input field
        self.entry = ctk.CTkEntry(self, 
                                  text_color='#cdcfd1', 
                                  fg_color='#242424', 
                                  border_width=2, 
                                  font=('Roboto', 30), 
                                  state=ctk.DISABLED
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky='we')

        # Data
        self.expr = ''

        # Buttons
        self.add_btn(1, 0, 'CE', command=self.clear_all, text_color='#963030')
        self.add_btn(1, 1, 'C', command=self.clear_last_character, text_color='#963030')
        self.add_btn(1, 2, '%', command=lambda: self.insert('/100'))
        self.add_btn(1, 3, '/')
        
        self.add_btn(2, 0, '7')
        self.add_btn(2, 1, '8')
        self.add_btn(2, 2, '9')
        self.add_btn(2, 3, '×', command=lambda: self.insert('*'))

        self.add_btn(3, 0, '4')
        self.add_btn(3, 1, '5')
        self.add_btn(3, 2, '6')
        self.add_btn(3, 3, '−', command=lambda: self.insert('-'))

        self.add_btn(4, 0, '1')
        self.add_btn(4, 1, '2')
        self.add_btn(4, 2, '3')
        self.add_btn(4, 3, '+')
        
        self.add_btn(5, 0, '( )', command=self.toggle_brackets)
        self.add_btn(5, 1, '0')
        self.add_btn(5, 2, '.')
        self.add_btn(5, 3, '=', command=self.result)


    # Add button
    def add_btn(self, row, column, text, command=None, columnspan=1, padx=5, pady=5, width=65, height=50, text_color='#cdcfd1'):

        if not command: command=lambda: self.insert(text)

        btn = ctk.CTkButton(self, 
                            text=text, 
                            command=command, 
                            text_color=text_color, 
                            fg_color='#202121', 
                            hover_color='#19191a',
                            border_color='#555b61',
                            border_width=2, 
                            width=width, 
                            height=height,
                            corner_radius=8, 
                            border_spacing=7, 
                            font=self.font
        )
        btn.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady)
        return btn


    # Insert button value and insert into the entry widget(CTk.Entry)
    def insert(self, text):

        self.entry.configure(state=ctk.NORMAL)  # The configuration is enabled
        self.expr += text
        self.entry.delete(0, ctk.END)  # The data has been deleted from 0 character to the END character
        self.entry.insert(0, self.expr)  # The text has been inserted into the entry
        self.entry.configure(state=ctk.DISABLED)  # The configuration is disabled


    # Clear all characters in the entry field 
    def clear_all(self):

        self.entry.configure(state=ctk.NORMAL)
        self.entry.delete(0, ctk.END)
        self.expr = ''
        self.entry.configure(state=ctk.DISABLED)


    # Clear the last character in the entry field 
    def clear_last_character(self):

        self.entry.configure(state=ctk.NORMAL)
        self.entry.delete(len(self.entry.get())-1,ctk.END)
        self.expr = self.expr[:-1]
        self.entry.configure(state=ctk.DISABLED)


    # Bracket logic
    def toggle_brackets(self):
        
        open_bracket = self.expr.count('(')
        close_bracket = self.expr.count(')')

        if open_bracket > close_bracket:
            self.insert(')')
        else:
            self.insert('(')


    # Equal
    def result(self):

        self.entry.configure(state=ctk.NORMAL)
        self.entry.delete(0, ctk.END)
        try: 
            result = str(eval(self.expr))
            self.expr = result
        except Exception as e:
            result = 'ERROR'
            self.after(1000, self.clear_all)
        self.entry.insert(0, str(result))
        self.entry.configure(state=ctk.DISABLED)
        

if __name__ == '__main__':
    main = Main()
    main.mainloop()
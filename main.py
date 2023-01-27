from tkinter import *

#global variables!
FontSize = 30
FontColor = '#000000'
BackGround = '#ffffff'
#---------------------------------->
def Save():
    def saveButton():
        SaveAs = TextExtention.get()
        Text = TextBox.get("1.0",END)
        
        with open(SaveAs,'w') as f:
            f.write(Text)
    
    NewWindow = Toplevel()
    
    TextSmall = Label(NewWindow,text="Save as:")
    TextSmall.pack()
    
    TextExtention = Entry(NewWindow,font=("mono",13))
    TextExtention.pack()

    ButtonSave = Button(NewWindow,text="save",command=saveButton,fg="#000000")
    ButtonSave.pack(pady= 10, padx= 10)
#---------------------------------->
def New():
    TextBox.delete('1.0',END)
#---------------------------------->
def Dark():
    TextBox.configure(bg=FontColor,fg=BackGround)

def Light():
    TextBox.configure(bg=BackGround,fg=FontColor)
#---------------------------------->
def Font():
    def Change():
        global FontSize
        New = int(TextExtention.get())
        TextBox.configure(font=("mono",New))

    NewWindow = Toplevel()
    
    TextSmall = Label(NewWindow,text="Font size:")
    TextSmall.pack()
    
    TextExtention = Entry(NewWindow,font=("mono",13))
    TextExtention.pack()

    ButtonSave = Button(NewWindow,text="Change",command=Change,fg="#000000")
    ButtonSave.pack(pady= 10, padx= 10)
#---------------------------------->
window = Tk()
window.geometry("550x550")
window.title("notes+++📝")

MenuBar = Menu(window)
window.config(menu=MenuBar)

FileMenu = Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label="File",menu=FileMenu)
FileMenu.add_command(label="New",command=New)
FileMenu.add_command(label="Save",command=Save)
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command=quit)

ThemesMenu = Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label="Themes",menu=ThemesMenu)
ThemesMenu.add_command(label="Dark",command=Dark)
ThemesMenu.add_command(label="Light",command=Light)
ThemesMenu.add_separator()
ThemesMenu.add_command(label="Font",command=Font)

TextBox = Text(window,font=("mono",FontSize),bg=BackGround,fg=FontColor)
TextBox.pack(fill=BOTH, expand=1)

window.mainloop()
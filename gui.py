import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class App(tk.Frame):
  def __init__(self, master):
    super().__init__(master)
    self.pack()

    self.select_image_button = ttk.Button(self, text='Select an image', command=self.select_image)
    self.select_image_button.pack()

  def select_image(self):
    filetypes = (
      ('All', '.*'),
      ('JPEG', '.jpg .jpeg'),
      ('PNG', '.png'))
    filename = filedialog.askopenfilename(
      title='Select an image',
      initialdir='~/',
      filetypes=filetypes)

    img = Image.open(filename)
    self.img = ImageTk.PhotoImage(img)
    label = ttk.Label(self, image=self.img)
    label.pack()

WIDTH = 1024
HEIGHT = 512

root = tk.Tk()
root.title('Dog breed analyzer')
root.resizable(False, False)

swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()

x_offset = int((swidth / 2) - (WIDTH / 2))
y_offset = int((sheight / 2) - (HEIGHT / 2))

root.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x_offset, y_offset))
app = App(root)
app.mainloop()


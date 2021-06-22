import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np

SAVED_MODEL_PATH = './saved_model'

class App(tk.Frame):
  def __init__(self, master):
    super().__init__(master)
    self.pack()

    self.select_image_button = ttk.Button(self, text='Select an image', command=self.select_image)
    self.predict_button= ttk.Button(self, text='Predict', command=self.predict)
    self.select_image_button.pack()
    self.predict_button.pack()
    self.model = keras.models.load_model(SAVED_MODEL_PATH)

  def select_image(self):
    filetypes = (
      ('All', '.*'),
      ('JPEG', '.jpg .jpeg'),
      ('PNG', '.png'))
    self.filename = filedialog.askopenfilename(
      title='Select an image',
      initialdir='./',
      filetypes=filetypes)

    img = Image.open(self.filename)
    self.img = ImageTk.PhotoImage(img)
    label = ttk.Label(self, image=self.img)
    label.pack()

  def predict(self):
    if self.filename:
      img = image.load_img(self.filename, target_size=(128, 128))
      img = image.img_to_array(img)
      img = np.expand_dims(img, axis=0)
      result = self.model.predict_classes(img)
      print(result)
    else:
      print('none selected')

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


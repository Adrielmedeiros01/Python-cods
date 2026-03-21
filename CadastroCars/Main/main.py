import tkinter as tk
from model import CarroModel
from view import CarroView
from controller import CarroController

root = tk.Tk()

model = CarroModel()
view = CarroView(root)
controller = CarroController(model, view)

root.mainloop()

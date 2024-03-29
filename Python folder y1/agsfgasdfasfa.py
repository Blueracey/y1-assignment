import tkinter as Tkinter
import random

class App:
    def __init__(self, t):
        self.width = 320
        self.height = 200
        self.i = Tkinter.PhotoImage(width=self.width,height=self.height)
        rgb_colors = ([random.randint(0,255) for i in range(0,3)] for j in range(0,self.width*self.height))
        pixels=" ".join(("{"+" ".join(('#%02x%02x%02x' %
            tuple(next(rgb_colors)) for i in range(self.width)))+"}" for j in range(self.height)))
        self.i.put(pixels,(0,0,self.width-1,self.height-1))
        c = Tkinter.Canvas(t, width=self.width, height=self.height); c.pack()
        c.create_image(0, 0, image = self.i, anchor=Tkinter.NW)

t = Tkinter.Tk()
a = App(t)    
t.mainloop()
import tkinter as tk
from PIL import ImageTk, Image
    
master = tk.Tk()
master.title("Space Game")
master.geometry("2560x1600")

canvas = tk.Canvas(master, bg="black", width=2560, height=1600)
canvas.pack()

# Load and display background image
background_image = tk.PhotoImage(file="bg.png")
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Load and display rocket image
rocket_image =  ImageTk.PhotoImage(Image.open("rocket.png").resize((120, 200)))
rocket = canvas.create_image(300, 350, anchor=tk.CENTER, image=rocket_image)


# Load and display rocket image
carrot_image =  ImageTk.PhotoImage(Image.open("carrot.png").resize((40, 50)))
carrot = canvas.create_image(300, 350, anchor=tk.CENTER, image=carrot_image)

def move_carrot_to(x, y):
    canvas.move(carrot, x, y)  # Move the rocket to the new position


def move_rocket(event):
    key = event.keysym
    if key == "Up":
        canvas.move(rocket, 0, -10)
    elif key == "Down":
        canvas.move(rocket, 0, 10)
    elif key == "Left":
        canvas.move(rocket, -10, 0)
    elif key == "Right":
        canvas.move(rocket, 10, 0)
        
    if key == "space":    
            
        move_carrot_to(0,-25)

master.bind("<KeyPress>", move_rocket)


master.mainloop()

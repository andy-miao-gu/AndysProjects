import tkinter as tk
import random

GRID_SIZE = 5
CELL_SIZE = 100

# Function to place a plant in the grid
def place_plant(row, col):
    plant = selected_plant.get()
    cost = selected_cost.get()

    if grid[row][col] == 0 and plant:
        if cost <= sun_count.get():
            grid[row][col] = plant
            update_sun_count(-cost)

            if plant == "Walnut":
                canvas.create_rectangle(
                    col * CELL_SIZE,
                    row * CELL_SIZE,
                    (col + 1) * CELL_SIZE,
                    (row + 1) * CELL_SIZE,
                    fill='#8B4513',
                    outline='black'
                )
            elif plant == "Peashooter":
                canvas.create_rectangle(
                    col * CELL_SIZE + 20,
                    row * CELL_SIZE + 20,
                    (col + 1) * CELL_SIZE - 20,
                    (row + 1) * CELL_SIZE - 20,
                    fill='green',
                    outline='black'
                )
                canvas.create_oval(
                    col * CELL_SIZE + 40,
                    row * CELL_SIZE + 40,
                    (col + 1) * CELL_SIZE - 40,
                    (row + 1) * CELL_SIZE - 40,
                    fill='#32CD32',
                    outline='black'
                )
            elif plant == "Sunflower":
                canvas.create_rectangle(
                    col * CELL_SIZE + 20,
                    row * CELL_SIZE + 20,
                    (col + 1) * CELL_SIZE - 20,
                    (row + 1) * CELL_SIZE - 20,
                    fill='green',
                    outline='black'
                )
                canvas.create_oval(
                    col * CELL_SIZE + 40,
                    row * CELL_SIZE + 40,
                    (col + 1) * CELL_SIZE - 40,
                    (row + 1) * CELL_SIZE - 40,
                    fill='orange',
                    outline='black'
                )

                # Schedule initial sun production for sunflower(s) after a random time between 3.5 and 5 seconds
                sunflower_count = sum(1 for row in grid for item in row if item == "Sunflower")
                delay = random.uniform(3.5, 5)
                root.after(int(delay * 1000), lambda count=sunflower_count: produce_suns(count))

            selected_plant.set("")
            selected_cost.set(0)
        else:
            print("Not enough suns!")

# Function to update sun count
def update_sun_count(value):
    current_sun = sun_count.get()
    sun_count.set(current_sun + value)

# Function to produce suns periodically for sunflowers
def produce_suns(sunflower_count):
    update_sun_count(sunflower_count * 25)
    delay = random.uniform(3.5, 5)
    root.after(int(delay * 1000), lambda count=sunflower_count: produce_suns(count))

# Function to handle plant selection
def select_plant(plant, cost):
    selected_plant.set(plant)
    selected_cost.set(cost)

# Initialize the Tkinter app and create a canvas
root = tk.Tk()
root.title("Plants vs. Zombies")

canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="lightgray")
canvas.pack(side=tk.RIGHT)

left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10)

selected_plant = tk.StringVar()
selected_cost = tk.IntVar()

sun_count = tk.IntVar()
sun_count.set(50)  # Initial sun count

# Buttons for selecting plants
plant_buttons = [
    ("Walnut", 75),
    ("Peashooter", 100),
    ("Sunflower", 50)
]

for plant, cost in plant_buttons:
    button = tk.Button(left_frame, text=f"{plant} - {cost} suns", command=lambda p=plant, c=cost: select_plant(p, c))
    button.pack(pady=5)

sun_label = tk.Label(left_frame, text="Suns: ")
sun_label.pack()

sun_count_label = tk.Label(left_frame, textvariable=sun_count)
sun_count_label.pack()

grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Bind click event to place plant
def on_click(event):
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE
    place_plant(row, col)

canvas.bind("<Button-1>", on_click)

root.mainloop()

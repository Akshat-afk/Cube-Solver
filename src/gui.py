import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import control
import cube_status
import kociemba


class RubiksCubeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rubik's Cube Solver")

        self.cube = cube_status.CubeStatus()
        self.controler = control.RubicControler()
        self.controler.prepare()
        self.current_status = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
        self.side_to_color = {'U': 'W', 'R': 'B', 'F': 'R', 'D': 'Y', 'L': 'G', 'B': 'O'}

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Rubik's Cube Solver", font=('Helvetica', 20, 'bold'), foreground='#1E3D58')
        self.label.pack(pady=10)

        # Frame for the cube display
        self.cube_frame = ttk.Frame(self.root)
        self.cube_frame.pack()

        self.canvas = tk.Canvas(self.cube_frame, width=500, height=500, background='#F9EBB2')  # Adjusted canvas size and background color
        self.canvas.grid(row=0, column=0, padx=10)

        # Frame for buttons and entry widgets
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=10)

        ttk.Label(self.button_frame, text="Number of Random Moves:", font=('Helvetica', 14), foreground='#1E3D58').grid(row=0, column=0, padx=5)

        # Entry widget for the number of random moves
        self.random_moves_entry = ttk.Entry(self.button_frame, width=5, font=('Helvetica', 14))
        self.random_moves_entry.grid(row=0, column=1, padx=5)
        self.random_moves_entry.insert(0, "5")  # Default value

        ttk.Button(self.button_frame, text="Scramble", command=self.scramble, style='C.TButton').grid(row=0, column=2, padx=10)
        ttk.Button(self.button_frame, text="Solve", command=self.solve, style='C.TButton').grid(row=0, column=3, padx=10)

        ttk.Label(self.button_frame, text="Enter Custom Moves:", font=('Helvetica', 14), foreground='#1E3D58').grid(row=1, column=0, padx=5)

        self.custom_moves_entry = ttk.Entry(self.button_frame, font=('Helvetica', 14))
        self.custom_moves_entry.grid(row=1, column=1, padx=5)

        ttk.Button(self.button_frame, text="Perform Custom Moves", command=self.perform_custom_moves, style='C.TButton').grid(row=1, column=2, padx=10)

    def update_cube_display(self):
        img = self.cube.display_status(list(self.current_status), self.side_to_color)
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        self.img_reference = ImageTk.PhotoImage(image=img)
        self.canvas.config(width=img.width, height=img.height)
        self.canvas.img = self.img_reference
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_reference)

    def scramble(self):
        num_moves = int(self.random_moves_entry.get())
        moves = self.controler.random_move(num_moves)
        print(moves)
        self.current_status = self.cube.change_status(self.current_status, moves)
        self.update_cube_display()

    def solve(self):
        moves = kociemba.solve(self.current_status).split()
        print(moves)
        for move in moves:
            self.controler.turn(move)
        self.current_status = self.cube.change_status(self.current_status, moves)
        self.update_cube_display()

    def perform_custom_moves(self):
        command = self.custom_moves_entry.get()
        moves = command.split()
        for move in moves:
            self.controler.turn(move)
        self.current_status = self.cube.change_status(self.current_status, moves)
        self.update_cube_display()


def main():
    root = tk.Tk()

    # Adding a custom style for buttons
    style = ttk.Style()
    style.configure('C.TButton', foreground='#1E3D58', background='#F9EBB2', font=('Helvetica', 14))

    app = RubiksCubeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class RubiksCubeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rubik's Cube Solver")

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Rubik's Cube Solver", font=(
            'Helvetica', 20, 'bold'), foreground='#1E3D58')
        self.label.pack(pady=10)

        self.canvas_frame = ttk.Frame(self.root)
        self.canvas_frame.pack()

        self.canvas = FigureCanvasTkAgg(
            self.create_3d_cube(), master=self.canvas_frame)
        self.canvas.get_tk_widget().pack()

    def create_3d_cube(self):
        fig = plt.Figure(figsize=(6, 6))
        ax = fig.add_subplot(111, projection='3d')

        # Define cube vertices 
        vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                             [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

        # Define cube faces
        faces = [[vertices[j] for j in [0, 1, 2, 3]],
                 [vertices[j] for j in [4, 5, 6, 7]],
                 [vertices[j] for j in [0, 3, 7, 4]],
                 [vertices[j] for j in [1, 2, 6, 5]],
                 [vertices[j] for j in [0, 1, 5, 4]],
                 [vertices[j] for j in [2, 3, 7, 6]]]

        for face in faces:
            ax.add_collection3d(plt.Poly3DCollection(
                [face], facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.8))

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        return fig


def main():
    root = tk.Tk()

    app = RubiksCubeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

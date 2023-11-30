    SIDE_AREA_SIZE = 50
    SIDE_AREA_GAP = 5
    SIDE_AREA_POSITION = {'U': (1, 0), 'R': (2, 1), 'F': (1, 1), 'D': (1, 2), 'L': (0, 1), 'B': (3, 1)}
    side_order = ['U', 'R', 'F', 'D', 'L', 'B']

    def display_status(self, status_list, side_to_color):
        img_width = self.SIDE_AREA_SIZE * 4 + self.SIDE_AREA_GAP * 5
        img_height = self.SIDE_AREA_SIZE * 3 + self.SIDE_AREA_GAP * 4
        img = np.zeros((img_height, img_width, 3), np.uint8)

        for idx, side in enumerate(self.side_order):
            (x, y) = self.SIDE_AREA_POSITION[side]
            offset = (x * self.SIDE_AREA_SIZE + (x + 1) * self.SIDE_AREA_GAP,
                      y * self.SIDE_AREA_SIZE + (y + 1) * self.SIDE_AREA_GAP)
            stickers = status_list[idx * 9: (idx + 1) * 9]
            self.draw_stickers(img, stickers, offset, side_to_color)
        return img

    def draw_stickers(self, img, stickers, offset, side_to_color):
        # Function to draw stickers on the image
        # ...
        pass

    def display_status_3d(self, current_status):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                             [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

        faces = [[vertices[j] for j in [0, 1, 2, 3]],
                 [vertices[j] for j in [4, 5, 6, 7]],
                 [vertices[j] for j in [0, 3, 7, 4]],
                 [vertices[j] for j in [1, 2, 6, 5]],
                 [vertices[j] for j in [0, 1, 5, 4]],
                 [vertices[j] for j in [2, 3, 7, 6]]]

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        for idx, side in enumerate(self.side_order):
            color = self.get_color(current_status, side)
            for face in faces:
                ax.add_collection3d(Poly3DCollection([face], facecolors=color, linewidths=1, edgecolors='r', alpha=0.8))

        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        ax.set_zlim([0, 1])

        plt.show()

    def get_color(self, current_status, side):
        color_map = {'U': 'O', 'R': 'B', 'F': 'W', 'D': 'R', 'L': 'G', 'B': 'Y'}
        color = color_map[side]
        index = self.side_order.index(side) * 9
        return [self.color_name_to_rgba(c) for c in current_status[index:index + 9]]

    def color_name_to_rgba(self, color_name):
        color_dict = {'O': (1.0, 0.5, 0.0, 1.0),  # Orange
                      'B': (0.0, 0.0, 1.0, 1.0),  # Blue
                      'W': (1.0, 1.0, 1.0, 1.0),  # White
                      'R': (1.0, 0.0, 0.0, 1.0),  # Red
                      'G': (0.0, 1.0, 0.0, 1.0),  # Green
                      'Y': (1.0, 1.0, 0.0, 1.0)}  # Yellow

        return color_dict.get(color_name, (1.0, 1.0, 1.0, 1.0))  # Default to white if color not found

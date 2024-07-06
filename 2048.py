import tkinter as tk
import random

class Game2048:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048 Game")
        self.window.geometry("400x400")
        self.frame = tk.Frame(self.window, bg="azure3")
        self.frame.pack(fill="both", expand=True)
        self.grid = [[0]*4 for _ in range(4)]
        self.score = 0
        self.create_widgets()
        self.window.bind("<Key>", self.key_press)

    def create_widgets(self):
        # Create a 4x4 grid of buttons
        self.buttons = []
        for i in range(4):
            row = []
            for j in range(4):
                button = tk.Button(self.frame, text="", width=5, height=2, font=("Arial", 20))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
        self.new_game()

    def new_game(self):
        # Reset the game state
        self.score = 0
        for i in range(4):
            for j in range(4):
                self.grid[i][j] = 0
                self.buttons[i][j]['text'] = ""
        self.add_tile()
        self.add_tile()

    def add_tile(self):
        # Add a new tile to the grid
        empty_tiles = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.grid[i][j] = 2
            self.buttons[i][j]['text'] = "2"

    def key_press(self, event):
        # Handle arrow key presses
        if event.keysym == "Up":
            self.move_up()
        elif event.keysym == "Down":
            self.move_down()
        elif event.keysym == "Left":
            self.move_left()
        elif event.keysym == "Right":
            self.move_right()

    def move_up(self):
        # Move tiles up
        for j in range(4):
            temp = []
            for i in range(4):
                if self.grid[i][j] != 0:
                    temp.append(self.grid[i][j])
            temp += [0] * (4 - len(temp))
            for i in range(3):
                if temp[i] == temp[i+1]:
                    temp[i] *= 2
                    self.score += temp[i]
                    temp[i+1] = 0
            temp = [x for x in temp if x != 0]
            temp += [0] * (4 - len(temp))
            for i in range(4):
                self.grid[i][j] = temp[i]
                self.buttons[i][j]['text'] = str(self.grid[i][j]) if self.grid[i][j] != 0 else ""
        self.add_tile()

    def move_down(self):
        # Move tiles down
        for j in range(4):
            temp = []
            for i in range(3, -1, -1):
                if self.grid[i][j] != 0:
                    temp.append(self.grid[i][j])
            temp += [0] * (4 - len(temp))
            for i in range(3):
                if temp[i] == temp[i+1]:
                    temp[i] *= 2
                    self.score += temp[i]
                    temp[i+1] = 0
            temp = [x for x in temp if x != 0]
            temp += [0] * (4 - len(temp))
            for i in range(4):
                self.grid[3-i][j] = temp[i]
                self.buttons[3-i][j]['text'] = str(self.grid[3-i][j]) if self.grid[3-i][j] != 0 else ""
        self.add_tile()

    def move_left(self):
        # Move tiles left
        for i in range(4):
            temp = []
            for j in range(4):
                if self.grid[i][j] != 0:
                    temp.append(self.grid[i][j])
            temp += [0] * (4 - len(temp))
            for j in range(3):
                if temp[j] == temp[j+1]:
                    temp[j] *= 2
                    self.score += temp[j]
                    temp[j+1] = 0
            temp = [x for x in temp if x != 0]
            temp += [0] * (4 - len(temp))
            for j in range(4):
                self.grid[i][j] = temp[j]
                self.buttons[i][j]['text'] = str(self.grid[i][j]) if self.grid[i][j] != 0 else ""
        self.add_tile()

    def move_right(self):
        # Move tiles right
        for i in range(4):
            temp = []
            for j in range(3, -1, -1):
                if self.grid[i][j]!= 0:
                    temp.append(self.grid[i][j])
            temp += [0] * (4 - len(temp))
            for j in range(3):
                if temp[j] == temp[j+1]:
                    temp[j] *= 2
                    self.score += temp[j]
                    temp[j+1] = 0
            temp = [x for x in temp if x!= 0]
            temp += [0] * (4 - len(temp))
            for j in range(4):
                self.grid[i][3-j] = temp[j]
                self.buttons[i][3-j]['text'] = str(self.grid[i][3-j]) if self.grid[i][3-j]!= 0 else ""
        self.add_tile()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = Game2048()
    game.run()
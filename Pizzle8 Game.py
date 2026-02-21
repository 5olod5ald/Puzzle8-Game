import tkinter as tk
import random
import heapq

class PuzzleLogic:
    def __init__(self):
        self.goal_state = [
            [1,2,3],
            [4,5,6],
            [7,8,0]
        ]
        self.reset()

    def reset(self):
        self.current_state = [row.copy() for row in self.goal_state]
        self.zero_pos = (2,2)

    def move_up(self):
        r,c = self.zero_pos
        if r > 0:
            self.current_state[r][c], self.current_state[r-1][c] = self.current_state[r-1][c], self.current_state[r][c]
            self.zero_pos = (r-1,c)

    def move_down(self):
        r,c = self.zero_pos
        if r < 2:
            self.current_state[r][c], self.current_state[r+1][c] = self.current_state[r+1][c], self.current_state[r][c]
            self.zero_pos = (r+1,c)

    def move_left(self):
        r,c = self.zero_pos
        if c > 0:
            self.current_state[r][c], self.current_state[r][c-1] = self.current_state[r][c-1], self.current_state[r][c]
            self.zero_pos = (r,c-1)

    def move_right(self):
        r,c = self.zero_pos
        if c < 2:
            self.current_state[r][c], self.current_state[r][c+1] = self.current_state[r][c+1], self.current_state[r][c]
            self.zero_pos = (r,c+1)

    def is_solved(self):
        return self.current_state == self.goal_state

    def shuffle(self, moves=100):
        self.reset()
        for _ in range(moves):
            random.choice([self.move_up,self.move_down,self.move_left,self.move_right])()

goal_state = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

def find_position(matrix,value):
    for r in range(3):
        for c in range(3):
            if matrix[r][c] == value:
                return r,c

def Htable(state):
    distance = 0
    for r in range(3):
        for c in range(3):
            if state[r][c] != 0:
                gr,gc = find_position(goal_state,state[r][c])
                distance += abs(r-gr)+abs(c-gc)
    return distance

class Node:
    def __init__(self,state,parent=None,g=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = Htable(state)
        self.f = self.g + self.h

    def __lt__(self,other):
        return self.f < other.f

def get_possible_moves(state):
    moves=[]
    r,c = find_position(state,0)

    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr,nc = r+dr, c+dc
        if 0<=nr<3 and 0<=nc<3:
            new_state=[list(row) for row in state]
            new_state[r][c],new_state[nr][nc]=new_state[nr][nc],new_state[r][c]
            moves.append(new_state)
    return moves

def solve_puzzle(start):

    open_list=[]
    start_node=Node(start)
    heapq.heappush(open_list,start_node)
    closed=set()

    while open_list:
        node=heapq.heappop(open_list)

        if node.state==goal_state:
            path=[]
            while node:
                path.append(node.state)
                node=node.parent
            return path[::-1]

        closed.add(tuple(map(tuple,node.state)))

        for move in get_possible_moves(node.state):

            if tuple(map(tuple,move)) in closed:
                continue

            new_node=Node(move,node,node.g+1)
            heapq.heappush(open_list,new_node)

    return None


def start_game():
    welcome_window.destroy()
    main_game()


def main_game():

    root = tk.Tk()
    root.title("8 Puzzle Game")
    root.geometry("420x520")
    root.configure(bg="#1e1e2f")

    logic = PuzzleLogic()

    title = tk.Label(root,
                     text="8 Puzzle Game",
                     font=("Segoe UI",24,"bold"),
                     bg="#1e1e2f",
                     fg="white")
    title.pack(pady=15)

    board_frame = tk.Frame(root,bg="#1e1e2f")
    board_frame.pack()

    buttons=[[None]*3 for _ in range(3)]

    def update_gui():
        for i in range(3):
            for j in range(3):
                value = logic.current_state[i][j]
                text = str(value) if value!=0 else ""
                buttons[i][j].config(text=text)

    def move_tile(x,y):

        r,c = logic.zero_pos

        if (abs(x-r)==1 and y==c) or (abs(y-c)==1 and x==r):

            logic.current_state[r][c],logic.current_state[x][y] = logic.current_state[x][y],logic.current_state[r][c]

            logic.zero_pos = (x,y)

            update_gui()

            if logic.is_solved():

                win=tk.Toplevel(root)
                win.title("Winner")
                win.geometry("250x120")

                tk.Label(win,
                         text="🎉 You solved it!",
                         font=("Segoe UI",16)).pack(pady=25)

    for i in range(3):
        for j in range(3):

            btn=tk.Button(board_frame,
                          width=4,
                          height=2,
                          font=("Segoe UI",28,"bold"),
                          bg="#4a6fa5",
                          fg="white",
                          bd=0,
                          relief="flat",
                          command=lambda x=i,y=j: move_tile(x,y))

            btn.grid(row=i,column=j,padx=6,pady=6)

            buttons[i][j]=btn


    control_frame=tk.Frame(root,bg="#1e1e2f")
    control_frame.pack(pady=20)

    def shuffle_board():
        logic.shuffle()
        update_gui()

    def reset_board():
        logic.reset()
        update_gui()

    def solve():

        solution=solve_puzzle(logic.current_state)

        if solution:

            def apply_solution(i=0):

                if i<len(solution):

                    logic.current_state=[list(row) for row in solution[i]]

                    logic.zero_pos=find_position(logic.current_state,0)

                    update_gui()

                    root.after(400,lambda:apply_solution(i+1))

            apply_solution()


    tk.Button(control_frame,
              text="Shuffle",
              width=10,
              font=("Segoe UI",12,"bold"),
              bg="#f7b32b",
              command=shuffle_board).grid(row=0,column=0,padx=10)

    tk.Button(control_frame,
              text="Reset",
              width=10,
              font=("Segoe UI",12,"bold"),
              bg="#6bcf63",
              command=reset_board).grid(row=0,column=1,padx=10)

    tk.Button(control_frame,
              text="Solve",
              width=10,
              font=("Segoe UI",12,"bold"),
              bg="#ff6b6b",
              fg="white",
              command=solve).grid(row=0,column=2,padx=10)

    update_gui()

    root.mainloop()



welcome_window = tk.Tk()

welcome_window.title("8 Puzzle Game")
welcome_window.geometry("400x300")
welcome_window.configure(bg="#1e1e2f")

title=tk.Label(welcome_window,
               text="8 Puzzle Game",
               font=("Segoe UI",28,"bold"),
               bg="#1e1e2f",
               fg="white")

title.pack(pady=60)

start_btn=tk.Button(welcome_window,
                    text="Start Game",
                    font=("Segoe UI",16,"bold"),
                    bg="#4a6fa5",
                    fg="white",
                    width=15,
                    command=start_game)

start_btn.pack()

welcome_window.mainloop()
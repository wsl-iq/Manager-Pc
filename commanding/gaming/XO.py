from tkinter import *
def play_XO():

    def function(r,c):
        global player
        if player == 'X':
            b[r][c].configure(text = 'X')
            player = 'O'
        else:
            b[r][c].configure(text = 'O')
            player = 'X'
    root = Tk()
    root.title('Game Play X O')
    b = [[0,5,0],[0,5,0],[0,5,0]]
    for i in range(3):
        for j in range(3):
            b[i][j] = Button(font=('Verdana', 50),width=3, bg='green',command=lambda r=i,c=j: function(r,c))
            b[i][j].grid(row = i, column = j)
    player = 'X'
    mainloop()
if __name__ == '__main__':
    play_XO()
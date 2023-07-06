import random
import tkinter

from PIL import ImageTk
from PIL.ImageTk import PhotoImage

stats = []


def get_winner(call):
    if random.random() <= (1 / 3):
        throw = "rock"
    elif (1 / 3) < random.random() <= (2 / 3):
        throw = "scissors"
    else:
        throw = "paper"

    if (throw == "rock" and call == "paper") or (throw == "paper" and call == "scissors") \
            or (throw == "scissors" and call == "rock"):
        stats.append('W')
        result = "You won!"
    elif throw == call:
        stats.append('D')
        result = "It's a draw"
    else:
        stats.append('L')
        result = "You lost!"

    global output
    output.config(text="Computer did: " + throw + "\n" + result)


def pass_s():
    get_winner("scissors")


def pass_r():
    get_winner("rock")


def pass_p():
    get_winner("paper")


window = tkinter.Tk()
window.geometry('1000x1000')

bg = PhotoImage(file="2.jpg")
new_label = tkinter.Label(window, text='Rock Paper Scissors Game', fg='white', bg='black', bd=6, relief=tkinter.RAISED,
                          font=('ariel', 30))
new_label.place(x=570, y=20)
scissors = tkinter.Button(window, text="Scissors", bg="#84ff54", command=pass_s, width=20)
scissors.place(x=570, y=25)
rock = tkinter.Button(window, text="Rock", bg="#595858", padx=10, pady=5, command=pass_r, width=20)
paper = tkinter.Button(window, text="Paper", bg="#f9fff7", padx=10, pady=5, command=pass_p, width=20)
output = tkinter.Label(window, width=20, fg="red", text="What's your call?")

scissors.pack()
rock.pack()
paper.pack()
output.pack()
window.mainloop()

for i in stats: print(i, end=" ")
if stats.count('L') > stats.count('W'):
    result = "\n OOPS! You loose the Game."
elif stats.count('L') == stats.count('W'):
    result = "\nSeries ended in a draw."
else:
    result = "\n Congratulations!  You win the Game."

print(result)

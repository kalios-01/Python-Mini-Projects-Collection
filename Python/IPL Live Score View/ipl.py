from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("Indian Premier League")

url = "https://www.cricbuzz.com/"
root.configure(background='black')
root.wm_minsize(700,300)
root.wm_maxsize(700,300)
#root.resizable(height=None, width=None)


def get_score():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    team_1 = soup.findAll(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
    team_2 = soup.findAll(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
    team_1_score = soup.findAll(class_="cb-ovr-flo")[8].get_text()
    team_2_score = soup.findAll(class_="cb-ovr-flo")[12].get_text()

    teams.config(text=f"{team_1}\t\t{team_2}")
    scores.config(text=f"{team_1_score}\t\t{team_2_score}")
    scores.after(10, get_score)


title = Label(root, text='IPL 2021', foreground="red", background="black", font=("Haveltica 20 bold"))
title.grid(row=0, pady=5)

teams = Label(root, foreground="red", background="black", font=("Haveltica 20 bold"))
teams.grid(row=1, pady=5)

scores = Label(root, foreground="red", background="black", font=("Haveltica 20 bold"))
scores.grid(row=2, pady=5)
get_score()
root.mainloop()

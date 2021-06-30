# window.py

from guizero import App, Text, Box, Picture, PushButton
from user import ask_name


app = App("Matching The Emojis", height=380, width=1000)
result = Text(app)

# get player names
player1 = ask_name('Player 1')
player2 = ask_name('Player 2')

# create a box to house the grids
game_box = Box(app, border=2, layout='grid')
# create a box to house the pictures
pictures_box = Box(game_box, layout="grid", width='fill', height='fill', grid=[1, 0], border=2)
buttons_box = Box(game_box, layout="grid", width='fill', height='fill', grid=[2, 0], border=2)

# Box for player 1
left_box = Box(game_box, grid=[0, 0], height='fill', layout='grid', border=2)
name_txt = Text(left_box, 'Name:', grid=[0, 0])
username_txt = Text(left_box, player1, grid=[1, 0])

score_txt = Text(left_box, text='Score:', grid=[0, 1])
left_scoreno_txt = Text(left_box, text=0, grid=[1, 1])

rounds_txt = Text(left_box, text='Rounds:', grid=[0, 2])
left_roundno_txt = Text(left_box, text=0, grid=[1, 2])

timer_txt = Text(left_box, text='Timer:', grid=[0, 3])
left_timerno_txt = Text(left_box, text='15', grid=[1, 3])

# Box for player 2
right_box = Box(game_box, grid=[4, 0], layout='grid', height='fill', border=2)
name_txt = Text(right_box, 'Name:', grid=[0, 0])
username_txt = Text(right_box, player2, grid=[1, 0])

score_txt = Text(right_box, text='Score:', grid=[0, 1])
right_scoreno_txt = Text(right_box, text=0, grid=[1, 1])

rounds_txt = Text(right_box, text='Rounds:', grid=[0, 2])
right_roundno_txt = Text(right_box, text=0, grid=[1, 2])

timer_txt = Text(right_box, text='Timer:', grid=[0, 3])
right_timerno_txt = Text(right_box, text='15', grid=[1, 3])


# create an empty lists to add the buttons and pictures to
buttons = []
pictures = []
# create 9 PushButtons with a different grid coordinate and add to the list
for x in range(0, 4):
    for y in range(0, 4):
        # put the pictures and buttons into the lists
        picture = Picture(pictures_box, grid=[x, y])
        pictures.append(picture)

        button = PushButton(buttons_box, grid=[x, y])
        buttons.append(button)

import window
import random
import os

emojis_dir = "emojis"
emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]

current_player = 1
score = window.left_scoreno_txt
rounds = window.left_roundno_txt
timer = window.left_timerno_txt


def match_emoji(matched):
    """command used in each button, it is ran when the button is clicked in

    Args:
        matched (bool): does it trigger right or wrong answer
    """
    global score
    global rounds

    if matched:
        window.result.value = "correct"
        score.value = int(score.value) + 1
    else:
        window.result.value = "incorrect"
        score.value = int(score.value) - 1

    rounds.value = int(rounds.value) + 1

    switch_player()

    insert_emojis(window.pictures)
    insert_emojis(window.buttons)


def get_rand_elems(lst, number):
    rand_indexes = random.sample(range(len(lst)), number)
    rand_elems = [lst[index] for index in rand_indexes]
    return rand_elems


def insert_emojis(widgets, is_alike=False):
    if not is_alike:
        emojis_set = get_rand_elems(emojis, len(widgets))
        for widget in widgets:
            widget.image = emojis_set.pop()
    if is_alike:
        alike_emoji = get_rand_elems(emojis, 1)[0]  # used [0] to get obj out of list
        for widget in widgets:
            widget.image = alike_emoji


def update_command(button_lst, func, arg):
    for button in button_lst:
        try:
            button.update_command(func, arg)
        except AttributeError:
            pass


def countdown():
    if int(timer.value) != 0:
        timer.value = int(timer.value) - 1
    elif int(timer.value) <= 0:
        # window.result.value = 'GAMEOVER'
        window.app.cancel(countdown)
        # window.app.warn('Warning', 'Time is up')
        #  score.value = 0
        #  rounds_txt.value = 0
        window.result.value = ''
        # timer.value = '15'
        pre_round()  # recursion
    else:
        pass


def switch_player():
    global current_player
    global score
    global rounds
    global timer

    if current_player is None or current_player == 2:
        current_player = 1
        score = window.left_scoreno_txt
        rounds = window.left_roundno_txt
        timer = window.left_timerno_txt

    elif current_player == 1:
        current_player = 2
        score = window.right_scoreno_txt
        rounds = window.right_roundno_txt
        timer = window.right_timerno_txt


def show_scores():
    scores = "The Game Has Ended\np"
    window.app.info(scores, 'test')


def pre_round():
    if int(timer.value) > 0:
        insert_emojis(window.pictures)
        insert_emojis(window.buttons)
        update_command(window.buttons, match_emoji, [False])

        # insert the alike emojis
        alike_set = [get_rand_elems(window.pictures, 1)[0], get_rand_elems(window.buttons, 1)[0]]  # used [0] to remove nested list
        insert_emojis(alike_set, True)
        update_command(alike_set, match_emoji, [True])
        window.app.repeat(1000, countdown)

    # fix: enters this condition by recurssion untl maximum recursion is reached
    elif int(timer.value) == 0:
        print('f')
        switch_player()
        pre_round()

    # fix: doesn't enter this condition as inteded
    if int(window.left_timerno_txt.value) == 0 and int(window.left_timerno_txt.value) == 0:
        print('h')
        show_scores()

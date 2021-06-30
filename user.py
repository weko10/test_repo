import window


def ask_name(title):
    username = window.app.question(title, 'Enter your name:', 'nameless')
    return username

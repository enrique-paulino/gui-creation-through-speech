import re
from word2number import w2n


def split_list(lst, word):  # Splits a list of words by specific word
    idx_list = [idx + 1 for idx, val in
                enumerate(lst) if val == word]
    result = [lst[i: j] for i, j in
              zip([0] + idx_list, idx_list
                  + ([len(lst)] if idx_list[-1] != len(lst) else []))]
    result[0].remove(word)
    return result


def find_widget(widget):  # Function to find widget name (and direction)
    widget_name = widget[0]
    try:
        direction = widget[2]+widget[3]
    except IndexError:
        try:
            direction = widget[2]
        except Exception:
            direction = 0
    return widget_name, direction

    # Temporary fix for speech recognizing two as to
    if (widget[1] == 'to'):
        widget[1] = 'two'

    widget_number = str(w2n.word_to_num(widget[1]))
    widget = widget_name + widget_number
    return widget, direction


def move(widget, direction):  # Function to position widget
    match direction:
        case 'top':
            return widget.pack(side='top', anchor='n')
        case 'bottom':
            return widget.pack(side='bottom', anchor='s')
        case 'left':
            return widget.pack(side='left', anchor='w')
        case 'right':
            return widget.pack(side='right', anchor='e')
        case 'center' | 'centre':
            return widget.place(relx=0.5, rely=0.5, anchor='center')

        case 'topleft':
            return widget.pack(side='top', anchor='nw')
        case 'topright':
            return widget.pack(side='top', anchor='ne')
        case 'bottomleft':
            return widget.pack(side='bottom', anchor='sw')
        case 'bottomright':
            return widget.pack(side='bottom', anchor='se')


def new_command(window, command):  # Command to create new widget
    query = re.search('new (.+)', command)
    if query:
        widget = query.group(1).split()
        try:
            widget = split_list(widget, 'text')
            widget_command = '_'.join(widget[0])
            widget_text = ' '.join(widget[1])
            func = getattr(__import__('widgets'), 'widget_'+widget_command)
            func(window, widget_text)
        except Exception:
            try:
                func = getattr(__import__('widgets'),
                               'widget_'+widget[0])
                func(window, '')
            except Exception as e:
                print('Error, please try again.')
                print(e)


def move_command(window, command):  # Command to move specific widget
    x = window.winfo_children()
    query = re.search('move (.+)', command)
    if query:
        # If there is a number convert it, but if there isnt let it be name
        try:
            widget = query.group(1).split()
            widget, direction = find_widget(widget)
            for i in x:
                # Fix for first widget created of its type has no number
                if ('.!' + widget) == str(i) + '1':
                    move(i, direction)
                if widget in str(i):
                    move(i, direction)
        except Exception:
            pass


def take(command, window):  # Main function
    if 'new' in command:
        new_command(window, command)

    elif 'move' in command:
        move_command(window, command)

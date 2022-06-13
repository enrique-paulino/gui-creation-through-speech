import re
from word2number import w2n


def split_list(lst, word):
    idx_list = [idx + 1 for idx, val in
                enumerate(lst) if val == word]
    result = [lst[i: j] for i, j in
              zip([0] + idx_list, idx_list
                  + ([len(lst)] if idx_list[-1] != len(lst) else []))]
    result[0].remove(word)
    return result


def take(command, window):
    if 'new' in command:
        query = re.search('new (.+)', command)
        if query:
            widget = query.group(1).split()
            widget = split_list(widget, 'text')
            widget_command = '_'.join(widget[0])
            widget_text = ' '.join(widget[1])
            print(widget_text)
            try:
                func = getattr(__import__('widgets'), 'widget_'+widget_command)
                func(window, widget_text)
            except Exception as e:
                print(e)

    elif 'move' in command:
        x = window.winfo_children()
        query = re.search('move (.+)', command)
        if query:
            # If there is a number convert it, but if there isnt let it be name
            try:
                widget = query.group(1).split()
                widget_name = widget[0]

                # Temporary fix for speech recognizing two as to
                if (widget[1] == 'to'):
                    widget[1] = 'two'

                widget_number = str(w2n.word_to_num(widget[1]))
                widget = widget_name + widget_number

                for i in x:
                    # Fix for first widget created of its type has no number
                    if ('.!' + widget) == str(i) + '1':
                        i.place(relx=0.5, rely=0.5, anchor='center')
                    if widget in str(i):
                        i.place(relx=0.5, rely=0.5, anchor='center')  # Center

            except Exception:
                pass

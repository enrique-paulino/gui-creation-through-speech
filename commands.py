import re


def split_list(lst):
    idx_list = [idx + 1 for idx, val in
                enumerate(lst) if val == 'text']
    result = [lst[i: j] for i, j in
              zip([0] + idx_list, idx_list
                  + ([len(lst)] if idx_list[-1] != len(lst) else []))]
    result[0].remove('text')
    return result


def take(command, window):
    if 'new' in command:
        query = re.search('new (.+)', command)
        if query:
            widget = query.group(1).split()
            widget = split_list(widget)
            widget_command = '_'.join(widget[0])
            widget_text = ' '.join(widget[1])
            print(widget_text)
            try:
                func = getattr(__import__('widgets'), 'widget_'+widget_command)
                func(window, widget_text)
            except Exception as e:
                print(e)

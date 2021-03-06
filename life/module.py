import inspect

def event(event):
    events = []
    schedules = []
    todos = []
    for i in event:
        if i.genre == 'Todo':
            todos.append([i.title, f'{i.date}'])
        else:
            schedules.append([i.title, f'{i.date}'])
        events.append([i.title, f'{i.date}'])
    
    if inspect.currentframe().f_back.f_lineno == 91:
        return schedules
    elif inspect.currentframe().f_back.f_lineno == 99:
        return todos
    else:
        return events

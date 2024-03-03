from nicegui import ui
from nicegui.events import ValueChangeEventArguments

import json
# import requests
from collections import OrderedDict
from flask import Flask, request

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzQ5N2EwNWYtZWMzNi00OWU2LTg5N2QtMGIyNzAwYjI4NTVmIiwidHlwZSI6ImFwaV90b2tlbiJ9.5ek4leIgzPBElXbnKfh_uQcRpCbg0nSpEnHShHkdaMQ"}

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('visible', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=3).bind_value(demo, 'number')
    ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')


def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

# ui.button('Button', on_click=lambda: ui.notify('Click'))
# with ui.row():
#     ui.checkbox('Checkbox', on_change=show)
#     ui.switch('Switch', on_change=show)
#     ui.radio(['A', 'B', 'C'], value='A', on_change=show).props('inline')

with ui.row():
    ui.label('Ordered Chaos')

with ui.row():
    ui.input('Photo URL input', on_change=show).bind_value(demo, 'url')

    
with ui.row():
    ui.input('Location of photo', on_change=show)

with ui.row():
    ui.button('Submit', on_click=lambda: ui.notify('Click'))
    
print("url is: " + 'url')

# ui.link('And many more...', '/documentation').classes('mt-8')

ui.run()
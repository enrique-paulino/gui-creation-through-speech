# GUI Creator using Speech Recognition
 A python program that allows the user to create a GUI through speech recognition.

## Commands
  - `new <widget_name>`: Creates widget of that type.   
      - Example: `new button` -> Creates empty button.
    - Optional arguments: `text <string>` -> Adds that string to the widget.
      - Example: `new button text enter` -> Creates button with text 'enter'.

  - `move <widget_name> <direction>`: Moves widget to the specified direction.
    - Example: `move button one left` -> Moves button to left.

## Available Widgets
  - Button
  - Check Button
  - Radio Button
  - Entry
  - Label

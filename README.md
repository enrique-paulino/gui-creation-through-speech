# GUI Creator using Speech Recognition
 A python program that uses threading and Google's voice recognition to allow the user to design a very basic GUI through voice commands. This program is just a proof of concept and would require a large amount of work to measure up to current GUI designing applications. A method to improve this would be to use an already completed GUI design application, such as a drag and drop interface, and associate voice commands to each of the widgets in said program.

## Commands
  `new <widget_name>`: Creates widget of that type.   
   - Optional arguments: `text <string>` -> Adds that string to the widget.
     - Example: `new button` -> Creates empty button.
     - Example: `new button text enter` -> Creates button with text 'enter'.

  `move <widget_name> <direction>`: Moves widget to the specified direction.
   - Example: `move button one left` -> Moves button to left.

  `hide <widget_name>`: Hides specified widget.
  - Example: `hide button one` -> Hides button one.

  `show <widget_name>`: Shows specified widget.
   - Example: `show button one` -> Shows button one.

   `list`: Lists all widgets.
   - Example: `list` -> `.!button, .!label, .!button2`

## Available Widgets
  `BUTTON`, `CHECK BUTTON`, `RADIO BUTTON`  
  `ENTRY`, `LABEL`

## Available Directions
 `TOP`, `BOTTOM`, `LEFT`, `RIGHT`, `CENTER`  
  `TOP LEFT`, `TOP RIGHT`, `BOTTOM LEFT`, `BOTTOM RIGHT`

## How to Run
1. Download project.
2. Navigate to folder in command prompt.
3. Enter `pip install -r requirements.txt`
4. Run `main.py`

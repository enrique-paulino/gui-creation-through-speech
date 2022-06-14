# GUI Creator using Speech Recognition
 A python program that allows the user to create a very basic GUI through speech recognition using voice commands.

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

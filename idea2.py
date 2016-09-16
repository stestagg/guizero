from guizero import *

# This is a Python program that requires the user to type the
# colour of the text and not the name of the colour.
# They have a set time limit and a scoring system.
# If you have any improvements or suggestions I would greatly
# appreciate them.

colors = ["red", "green", "blue"]

def button_clicked(window):
    if window.data['current_color'] == text_input.text:
        you_won()
    button.text = input.text

def change_color(window):
    window.data['current_color'] = random.choice()

window = guizero.Screen()
button = window.add_button(label="go", onclick=button_clicked)
label = window.add_label(text="-")
text_input = window.add_input()
timer1 = window.add_timer(change_color, time=5)

def main():
    window.show()

if __name__ == '__main__':
    main()

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

window = guizero.Screen()
button = window.add_button(label="go", onclick=button_clicked)
label = window.add_label(text="-")
text_input = window.add_input()

def main():
    window.show()
    while True:
        window.data['current_color'] = random.choice()

if __name__ == '__main__':
    main()

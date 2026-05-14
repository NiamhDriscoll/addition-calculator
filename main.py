def on_button_pressed_a():
    global num
    num += 1
    if num == 10:
        num = 1
    basic.show_number(num)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global pls
    pls = num + num1
    basic.show_number(pls)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global num1
    num1 += 1
    if num1 == 10:
        num1 = 1
    basic.show_number(num1)
input.on_button_pressed(Button.B, on_button_pressed_b)

pls = 0
num1 = 0
num = 0
num = 1
num1 = 1
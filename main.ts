input.onButtonPressed(Button.A, function () {
    num += 1
    if (num == 10) {
        num = 1
    }
    basic.showNumber(num)
})
input.onButtonPressed(Button.AB, function () {
    pls = num + num1
    basic.showNumber(pls)
})
input.onButtonPressed(Button.B, function () {
    num1 += 1
    if (num1 == 10) {
        num1 = 1
    }
    basic.showNumber(num1)
})
let pls = 0
let num1 = 0
let num = 0
num = 1
num1 = 1

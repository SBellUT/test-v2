input.onButtonPressed(Button.A, function () {
	
})
input.onButtonPressed(Button.B, function () {
    LCD1IN8.LCD_Clear()
})
max7219_matrix.setup(
1,
DigitalPin.P16,
DigitalPin.P15,
DigitalPin.P14,
DigitalPin.P13
)
max7219_matrix.displayTextAlignRight(
"H",
true
)
basic.forever(function () {
	
})

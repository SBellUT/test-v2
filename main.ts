input.onPinPressed(TouchPin.P0, function () {
    max7219_matrix.clearAll()
})
input.onPinReleased(TouchPin.P0, function () {
    max7219_matrix.displayTextAlignRight(
    happySad,
    true
    )
})
input.onButtonPressed(Button.A, function () {
    if (!(input.pinIsPressed(TouchPin.P0))) {
        randomAnimation = randomAnimation * -1
        max7219_matrix.displayTextAlignRight(
        happySad,
        true
        )
    }
})
input.onPinPressed(TouchPin.P1, function () {
    if (!(input.pinIsPressed(TouchPin.P0))) {
        playExplode = playExplode * -1
        max7219_matrix.displayTextAlignRight(
        happySad,
        true
        )
    }
})
let brightness = 0
let degrees = 0
let voltage = 0
let sensorVal = 0
let happySad = ""
let playExplode = 0
let randomAnimation = 0
let vcc = 3.3
let full_angle = 300
randomAnimation = 1
playExplode = 1
let makeNoise = 1
happySad = ":)"
max7219_matrix.setup(
1,
DigitalPin.P16,
DigitalPin.P15,
DigitalPin.P14,
DigitalPin.P13
)
max7219_matrix.for_4_in_1_modules(
rotation_direction.clockwise,
false
)
max7219_matrix.displayTextAlignRight(
happySad,
true
)
basic.forever(function () {
    if (input.pinIsPressed(TouchPin.P0)) {
        max7219_matrix.clearAll()
    }
    sensorVal = pins.analogReadPin(AnalogPin.P2)
    voltage = Math.idiv(sensorVal * vcc, 1023)
    degrees = Math.idiv(voltage * full_angle, vcc)
    brightness = Math.map(degrees, 0, full_angle, 0, 255)
    max7219_matrix.brightnessAll(brightness)
    basic.pause(500)
})
basic.forever(function () {
    while (randomAnimation < 0) {
        max7219_matrix.randomizeAll()
        basic.pause(100)
    }
    while (playExplode < 0) {
        max7219_matrix.fillAll()
        basic.pause(100)
        max7219_matrix.clearAll()
        basic.pause(100)
    }
})

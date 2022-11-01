def on_pin_pressed_p0():
    max7219_matrix.clear_all()
    max7219_matrix.brightness_all(0)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_released_p0():
    control.reset()
input.on_pin_released(TouchPin.P0, on_pin_released_p0)

def on_button_pressed_a():
    global randomAnimation
    if not (input.pin_is_pressed(TouchPin.P0)):
        randomAnimation = randomAnimation * -1
        max7219_matrix.display_text_align_right(happySad, True)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p1():
    global happySad
    if not (input.pin_is_pressed(TouchPin.P0)):
        if happySad == ":)":
            music.play_tone(349, music.beat(BeatFraction.WHOLE))
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            music.play_tone(294, music.beat(BeatFraction.WHOLE))
            music.play_tone(220, music.beat(BeatFraction.DOUBLE))
            happySad = ":("
        else:
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
            music.play_tone(294, music.beat(BeatFraction.WHOLE))
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            music.play_tone(523, music.beat(BeatFraction.DOUBLE))
            happySad = ":)"
        max7219_matrix.display_text_align_right(happySad, True)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

brightness = 0
degrees = 0
voltage = 0
sensorVal = 0
happySad = ""
randomAnimation = 0
vcc = 3.3
full_angle = 300
randomAnimation = 1
playExplode = 1
makeNoise = 1
happySad = ":)"
max7219_matrix.setup(1,
    DigitalPin.P16,
    DigitalPin.P15,
    DigitalPin.P14,
    DigitalPin.P13)
max7219_matrix.for_4_in_1_modules(rotation_direction.CLOCKWISE, False)
max7219_matrix.display_text_align_right(happySad, True)

def on_forever():
    global sensorVal, voltage, degrees, brightness
    if input.pin_is_pressed(TouchPin.P0):
        max7219_matrix.clear_all()
    sensorVal = pins.analog_read_pin(AnalogPin.P2)
    voltage = Math.idiv(sensorVal * vcc, 1023)
    degrees = Math.idiv(voltage * full_angle, vcc)
    brightness = Math.map(degrees, 0, full_angle, 0, 255)
    max7219_matrix.brightness_all(brightness)
    music.set_volume(brightness)
    basic.pause(500)
basic.forever(on_forever)

def on_forever2():
    while randomAnimation < 0:
        max7219_matrix.randomize_all()
        basic.pause(100)
    while playExplode < 0:
        max7219_matrix.fill_all()
        basic.pause(100)
        max7219_matrix.clear_all()
        basic.pause(100)
basic.forever(on_forever2)

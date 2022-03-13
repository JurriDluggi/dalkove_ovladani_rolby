y = 0
x = 0
radio.set_group(1)

def on_forever():
    global x, y
    x = Math.map(joystickbit.get_rocker_value(joystickbit.rockerType.X),
        1023,
        0,
        45,
        135)
    y = Math.map(joystickbit.get_rocker_value(joystickbit.rockerType.Y),
        1023,
        0,
        -100,
        100)
    radio.send_value("x", x)
    radio.send_value("y", y)
basic.forever(on_forever)

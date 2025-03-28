import time
import board
import digitalio

# Initialize GPIO15 as an input with an internal pull-up resistor
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # Ensures default state is HIGH

# Initialize LED pins (Modify if needed)
led_pins = [board.GP10, board.GP11, board.GP12, board.GP13]
leds = []

# Set up LEDs as outputs
for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

def run_sequence():
    """Function to execute when the button is pressed"""
    print("Button Pressed! Executing sequence...")

    # Example sequence: Blink LEDs in order
    for i in range(3):  # Blink sequence 3 times
        for led in leds:
            led.value = True  # Turn ON LED
            time.sleep(0.5)
            led.value = False  # Turn OFF LED
            time.sleep(0.5)

    print("Sequence complete. Waiting for next press...")

while True:
    # Wait for button press (active-low)
    while button.value:  
        pass  # Do nothing until button is pressed (button.value goes LOW)

    # Button is pressed; execute the sequence
    run_sequence()

    # Wait until the button is released before continuing
    while not button.value:
        pass  # Do nothing until button is released

    print("Ready for the next press...")


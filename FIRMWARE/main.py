import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Define your matrix pins (adjust to match your wiring)
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D8, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define what each key does
keyboard.keymap = [
    [KC.ESCAPE, KC.L, KC.R, KC.A],
    [KC.G, KC.C, KC.M, KC.P],
    [KC.D, KC.O, KC.LSFT(KC.E), KC.LSFT(KC.S)]
]

if __name__ == "__main__":
    keyboard.go()
import os
import msvcrt

def select_option(options):
    pointerIndex = 0

    def display_menu():
        os.system("cls")
        for i, option in enumerate(options):
            if i == pointerIndex:
                print(f"> {option}")
            else:
                print(f"  {option}")

    display_menu()

    while True:
        key = msvcrt.getch()

        if key == b"\xe0":
            key = msvcrt.getch()
            if key == b"H" and pointerIndex > 0:
                pointerIndex -= 1
            elif key == b"P" and pointerIndex < len(options) - 1:
                pointerIndex += 1
        elif key == b"\r":
            return options[pointerIndex]

        display_menu()

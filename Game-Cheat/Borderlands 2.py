from pymem import *
from pymem.process import *
import keyboard
import pyautogui

mem = Pymem("Borderlands2.exe")
module = module_from_name(mem.process_handle, "Borderlands2.exe").lpBaseOfDll
offsets = [0xDC, 0x54, 0x38, 0x28, 0x988, 0x728, 0xA28]
shortcut_1 = "F1"
shortcut_2 = "F2"


def get_pointer(base, offsets_list):
    address = mem.read_int(base)
    for offset in offsets_list:
        if offset != offsets_list[-1]:
            address = mem.read_int(address + offset)
    address = address + offsets_list[-1]
    return address


while True:
    if keyboard.is_pressed(shortcut_1):
        mem.write_int(get_pointer(module + 0x01653994, offsets), 9)
    elif keyboard.is_pressed(shortcut_2):
        for i in range(6000):
            pyautogui.keyDown("Enter", _pause=False)
            pyautogui.keyUp("Enter", _pause=False)

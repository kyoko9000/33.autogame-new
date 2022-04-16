# from pymem import *
# from pymem.process import *
from pymem import Pymem
from pymem.process import module_from_name

mem = Pymem("sro_client.exe")  # tên trong task manager
game_module = module_from_name(mem.process_handle, "sro_client.exe").lpBaseOfDll  # tên trong cheat engine

def getPtrAddr(address, offsets):
    addr = mem.read_int(address)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = mem.read_int(addr + offset)
    addr = addr + offsets[-1]
    return addr
# while True:
mem.write_float(getPtrAddr(game_module + 0x00D14868, [0x740, 0x30]), 1200.0)
z = mem.read_float(getPtrAddr(game_module + 0x00D14868, [0x740, 0x34]))
x = mem.read_float(getPtrAddr(game_module + 0x00D14868, [0x740, 0x38]))
y = mem.read_float(getPtrAddr(game_module + 0x00D14868, [0x740, 0x30]))
print(int(z), int(x), int(y))
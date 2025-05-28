import pyautogui as gui
import keyboard as kb

clicker = False


def move():
    m_pos = gui.position()
    gui.moveTo(m_pos.x, m_pos.y, duration=0.25)
    gui.moveTo(m_pos.x + 100, m_pos.y, duration=0.25)
    gui.moveTo(m_pos.x + 100, m_pos.y + 100, duration=0.25)
    gui.moveTo(m_pos.x, m_pos.y + 100, duration=0.25)
    gui.moveTo(m_pos.x, m_pos.y, duration=0.25)


def draw():
    change = 0
    m_pos = gui.position()
    for i in range(5):
        gui.dragTo(m_pos.x - change, m_pos.y - change, duration=0.25)
        gui.dragTo(m_pos.x + 100 - change, m_pos.y - change, duration=0.25)
        gui.dragTo(m_pos.x + 100 - change, m_pos.y + 100 - change, duration=0.25)
        gui.dragTo(m_pos.x - change, m_pos.y + 100 - change, duration=0.25)
        gui.dragTo(m_pos.x - change, m_pos.y - change, duration=0.25)
        change += 10

def autoclicker():
    if clicker:
        gui.click(interval=0.32, _pause=False)
        print(1)

while True:
    if clicker:
        autoclicker()
    if kb.is_pressed("1"):
        clicker = True
    if kb.is_pressed("2"):
        clicker = False
    if kb.is_pressed("3"):
        move()
    if kb.is_pressed("4"):
        draw()

import math
import time
import pyautogui as gui
import keyboard as key


def get_pixel(image, x, y):
    px = image.load()
    return px[x, y]


def detect_obstacle_size(image, x, ground_y, bg_color):
    height = 0
    width = 0

    for offset in range(0, 20):
        if get_pixel(image, x + offset, ground_y) != bg_color:
            width += 1
        else:
            break

    for offset in range(0, 30):
        if get_pixel(image, x, ground_y - offset) != bg_color:
            height += 1
        else:
            break
    return width, height


def game():
    print("я работаю")
    x, y, width, height = 0, 0, 1920, 1080
    y_up, y_down, x_left, x_right = 400, 410, 700, 745
    y_search_for_bird = 390


    last_jump_time = 0
    last_interval_time = 0


    while True:
        sct_img = gui.screenshot(region=(x, y, width, height))
        bg_color = get_pixel(sct_img, 300, 300)
        #print(bg_color)

        for i in range(x_right, x_left, -1):
            if get_pixel(sct_img, i, y_up) != bg_color or get_pixel(sct_img, i, y_down) != bg_color:
                width_obstacle, height_obstacle = detect_obstacle_size(sct_img, i, y_down, bg_color)
                #print("Препятствие!", width_obstacle, height)
                if height_obstacle > 20 or width_obstacle > 15:
                    key.press("up")
                    time.sleep(0.2)
                    key.release("up")
                    print(f'HIGH jump | Width: {width_obstacle}, Height: {height_obstacle}')

                else:
                    key.press("up")
                    time.sleep(0.08)
                    key.release("up")
                    print(f'HIGH jump | Width: {width_obstacle}, Height: {height_obstacle}')

                jump_time = time.time()
                interval_time = jump_time - last_jump_time
                last_jump_time = jump_time

                if math.floor(interval_time) != math.floor(last_interval_time):
                    x_right += 2
                    if x_right >= width:
                        x_right = width
                    last_interval_time = interval_time

                break

            elif get_pixel(sct_img, i, y_search_for_bird) != bg_color:
                key.press("down")
                time.sleep(0.4)
                key.release("down")
                #print("Bird")
                break



if __name__ == "__main__":
    game()
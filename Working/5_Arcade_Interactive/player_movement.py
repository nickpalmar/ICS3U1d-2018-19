import arcade
from random import *
from math import *

WIDTH = 640
HEIGHT = 480

# start player position in middle of window
player_x = WIDTH/2
player_y = HEIGHT/2 + 50
player_rad = 30

# Variables to record if certain keys are being pressed.
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False


# speed var for player
speed_y1 = 0
speed_y2 = 0
speed_x1 = 0
speed_x2 = 0

# coin var
coin_x = WIDTH/2
coin_y = randint(30, HEIGHT-30)
coin_rad = 10
coin_spx = 1
spx_change = 0

amp = randint(20, 150)
k_val = randint(1, 8)
axis = randint(200, 300)

# score var
score = 0

def on_update(delta_time):
    global up_pressed, player_y, speed_y1, player_x, left_pressed, speed_y2, speed_x1, speed_x2, right_pressed, coin_x
    global coin_y, player_rad, coin_rad, score, coin_spx, amp, axis, k_val, spx_change

    # check if player is outside of the screen and change speeds accordingly
    if up_pressed:
        player_y += speed_y1
    if player_y >= HEIGHT - 30:
        speed_y1 = 0
    else:
        speed_y1 = 10

    if down_pressed:
        player_y += speed_y2
    if player_y <= 30:
        speed_y2 = 0
    else:
        speed_y2 = -10

    if left_pressed:
        player_x += speed_x1
    if player_x < 30:
        speed_x1 = 0
    else:
        speed_x1 = -10

    if right_pressed:
        player_x += speed_x2
    if player_x >= WIDTH - 30:
        speed_x2 = 0
    else:
        speed_x2 = 10
    # calculate distance of player from coin, then check if they are touching
    distance = ((player_x - coin_x)**2 + (player_y - coin_y)**2) ** 0.5
    if coin_x >= WIDTH-30 or coin_x <= 30:
        coin_spx *= 0
        arcade.draw_text("L", WIDTH/2, HEIGHT/2, arcade.color.RED, 70)
    elif distance <= coin_rad + player_rad:
        coin_x = WIDTH/2
        coin_y = randint(30, HEIGHT-30)
        score += 1
        amp = randint(20, 150)
        k_val = randint(1, 8)
        axis = randint(200, 300)
        spx_change += 1
        random_direction = randint(0, 2)
        if random_direction == 0:
            coin_spx = -(sqrt(spx_change))
        else:
            coin_spx = sqrt(spx_change)

    # coin motion
    coin_y = amp * sin((k_val*0.01) * coin_x) + axis
    coin_x += coin_spx


def on_draw():
    global player_x, player_y, coin_x, coin_y, player_rad, coin_rad, score, WIDTH, HEIGHT
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(player_x, player_y, player_rad, arcade.color.BLUE)

    # draw_coin
    arcade.draw_circle_filled(coin_x, coin_y, coin_rad, arcade.color.GOLD)

    # write score text
    arcade.draw_text(str(score), 30, HEIGHT - 30, arcade.color.BLACK, 10)

    if coin_x >= WIDTH-30 or coin_x <= 30:
        arcade.draw_text("L", WIDTH/2 - 40, HEIGHT/2 - 40, arcade.color.RED, 70)


def on_key_press(key, modifiers):
    global up_pressed, left_pressed, down_pressed, right_pressed
    if key == arcade.key.W:
        up_pressed = True
    if key == arcade.key.S:
        down_pressed = True
    if key == arcade.key.A:
        left_pressed = True
    if key == arcade.key.D:
        right_pressed = True


def on_key_release(key, modifiers):
    global up_pressed, left_pressed, down_pressed, right_pressed
    if key == arcade.key.W:
        up_pressed = False
    if key == arcade.key.S:
        down_pressed = False
    if key == arcade.key.A:
        left_pressed = False
    if key == arcade.key.D:
        right_pressed = False


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()

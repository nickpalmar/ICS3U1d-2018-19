import arcade


WIDTH = 640
HEIGHT = 480

# start player position in middle of window
player_x = WIDTH/2
player_y = HEIGHT/2

# Variables to record if certain keys are being pressed.
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False


# speed var
speed_y1 = 5
speed_y2 = -5
speed_x1 = -5
speed_x2 = 5

def on_update(delta_time):
    global up_pressed, player_y, speed_y1, player_x, left_pressed, speed_y2, speed_x1, speed_x2, right_pressed
    if up_pressed:
        player_y += speed_y1
    if player_y > HEIGHT - 30:
        speed_y1 = 0
    else:
        speed_y1 = 10

    if down_pressed:
        player_y += speed_y2
    if player_y < 30:
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
    if player_x > WIDTH - 30:
        speed_x2 = 0
    else:
        speed_x2 = 10

    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.BLUE)





def on_draw():
    global player_x, player_y
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.BLUE)


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

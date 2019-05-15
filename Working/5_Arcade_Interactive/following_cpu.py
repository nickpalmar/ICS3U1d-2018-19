import arcade


WIDTH = 640
HEIGHT = 480

# player vars
player_x = 100
player_y = 100
player_radius = 25

# cpu vars
cpu_x = 30
cpu_y = 30
cpu_radius = 25
repel = False

def on_update(delta_time):
    global player_x, player_y, cpu_x, cpu_y, cpu_radius, repel

    # check if balls collide, also attract them
    distance = ((player_x-cpu_x)**2 + (player_y-cpu_y)**2)**0.5
    slope_y = player_y - cpu_y
    slope_x = player_x - cpu_x
    if distance <= cpu_radius*2 or repel:
        repel = True
        if distance > cpu_radius*8:
            repel = False
        elif distance > cpu_radius*4:
            cpu_x += slope_x * -0.01
            cpu_y += slope_y * -0.01
        else:
            cpu_x += slope_x * -0.2
            cpu_y += slope_y * -0.2

    else:
        cpu_x += slope_x * 0.01
        cpu_y += slope_y * 0.01
        repel = False



def on_draw():
    global player_x, player_y, cpu_x, cpu_y, cpu_radius
    arcade.start_render()
    # player
    arcade.draw_circle_filled(player_x, player_y, player_radius, arcade.color.BLUE)

    # cpu
    arcade.draw_circle_filled(cpu_x, cpu_y, cpu_radius, arcade.color.BLACK)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global player_x, player_y
    player_x = x
    player_y = y



def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
import arcade

# screen dimension variables
WIDTH = 600
HEIGHT = 600

# pacman variables
pac_x = 300
pac_y = 200
pac_rad = 20
init_arc_angle = 0
final_arc_angle = 360
# pacman as a circle (0) or arc(1)
pacman_character = 1

# arrow key variables
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False
pac_speed_x = 0
pac_speed_y = 0
time = 0

# maze/wall variables
perim_walls = []
wall_dimension = 40
wall_rows = 15
wall_columns = 15
perim_wall_pos = []


def on_update(delta_time):
    global pacman_character, time

    pac_move()

    # change pacman's outfit (open mouth to closed mouth and vice versa)
    time += delta_time
    if time > 0.1:
        if pacman_character == 0:
            pacman_character = 1
        elif pacman_character == 1:
            pacman_character = 0
        time = 0


def pac_move():
    global final_arc_angle, time, pacman_character, perim_walls, wall_dimension, wall_rows, wall_columns, perim_wall_pos
    global up_pressed, down_pressed, left_pressed, right_pressed, pac_x, pac_y, pac_rad, pac_speed_x, init_arc_angle
    global pac_speed_y
    # check if pacman is in contact with perimeter walls
    pac_stop = False
    for i in range(len(perim_wall_pos)):
        # calculate distance from pacman to wall, it touching make him stop moving
        pac_to_perim = ((perim_wall_pos[i][0] - pac_x) ** 2 + (perim_wall_pos[i][1] - pac_y) ** 2) ** (1 / 2)
        if pac_to_perim <= ((wall_dimension // 2) + pac_rad):
            pac_stop = True
            current_wall_distance = pac_to_perim

    # set pac speeds depending on keys pressed
    if up_pressed:
        pac_speed_y = 5
    elif down_pressed:
        pac_speed_y = -5
    elif left_pressed:
        pac_speed_x = -5
    elif right_pressed:
        pac_speed_x = 5

    # check if player motion can move pacman away from tbe wall
    if pac_stop:
        if (pac_speed_x + current_wall_distance >= wall_dimension // 2 + pac_rad) or (
                pac_speed_y + current_wall_distance >= wall_dimension // 2 + pac_rad):
            pac_stop = False
    # if in contact, stop him
    if pac_stop == False:
        # check if any keys are pressed and move pacman accordingly
        if up_pressed or down_pressed:
            if up_pressed:
                init_arc_angle = 135
                final_arc_angle = 405
            elif down_pressed:
                init_arc_angle = 315
                final_arc_angle = 585
            pac_speed_x = 0
        elif left_pressed or right_pressed:
            if left_pressed:
                init_arc_angle = 225
                final_arc_angle = 495
            elif right_pressed:
                init_arc_angle = 45
                final_arc_angle = 315
            pac_speed_y = 0

        # move pacman
        pac_x += pac_speed_x
        pac_y += pac_speed_y
    else:
        if up_pressed or down_pressed:
            pac_speed_y = 0
        elif left_pressed or right_pressed:
            pac_speed_x = 0
    print(pac_speed_x, pac_speed_y)


def on_draw():
    global pac_x, pac_y, pacman_character, perim_walls, wall_dimension, WIDTH, HEIGHT
    arcade.start_render()

    draw_perim_walls()

    # Draw pacman, alternating
    if pacman_character == 1:
        draw_pacman_open(pac_x, pac_y)
    else:
        draw_pacman_closed(pac_x, pac_y)


def draw_perim_walls():
    global WIDTH, wall_dimension, perim_walls, HEIGHT, wall_rows, wall_columns, perim_wall_pos
    for r in range(wall_rows):
        for c in range(wall_columns):
            if (r == 0 or c == 0 or r == 14 or c == 14) and r != 7:
                perim_walls[r][c] = 1
            else:
                perim_walls[r][c] = 0
    # draw the perimeter perim_walls
    for row in range(wall_rows):
        for column in range(wall_columns):
            if perim_walls[row][column] == 1:
                colour = arcade.color.BLUE
                # find wall x and y pos
                wall_x = column * 40 + wall_dimension / 2
                wall_y = row * 40 + wall_dimension / 2
                perim_wall_pos.append([wall_x, wall_y])
                # draw perim_walls and maze
                arcade.draw_rectangle_filled(wall_x, wall_y, wall_dimension, wall_dimension, colour)


def draw_pacman_closed(x, y):
    global pac_rad
    arcade.draw_circle_filled(x, y, pac_rad, arcade.color.YELLOW)


def draw_pacman_open(x, y):
    global pac_rad, init_arc_angle, final_arc_angle
    arcade.draw_arc_filled(x, y, pac_rad, pac_rad, arcade.color.YELLOW, init_arc_angle, final_arc_angle)


def on_key_press(key, modifiers):
    global up_pressed, down_pressed, left_pressed, right_pressed
    # create a key list
    key_pressed_list = [0] * 4

    # check if any key is pressed, if it is set that direction to true (move in 1 direction)
    if key == arcade.key.UP:
        up_pressed = True
        key_pressed_list[0] = 1
    elif key == arcade.key.DOWN:
        down_pressed = True
        key_pressed_list[1] = 1
    elif key == arcade.key.LEFT:
        left_pressed = True
        key_pressed_list[2] = 1
    elif key == arcade.key.RIGHT:
        right_pressed = True
        key_pressed_list[3] = 1
    key_pressed_boolean = [up_pressed, down_pressed, left_pressed, right_pressed]

    # turn off all keys which are not pressed, account for no on key released
    for i in range(len(key_pressed_list)):
        if key_pressed_list[i] == 0:
            key_pressed_boolean[i] = False
    up_pressed = key_pressed_boolean[0]
    down_pressed = key_pressed_boolean[1]
    left_pressed = key_pressed_boolean[2]
    right_pressed = key_pressed_boolean[3]


def setup():
    global WIDTH, HEIGHT, wall_rows, wall_columns, perim_walls
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press

    # create an list for the perim_walls
    for row in range(wall_rows):
        perim_walls.append([])
        for column in range(wall_columns):
            perim_walls[row].append(0)
    arcade.run()


if __name__ == '__main__':
    setup()
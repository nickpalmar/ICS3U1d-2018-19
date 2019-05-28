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
# is pacman in contact with perimeter walls, can pacman move U,D,L,R
pac_stop = [False]*4
pac_poss_motion = [True]*4
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
perim_wall_pos1 = 300
perim_wall_pos2 = 20
perim_wall_width = 600
perim_wall_height = 40
current_wall_distance = []


def on_update(delta_time):
    global pacman_character, time, pac_stop

    wall_outer_side = pac_stop_perim()

    # pac_move(wall_outerside)

    # change pacman's outfit (open mouth to closed mouth and vice versa)
    time += delta_time
    if time > 0.075:
        if pac_stop:
            pacman_character = 0
        elif pacman_character == 0:
            pacman_character = 1
        elif pacman_character == 1:
            pacman_character = 0
        time = 0


def pac_move():
    global final_arc_angle, time, pacman_character, up_pressed, down_pressed, left_pressed, right_pressed, pac_x, pac_y, pac_rad, pac_speed_x, init_arc_angle
    global pac_speed_y, perim_wall_pos1, perim_wall_pos2, perim_wall_width, perim_wall_height, current_wall_distance
    global WIDTH, HEIGHT, pac_stop, pac_poss_motion
    # set pac speeds depending on keys pressed
    if up_pressed:
        pac_speed_y = 2.5
    elif down_pressed:
        pac_speed_y = -2.5
    elif left_pressed:
        pac_speed_x = -2.5
    elif right_pressed:
        pac_speed_x = 2.5

    for i in range(len(pac_stop)):
        if pac_stop[i] == False:
            # check if any keys are pressed and stop all other motions accordingly
            if up_pressed:
                pac_speed_x = 0
            elif down_pressed:
                pac_speed_x = 0

            if left_pressed:
                pac_speed_y = 0
            elif right_pressed:
                pac_speed_y = 0

        # else:
            # check if pacman can still move in direction pressed

        if pac_stop[i]:
            # do not allow pacman to move past walls
            # do not pass top
            if pac_poss_motion[0] == False:
                if pac_speed_y > 0:
                    pac_speed_y = 0
                # else:
                #     pac_stop =
            # do not pass bottom
            elif pac_poss_motion[1] == False:
                if pac_speed_y < 0:
                    pac_speed_y = 0

            # do not pass left
            if pac_poss_motion[2] == False:
                if pac_speed_x < 0:
                    pac_speed_x = 0
            # do not pass right
            if pac_poss_motion[3] == False:
                if pac_speed_x > 0:
                    pac_speed_x = 0

    if up_pressed:
        init_arc_angle = 135
        final_arc_angle = 405
    elif down_pressed:
        init_arc_angle = 315
        final_arc_angle = 585
    if left_pressed:
        init_arc_angle = 225
        final_arc_angle = 495
    elif right_pressed:
        init_arc_angle = 45
        final_arc_angle = 315
    # move pacman
    pac_x += pac_speed_x
    pac_y += pac_speed_y



def pac_stop_perim():
    global final_arc_angle, time, pacman_character, up_pressed, down_pressed, left_pressed, right_pressed, pac_x, pac_y, pac_rad, pac_speed_x, init_arc_angle
    global pac_speed_y, perim_wall_pos1, perim_wall_pos2, perim_wall_width, perim_wall_height, current_wall_distance
    global WIDTH, HEIGHT, pac_stop, pac_poss_motion
    # calculate distance from pacman to base wall, it touching make him stop moving
    d_to_base = pac_y - (perim_wall_pos2 + perim_wall_height // 2 - pac_rad)
    d_to_left = pac_x - (perim_wall_pos2 + perim_wall_height // 2 - pac_rad)
    d_to_right = (perim_wall_pos1 + perim_wall_width // 2 - pac_rad) - pac_x
    d_to_top = (perim_wall_pos1 + perim_wall_width // 2 - pac_rad) - pac_y

    # set the pacman distance
    current_wall_distance = [0] * 4
    current_wall_distance[0] = d_to_base
    current_wall_distance[1] = d_to_left
    current_wall_distance[2] = d_to_right
    current_wall_distance[3] = d_to_top

    # reset variables
    # pac_poss_motion = [True]*4
    pac_stop = [False]*4
    # set the index at 4; not touching
    current_wall_index = 4

    # check if pacman in contact with wall, and store the wall
    if d_to_base <= pac_rad + perim_wall_height // 2:
        pac_stop[0] = True
    elif d_to_top <= pac_rad + perim_wall_height // 2:
        pac_stop[1] = True
    if d_to_left <= pac_rad + perim_wall_height // 2:
        pac_stop[2] = True
    elif d_to_right <= pac_rad + perim_wall_height // 2:
        pac_stop[3] = True

    # for

    # if touching, return values
    return pac_stop[current_wall_index]



def on_draw():
    global pac_x, pac_y, pacman_character, perim_walls, wall_dimension, WIDTH, HEIGHT
    global perim_wall_pos1, perim_wall_pos2, perim_wall_width, perim_wall_height
    arcade.start_render()

    # base wall
    draw_perim_walls(perim_wall_pos1, perim_wall_pos2, perim_wall_width, perim_wall_height)
    # left_wall
    draw_perim_walls(perim_wall_pos2, perim_wall_pos1, perim_wall_height, perim_wall_width)
    #top wall
    draw_perim_walls(perim_wall_pos1, HEIGHT - perim_wall_pos2, perim_wall_width, perim_wall_height)
    # right wall
    draw_perim_walls(WIDTH - perim_wall_pos2, perim_wall_pos1, perim_wall_height, perim_wall_width)

    # Draw pacman, alternating
    if pacman_character == 1:
        draw_pacman_open(pac_x, pac_y)
    else:
        draw_pacman_closed(pac_x, pac_y)


def draw_perim_walls(perim_wall_basex, perim_wall_basey, width, height):
    # draw a peremiter wall
    arcade.draw_rectangle_filled(perim_wall_basex, perim_wall_basey, width, height, arcade.color.BLUE)


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

    arcade.run()


if __name__ == '__main__':
    setup()
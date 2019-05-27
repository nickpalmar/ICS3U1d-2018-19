import arcade

WIDTH = 1240
HEIGHT = 680

# tile dimension; wall fits to tile
tile_width = 40
tile_height = 40

# pellet dimension
pellet_rad = 5

# create grid variables
pac_grid = []
row_count = 15
column_count = 31

# pacman variables
pac_x = 60
pac_y = 60
pac_rad = 20
init_arc_angle = 0
final_arc_angle = 360
pac_skin = 0

# arrow key variables
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False
pac_speed_x = 0
pac_speed_y = 0

# time variable
time = 0

#  score variables
score = 0

# wall image
texture = arcade.load_texture("pacific-blue-high-sheen-merola-tile-mosaic-tile-fyfl1spa-64_1000.jpg")


def on_update(delta_time):
    global pac_x, pac_y, time, pac_speed_x, pac_speed_y
    wall_touch = wall_collision(pac_x, pac_y)
    pac_move(wall_touch)
    pac_object_detection(pac_x, pac_y)

    # open and close pac mans mouth
    time += delta_time
    if time >= 0.075:
        change_skin()
        time = 0


def on_draw():
    global pac_grid, row_count, column_count, tile_width, tile_height, pac_x ,pac_y, score

    # draw out the current grid
    arcade.start_render()
    for row in range(row_count):
        for column in range(column_count):
            # calculate tile position
            tile_centre_x = (column + 1) * tile_width - 20
            tile_centre_y = (row + 1) * tile_height - 20
            # check if wall
            if pac_grid[row][column] == 0:
                draw_wall_tile(tile_centre_x, tile_centre_y)
            # check if pellet
            elif pac_grid[row][column] == 1:
                draw_pellet(tile_centre_x, tile_centre_y)

    # draw pacman
    draw_pac(pac_x, pac_y)

    # draw the score
    write_score(score)


def write_score(score):
    arcade.draw_text(str(score), 40, 640, arcade.color.WHITE, 40)


def change_skin():
    # change pacman from open to close mouth
    global pac_skin
    if pac_skin == 1:
        pac_skin = 0
    else:
        pac_skin = 1


def draw_pac(x, y):
    global pac_skin
    # open mouth
    if pac_skin == 0:
        draw_pacman_open(x, y)
    # close mouth
    else:
        draw_pacman_closed(x, y)


def wall_collision(x, y):
    global tile_height, tile_width, pac_rad, pac_grid, row_count, column_count
    # check if pacman is in the middle of a tile
    if x <= 600:
        check_x = (x + (tile_width//2)) % tile_width
    else:
        check_x = (x - (tile_width//2)) % tile_width

    if y <= 300:
        check_y = (y + (tile_width // 2)) % tile_width
    else:
        check_y = (y - (tile_width // 2)) % tile_width

    # in the middle of a tile
    if check_x == 0 and check_y == 0:
        # calculate pacman tile
        pac_column  = int(((x + 20) // 40) - 1)
        pac_row = int(((y + 20) // 40) - 1)

        # calculte rows and columns adjectent to pacman
        row_above = pac_row + 1
        row_below = pac_row - 1
        column_left = pac_column - 1
        column_right = pac_column + 1

        wall_touch = []

        # check if adjacent tiles are walls or not
        if pac_grid[row_above][pac_column] == 0:
            wall_touch.append("up")
        if pac_grid[row_below][pac_column] == 0:
            wall_touch.append("down")
        if pac_grid[pac_row][column_left] == 0:
            wall_touch.append("left")
        if pac_grid[pac_row][column_right] == 0:
            wall_touch.append("right")

        return wall_touch

    # not in mid tile
    else:
        return "null"


def pac_move(wall_touch):
    global pac_speed_x, pac_speed_y, up_pressed, down_pressed, left_pressed, right_pressed, pac_x, pac_y
    global init_arc_angle, final_arc_angle

    # check if mid-tile, check wall collision
    if wall_touch != "null":
        # pacman motion depending on key pressed
        if up_pressed:
            pac_speed_y = 5
            pac_speed_x = 0
            init_arc_angle = 135
            final_arc_angle = 405
        elif down_pressed:
            pac_speed_y = -5
            pac_speed_x = 0
            init_arc_angle = 315
            final_arc_angle = 585
        elif left_pressed:
            pac_speed_x = -5
            pac_speed_y = 0
            init_arc_angle = 225
            final_arc_angle = 495
        elif right_pressed:
            pac_speed_x = 5
            pac_speed_y = 0
            init_arc_angle = 45
            final_arc_angle = 315

        # loop through the walls that are touching, restrict motion in certain directions
        for wall in wall_touch:
            # restrict up motion
            if wall == "up" and pac_speed_y > 0:
                pac_speed_y = 0
                init_arc_angle = 0
                final_arc_angle = 360
            # restrict down motion
            if wall == "down" and pac_speed_y < 0:
                pac_speed_y = 0
                init_arc_angle = 0
                final_arc_angle = 360
            # restict left motion
            if wall == "left" and pac_speed_x < 0:
                pac_speed_x = 0
                init_arc_angle = 0
                final_arc_angle = 360
            # restrict right motion
            if wall == "right" and pac_speed_x > 0:
                pac_speed_x = 0
                init_arc_angle = 0
                final_arc_angle = 360

    # move pacman
    pac_x += pac_speed_x
    pac_y += pac_speed_y


def pac_object_detection(x, y):
    global tile_height, tile_width, pac_rad, pac_grid, row_count, column_count, score
    # check if pacman is in the middle of a tile
    if x <= 600:
        check_x = (x + (tile_width // 2)) % tile_width
    else:
        check_x = (x - (tile_width // 2)) % tile_width

    if y <= 300:
        check_y = (y + (tile_width // 2)) % tile_width
    else:
        check_y = (y - (tile_width // 2)) % tile_width

    # in the middle of a tile
    if check_x == 0 and check_y == 0:
        # calculate pacman tile
        pac_column = int(((x + 20) // 40) - 1)
        pac_row = int(((y + 20) // 40) - 1)

        # check if pacman is on a pellet
        if pac_grid[pac_row][pac_column] == 1:
            # change status to nothing
            pac_grid[pac_row][pac_column] = 2
            score += 10


def draw_wall_tile(x, y):
    global tile_height, tile_width, texture
    # arcade.draw_rectangle_filled(x, y, tile_width, tile_height, arcade.color.BLUE)
    # texture = arcade.load_texture("pacific-blue-high-sheen-merola-tile-mosaic-tile-fyfl1spa-64_1000.jpg")
    # display fire image on screen
    arcade.draw_texture_rectangle(x, y, tile_width, tile_height, texture, 0)


def draw_pacman_closed(x, y):
    global pac_rad
    arcade.draw_circle_filled(x, y, pac_rad, arcade.color.YELLOW)


def draw_pacman_open(x, y):
    global pac_rad, init_arc_angle, final_arc_angle
    arcade.draw_arc_filled(x, y, pac_rad, pac_rad, arcade.color.YELLOW, init_arc_angle, final_arc_angle)


def draw_pellet(x, y):
    global pellet_rad
    # arcade.draw_circle_filled(x, y, pellet_rad, arcade.color.ORANGE_PEEL)


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


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    global pac_grid, row_count, column_count, texture
    global pac_grid, row_count, column_count, tile_width, tile_height, pac_x,pac_y, score
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    # create the pacman grid
    for row in range(row_count):
        # open a list for the first row
        pac_grid.append([])
        for column in range(column_count):
            # if on the outside, make tile a wall
            if row == 0 or column == 0 or row == 14 or column == 30:
                pac_grid[row].append(0)
            # draw wall tiles from column to column
            elif (2 <= row <= 5 or row == 7 or 9 <= row <= 12) and column == 2:
                pac_grid[row].append(0)
            elif row == 7 and column == 3:
                pac_grid[row].append(0)
            elif (row == 2 or 4 <= row <= 5 or row == 7 or 9 <= row <= 10 or row == 12) and column == 4:
                pac_grid[row].append(0)
            elif (row == 2 or 9 <= row <= 10 or row == 12) and column == 5:
                pac_grid[row].append(0)
            elif (row == 2 or 4 <= row <= 5 or row == 7) and column == 6:
                pac_grid[row].append(0)
            elif (row == 2 or 4 <= row <= 5 or row == 7 or row == 9 or row == 12) and column == 7:
                pac_grid[row].append(0)
            elif (row == 7 or 11 <= row <= 12) and column == 8:
                pac_grid[row].append(0)
            elif (row == 1 or 3 <= row <= 5 or 10 <= row <= 11) and column == 9:
                pac_grid[row].append(0)
            elif (row == 7 or row == 10 or row == 13) and column == 10:
                pac_grid[row].append(0)
            elif (2 <= row <= 3 or 6 <= row <= 8 or row == 10) and column == 11:
                pac_grid[row].append(0)
            elif (row == 3 or 5 <= row <= 9 or row == 11 or row == 13) and column == 13:
                pac_grid[row].append(0)
            elif (2 <= row <= 3 or row == 5 or row == 9 or row == 11) and column == 14:
                pac_grid[row].append(0)
            elif (2 <= row <= 3 or row == 5 or row == 9 or 11 <= row <= 12) and column == 15:
                pac_grid[row].append(0)
            elif (row == 3 or row == 5 or row == 9 or 11 <= row <= 12) and column == 16:
                pac_grid[row].append(0)
            elif (row == 1 or row == 3 or 5 <= row <= 9 or row == 11) and column == 17:
                pac_grid[row].append(0)
            elif (row == 4 or 6 <= row <= 8 or 11 <= row <= 12) and column == 19:
                pac_grid[row].append(0)
            elif (row == 1 or row == 4 or row == 7) and column == 20:
                pac_grid[row].append(0)
            elif (3 <= row <= 4 or 9 <= row <= 10 or row == 13) and column == 21:
                pac_grid[row].append(0)
            elif (2 <= row <= 3 or row == 7) and column == 22:
                pac_grid[row].append(0)
            elif (row == 2 or row == 5 or row == 7 or 9 <= row <= 10 or row == 12) and column == 23:
                pac_grid[row].append(0)
            elif (row == 7 or 9 <= row <= 10 or row == 12) and column == 24:
                pac_grid[row].append(0)
            elif (row == 2 or 4 <= row <= 5 or row == 12) and column == 25:
                pac_grid[row].append(0)
            elif (row == 2 or 4 <= row <= 5 or row == 7 or 9 <= row <= 10 or row == 12) and column == 26:
                pac_grid[row].append(0)
            elif row == 7 and column == 27:
                pac_grid[row].append(0)
            elif (2 <= row <= 5 or row == 7 or 9 <= row <= 12) and column == 28:
                pac_grid[row].append(0)

            # if not a wall tile, pellet tile
            elif (1 <= column <= 29) and (1 <= row <= 13):
                pac_grid[row].append(1)

    # for row in range(row_count):
    #     for column in range(column_count):
    #         # calculate tile position
    #         tile_centre_x = (column + 1) * tile_width - 20
    #         tile_centre_y = (row + 1) * tile_height - 20
    #         # check if wall
    #         if pac_grid[row][column] == 0:
    #             draw_wall_tile(tile_centre_x, tile_centre_y)
    #         # check if pellet
    #         elif pac_grid[row][column] == 1:
    #             draw_pellet(tile_centre_x, tile_centre_y)
    texture = arcade.load_texture("pacific-blue-high-sheen-merola-tile-mosaic-tile-fyfl1spa-64_1000.jpg")

    arcade.run()


if __name__ == '__main__':
    setup()

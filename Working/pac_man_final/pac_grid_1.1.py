import arcade


WIDTH = 1240
HEIGHT = 600

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

def on_update(delta_time):
    pass


def on_draw():
    global pac_grid, row_count, column_count, tile_width, tile_height
    arcade.start_render()
    # draw out the current grid
    for row in range(8):
        for column in range(4):
            # calculate tile position
            tile_centre_x = (column+1)*tile_width - 20
            tile_centre_y = (row+1)*tile_height - 20
            # check if wall
            if pac_grid[row][column] == 0:
                draw_wall_tile(tile_centre_x, tile_centre_y)
            # check if pellet
            elif pac_grid[row][column] == 1:
                draw_pellet(tile_centre_x, tile_centre_y)


def draw_wall_tile(x, y):
    global tile_height, tile_width
    arcade.draw_rectangle_filled(x, y, tile_width, tile_height, arcade.color.BLUE)

def draw_pacman_open(x, y):
    global pac_rad, init_arc_angle, final_arc_angle
    arcade.draw_arc_filled(x, y, pac_rad, pac_rad, arcade.color.YELLOW, init_arc_angle, final_arc_angle)

def draw_pellet(x, y):
    global pellet_rad
    arcade.draw_circle_filled(x, y, pellet_rad, arcade.color.ORANGE_PEEL)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    global pac_grid, row_count, column_count
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
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
            if row == 0 or column == 0:
                pac_grid[row].append(0)
            # make a vertical wall
            elif (2 <= row <= 5) and column == 2:
                pac_grid[row].append(0)
            # make tile a pellet
            elif (column == 1 or column == 3) and 1 <= row <= 7:
                pac_grid[row].append(1)
            elif row == 1 and 1 <= column <= 9:
                pac_grid[row].append(1)
        print(pac_grid[row])

    arcade.run()

if __name__ == '__main__':
    setup()

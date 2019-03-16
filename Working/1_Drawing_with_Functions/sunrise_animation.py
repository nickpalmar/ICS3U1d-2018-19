import arcade

def sun(pos_x, pos_y, radius):
    arcade.draw_circle_filled(pos_x, pos_y, radius, arcade.color.SUNSET_ORANGE)


def grass():
    # draw the grass
    grass_x = 250
    grass_y = 100
    grass_width = 500
    grass_height = 200

    arcade.draw_rectangle_filled(grass_x, grass_y, grass_width, grass_height, arcade.color.DARK_GREEN)


def on_draw(delta_time):
    global sun_pos_x
    global sun_pos_y
    global sun_radius

    # start looping-draw
    arcade.start_render()

    # draw the sun and move it up
    sun(sun_pos_x, sun_pos_y, sun_radius)


    sun_pos_y += 0.1
    sun_radius *= 1.002

    # draw the grass
    grass()


sun_pos_x = 250
sun_pos_y = 100
sun_radius = 40



def main():

    # set screen width and height parameters and  create the screen + backgroud
    screen_width = 500
    screen_height = 500
    arcade.open_window(screen_width, screen_height, "Sunrise animation")
    arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)


    arcade.schedule(on_draw, 1/60)
    arcade.run()

# call main function to run all the code
main()



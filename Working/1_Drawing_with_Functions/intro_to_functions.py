import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_clouds():
    # cloud 1
    arcade.draw_circle_filled(30, 400, 30, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(50, 400, 30, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(40, 380, 40, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(100, 370, 40, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(95, 400, 30, arcade.color.WHITE_SMOKE)

    # cloud 2
    arcade.draw_circle_filled(320, 390, 30, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(340, 400, 30, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(370, 380, 40, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(400, 370, 40, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(410, 400, 30, arcade.color.WHITE_SMOKE)

def draw_rollinghill():
    # hill 1
    arcade.draw_ellipse_filled(100, 0, 200, 250, arcade.color.BRIGHT_GREEN)
    # hill 2
    arcade.draw_ellipse_filled(300, 0, 200, 200, arcade.color.BRIGHT_GREEN)
    # hill 3
    arcade.draw_ellipse_filled(500, 0, 300, 150, arcade.color.BRIGHT_GREEN)




def draw_tree():
    # tree trunk
    arcade.draw_lrtb_rectangle_filled(400, 450, 225, 125, arcade.color.BROWN)

    # tree leaves
    arcade.draw_ellipse_filled(415, 255, 30, 40, arcade.color.GREEN)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_clouds()
    draw_rollinghill()
    draw_tree()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_clouds(x, y):
    # cloud 1
    arcade.draw_circle_filled(x - 20, y, 30, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x, y, 30, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x - 10, y - 20, 40, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x + 50, y -30, 40, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x + 45, y, 30, arcade.color.WHITE_SMOKE)

def draw_rollinghill():
    # hill 1
    arcade.draw_ellipse_filled(100, 0, 200, 250, arcade.color.BRIGHT_GREEN)
    # hill 2
    arcade.draw_ellipse_filled(300, 0, 200, 200, arcade.color.BRIGHT_GREEN)
    # hill 3
    arcade.draw_ellipse_filled(500, 0, 300, 150, arcade.color.BRIGHT_GREEN)




def draw_tree(x, y):
    # tree trunk
    arcade.draw_lrtb_rectangle_filled(x, x + 50, y, y - 100, arcade.color.BROWN)

    # tree leaves
    arcade.draw_ellipse_filled(x + 10, y + 10, 45, 35, arcade.color.ANDROID_GREEN)
    arcade.draw_circle_filled(x + 50, y - 5, 40, arcade.color.ANDROID_GREEN)
    arcade.draw_circle_filled(x + 50, y + 45, 25, arcade.color.ANDROID_GREEN)




def on_draw(delta_time):
    global cloud1_x
    arcade.start_render()


    draw_rollinghill()
    draw_tree(120, 200)
    draw_tree(200, 200)
    draw_tree(300, 175)
    draw_tree(425, 150)
    draw_tree(500, 120)
    draw_tree(650, 120)



    draw_clouds(cloud1_x,  400)
    # draw_clouds(40, 500)
    # draw_clouds(200, 350)
    # draw_clouds(350, 375)
    # draw_clouds(550, 320)
    # draw_clouds(650, 300)
    # draw_clouds(700,400)
    # cloud1_x += 10

    if cloud1_x >= 0 and cloud1_x <= 600:
        cloud1_x += 10
    elif cloud1_x <= 600 and cloud1_x >= 0:
        cloud1_x -= 20




cloud1_x = 50

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()




# Call the main function to get the program started.

main()


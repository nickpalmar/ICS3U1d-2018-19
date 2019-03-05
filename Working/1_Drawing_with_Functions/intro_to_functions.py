import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_clouds(cloud_pos_x, cloud_pos_y):
    # cloud 1
    arcade.draw_circle_filled(cloud_pos_x - 20, cloud_pos_y, 30, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(cloud_pos_x, cloud_pos_y, 30, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(cloud_pos_x - 10, cloud_pos_y - 20, 40, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(cloud_pos_x + 50, cloud_pos_y -30, 40, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(cloud_pos_x + 45, cloud_pos_y, 30, arcade.color.WHITE_SMOKE)
    #
    # cloud_pos_x += 1
    # cloud_pos_y += 1

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
    arcade.draw_ellipse_filled(410, 255, 45, 35, arcade.color.ANDROID_GREEN)
    arcade.draw_circle_filled(450, 240, 40, arcade.color.ANDROID_GREEN)
    arcade.draw_circle_filled(450, 285, 25, arcade.color.ANDROID_GREEN)

#
# def draw_bird():
#     arcade.draw()



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # # call your draw functions
   #  global cloud_pos_x
   #  global cloud_pos_y
   #  cloud_pos_x = 50
   #  cloud_pos_y = 400
   #  draw_clouds(cloud_pos_x, cloud_pos_y)

    draw_rollinghill()
    draw_tree()


    # draw the moving bird
    # global bird_pos_x
    # global bird_pos_y
    #
    # bird_pos_x = 20
    # bird_pos_y = 500
    # draw_bird()

    cloud_pos_x = 50
    cloud_pos_y = 400
    draw_clouds(cloud_pos_x, cloud_pos_y)
    # while True:
    #     cloud_pos_x += 0.0001
    #     cloud_pos_y += 0.0001

    # Finish and run
    arcade.finish_render()
    arcade.run()





# Call the main function to get the program started.

main()


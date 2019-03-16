import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_clouds(x, y):
    # cloud 1
    arcade.draw_circle_filled(x - 20, y, 30, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x, y, 30, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x - 10, y - 20, 40, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x + 50, y - 30, 40, arcade.color.WHITE_SMOKE)
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
    global speed_x
    global cloud_width
    global cloud_y
    arcade.start_render()

    draw_rollinghill()
    draw_tree(120, 200)
    draw_tree(200, 200)
    draw_tree(300, 175)
    draw_tree(425, 150)
    draw_tree(500, 120)
    draw_tree(650, 120)

    draw_clouds(cloud1_x + 30, cloud_y)
    draw_clouds(cloud1_x, cloud_y - 100)
    draw_clouds(cloud1_x + 120, cloud_y + 155)

    if cloud1_x < (cloud_width // 2) or cloud1_x > (SCREEN_WIDTH - cloud_width // 2):
        cloud1_x = cloud_width
        cloud_y = random.randint(300, 500)

    cloud1_x += speed_x


cloud1_x = 50
speed_x = 10
cloud_width = 100
cloud_y = 400


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


# Call the main function to get the program started.

main()


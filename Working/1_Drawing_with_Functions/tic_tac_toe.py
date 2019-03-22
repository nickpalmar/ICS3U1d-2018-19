import arcade
from pyglet import *


# creat screen width and heigth values and box (on the board) width and height
screen_width = 500
screen_height = 500
half_box_width = screen_width // 6
half_box_height = screen_height // 6

def board(width, height):
    for x_value in range (0, width, screen_width//3):
        arcade.draw_line(x_value, 0, x_value, screen_height, arcade.color.BLACK)
    for y_value in range (0, height, screen_height//3):
        arcade.draw_line(0, y_value, screen_width, y_value, arcade.color.BLACK)

def draw_X(pos_x, pos_y):
    # draw first x symbol line
    arcade.draw_line(pos_x - half_box_width, pos_y + half_box_height, pos_x + half_box_width, pos_y - half_box_height, arcade.color.BLACK)
    # draw second x symbol line
    arcade.draw_line(pos_x + half_box_width, pos_y + half_box_height, pos_x - half_box_width, pos_y - half_box_height, arcade.color.BLACK)

def draw_O(pos_x, pos_y):
    # draw circle ellipse
    arcade.draw_circle_outline(pos_x, pos_y, half_box_width, arcade.color.BLACK)


# def on_mouse_press(mouse_x, mouse_y, button, modifiers):
#     print(mouse_x, mouse_y)


def on_draw(delta_time):
    # draw the 3x3 board
    board(screen_width, screen_height)

    # draw both player and cpu symbols
    draw_X(half_box_width, half_box_height*5)
    draw_O(half_box_width, half_box_height*5)

    # draw an X where the p
    def on_mouse_press(mouse_x, mouse_y, button, modifiers):
        print(mouse_x, mouse_y)

def main():
    # make screen and screen background
    arcade.open_window(screen_width, screen_height, "Tic-Tac-Toe")
    arcade.set_background_color(arcade.color.WHITE)

    # loop the on_draw function
    arcade.schedule(on_draw, 1/60)
    arcade.run()

# call the main to run the code
main()


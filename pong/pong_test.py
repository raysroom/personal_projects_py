import pytest
import pong
from pong import Paddle
from pong import Ball

# Width and Height of a sample screen
screen_width = 400
screen_height = 400

# Testing default parameters of objects used in pong
def main():
    test_ball_pos()
    test_paddle_pos()
    test_velocity()

def test_ball_pos():
    ball = Ball(screen_width // 2, screen_height // 4)

    assert(ball.x_pos) == 200
    assert(ball.y_pos) == 100

    ball2 = Ball(screen_width // 2, screen_height // 2, 10, 11)
    assert(ball2.width) == 10
    assert(ball2.height) == 11
    assert(ball.width) == 6

def test_paddle_pos():
    player = Paddle(10, 40)
    assert(player.x_pos) == 10

    player.x_pos = 20
    assert(player.x_pos) == 20

    assert(player.y_pos) == 40

def test_velocity():
    player = Paddle(10, 40)
    assert(player.velocity) == 10

    player.velocity = 20
    assert(player.velocity) == 20

    ball = Ball(0, 0)
    assert(ball.max_velocity) == 8


if __name__ == "__main__":
    main()
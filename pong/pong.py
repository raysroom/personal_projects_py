import pygame
from sys import exit
from random import randint

pygame.init()
screen_width = 800
screen_height = 600
Screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
framerate = 60
title_font = pygame.font.Font("font/8-BIT_WONDER.ttf", 30)
game_font = pygame.font.Font("font/BMSPA.ttf", 30)
game_font_small = pygame.font.Font("font/BMSPA.ttf", 20)
win_audio = pygame.mixer.Sound('sfx/win.mp3')
win_audio.set_volume(0.5)
win_score = 3


class Paddle:
    velocity = 10

    def __init__(self, x_pos, y_pos, width=10, height=80):
        self.x_pos = x_pos
        self.y_pos = self.y_start = y_pos
        self.width = width
        self.height = height

    def paddle_draw(self, screen):
        pygame.draw.rect(
            screen, "springgreen3", (self.x_pos, self.y_pos, self.width, self.height)
        )

    def move_paddle(self, up=True):
        if up:
            self.y_pos -= self.velocity
        else:
            self.y_pos += self.velocity

    def reset_paddle(self):
        self.y_pos = self.y_start


class Ball:
    max_velocity = 8

    def __init__(self, x_pos, y_pos, width=6, height=6):
        self.x_pos = self.x_start = x_pos
        self.y_pos = self.y_start = y_pos
        self.width = width
        self.height = height
        self.x_vel = self.max_velocity
        self.y_vel = 0

        self.hit_audio = pygame.mixer.Sound("sfx/hit.wav")
        self.hit_audio.set_volume(0.2)

        self.score_audio = pygame.mixer.Sound("sfx/score.wav")
        self.score_audio.set_volume(0.25)

    def ball_draw(self, screen):
        pygame.draw.rect(
            screen, "springgreen", (self.x_pos, self.y_pos, self.width, self.height)
        )

    def move_ball(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

    def reset_ball(self):
        self.x_pos = self.x_start
        self.y_pos = self.y_start
        self.y_vel = randint(-(self.max_velocity // 4), (self.max_velocity // 5))
        self.x_vel *= -1
        self.score_audio.play()

    def ball_hit(self):
        self.hit_audio.play()


def draw(screen, paddles, ball, p1_score, p2_score):
    screen.fill("grey10")
    middle_line = pygame.draw.rect(
        screen, "springgreen3", (screen_width // 2, 5, 2, 590)
    )

    p1_score_text = game_font.render(f"{p1_score}", False, "lightcyan2")
    p2_score_text = game_font.render(f"{p2_score}", False, "lightcyan2")
    screen.blit(p1_score_text, (screen_width // 6 * 2, screen_height // 2))
    screen.blit(p2_score_text, (screen_width // 6 * 4, screen_height // 2))

    for paddle in paddles:
        paddle.paddle_draw(screen)

    ball.ball_draw(screen)

    pygame.display.update()


def draw_menu(screen, p1_score, p2_score):
    screen.fill("grey10")
    game_name = title_font.render("Pong", False, "springgreen3")
    screen.blit(
        game_name,
        ((screen_width // 2) - (game_name.get_width() // 2), screen_height // 7),
    )

    game_start = game_font_small.render("Press 1 to play", False, "lightcyan2")
    game_start_2 = game_font_small.render("Press 2 to play together", False, "lightcyan2")
    game_start_controls = game_font_small.render("Controls - P1: W and S / P2: Up and Down", False, "lightcyan4")
    
    screen.blit(
        game_start,
        ((screen_width // 2) - (game_start.get_width() // 2), screen_height // 7 * 3),
    )
    screen.blit(
        game_start_2,
        ((screen_width // 2) - (game_start_2.get_width() // 2), screen_height // 7 * 4),
    )
    screen.blit(
        game_start_controls,
        ((screen_width // 2) - (game_start_controls.get_width() // 2), screen_height // 7 * 5)
    )

    if p1_score > 0 or p2_score > 0:
        if p1_score > p2_score:
            _winner = "Player 1 wins"
        elif p2_score > p1_score:
            _winner = "Player 2 wins"
        winner = game_font_small.render(
            f"{_winner} : {p1_score} - {p2_score}", False, "lightcyan2"
        )
        screen.blit(
            winner,
            ((screen_width // 2) - (winner.get_width() // 2), screen_height // 7 * 2),
        )
    pygame.display.update()


def player_movement(keys, player_1):
    if keys[pygame.K_s] and player_1.y_pos <= screen_height - player_1.height - 5:
        player_1.move_paddle(up=False)
    if keys[pygame.K_w] and player_1.y_pos >= 5:
        player_1.move_paddle(up=True)


def opponent_movement(keys, player_2):
    player_2.velocity = 10
    if keys[pygame.K_DOWN] and player_2.y_pos <= screen_height - player_2.height - 5:
        player_2.move_paddle(up=False)
    if keys[pygame.K_UP] and player_2.y_pos >= 5:
        player_2.move_paddle(up=True)

def ai_opponent(player_2, ball):
    player_2.velocity = 5
    if ball.y_pos > player_2.y_pos and player_2.y_pos < screen_height - player_2.height - 5:
        player_2.y_pos += player_2.velocity
    if ball.y_pos < player_2.y_pos and player_2.y_pos >= 5:
        player_2.y_pos -= player_2.velocity

def ball_collision(ball, player_1, player_2):
    if ball.y_pos <= 0 or ball.y_pos + ball.height >= screen_height:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if (
            ball.y_pos >= player_1.y_pos
            and ball.y_pos <= player_1.y_pos + player_1.height
        ):
            if ball.x_pos <= player_1.x_pos + player_1.width:
                ball.x_vel *= -1

                center = player_1.y_pos + player_1.height // 2
                center_offset = ball.y_pos - center
                offset_speed = (player_1.height // 2) // ball.max_velocity
                y_vel = center_offset // offset_speed

                ball.y_vel = y_vel
                ball.ball_hit()
    else:
        if (
            ball.y_pos >= player_2.y_pos
            and ball.y_pos <= player_2.y_pos + player_2.height
        ):
            if ball.x_pos + ball.width >= player_2.x_pos:
                ball.x_vel *= -1

                center = player_2.y_pos + player_2.height / 2
                center_offset = ball.y_pos - center
                offset_speed = (player_2.height / 2) / ball.max_velocity
                y_vel = center_offset / offset_speed

                ball.y_vel = y_vel
                ball.ball_hit()

def main():
    run = True

    player_1 = Paddle(10, screen_height // 2 - 80 // 2)
    player_2 = Paddle(screen_width - 20, screen_height // 2 - 80 // 2)
    ball = Ball(screen_width // 2, screen_height // 2)

    p1_score = 0
    p2_score = 0

    game_active = False
    two_player = False

    while run:
        clock.tick(framerate)
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                exit()
            if game_active == False:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    game_active = True
                    p1_score = 0
                    p2_score = 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    two_player = True
                    game_active = True
                    p1_score = 0
                    p2_score = 0


        if game_active == True:
            
            draw(Screen, [player_1, player_2], ball, p1_score, p2_score)

            keys = pygame.key.get_pressed()
            player_movement(keys, player_1)
            if two_player:
                opponent_movement(keys, player_2)
            else:
                ai_opponent(player_2, ball)
            ball.move_ball()
            ball_collision(ball, player_1, player_2)

            if ball.x_pos > screen_width - 5:
                p1_score += 1
                ball.reset_ball()
            elif ball.x_pos < 5:
                p2_score += 1
                ball.reset_ball()

            winner = False
            if p1_score >= win_score:
                winner = True
            if p2_score >= win_score:
                winner = True

            if winner:
                game_active = False
                player_1.reset_paddle()
                player_2.reset_paddle()
                win_audio.play()
                if two_player:
                    two_player = False


        else:
            draw_menu(Screen, p1_score, p2_score)
            


if __name__ == "__main__":
    main()
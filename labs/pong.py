# Alisha Agrawal (aa3se)

import pygame
import gamebox
camera = gamebox.Camera(800,600)

p_width = 10
p_height = 80
ball_velocity = 15
player_speed = 14
p1_score = 0
p2_score = 0
game_on = False

ticker = 0

walls = [
    gamebox.from_color(400, 600, "green", 1000, 20),
    gamebox.from_color(400, 0, "green", 1000, 20),
]

p1 = gamebox.from_color(20, 400, "red", 15, 100)
p2 = gamebox.from_color(780, 400, "yellow", 15, 100)
ball = gamebox.from_color(400,300, "green", 20, 20)

ball.xspeed = ball_velocity
ball.yspeed = ball_velocity

def tick(keys):

    global game_on
    global p1_score
    global p2_score

    # --- BALL MOVEMENT ---
    if game_on:
        ball.move_speed()

    # ------- INPUT ---------
    if pygame.K_SPACE in keys:
        game_on = True
    if pygame.K_w in keys:
        p1.y -= player_speed
    if pygame.K_s in keys:
        p1.y += player_speed
    if pygame.K_UP in keys:
        p2.y -= player_speed
    if pygame.K_DOWN in keys:
        p2.y += player_speed

    # ----- COLLISION DETECTION -----
    if ball.bottom_touches(walls[0]):
        ball.move_both_to_stop_overlapping(walls[0])
        ball.yspeed -= ball_velocity
    if ball.top_touches(walls[1]):
        ball.move_both_to_stop_overlapping(walls[1])
        ball.yspeed += ball_velocity
    if ball.right_touches(p1):
        ball.move_both_to_stop_overlapping(p1)
        ball.xspeed += ball_velocity
    if ball.left_touches(p2):
        ball.move_both_to_stop_overlapping(p2)
        ball.xspeed -= ball_velocity


    # ----- SCORING ------
    if ball.left > camera.right:
        p1_score += 1
        ball.x = 400
        ball.y = 300
        game_on = False
    if ball.right < camera.left:
        p2_score += 1
        ball.x = 400
        ball.y = 300
        game_on = False


    # ----- DRAW METHODS --------
    # We have provided all of the draw methods for you.
    # You do not need to add anything here.
    camera.clear("black")
    camera.draw(gamebox.from_text(300, 50, str(p1_score), 50, "Red", bold=True))
    camera.draw(gamebox.from_text(500, 50, str(p2_score), 50, "Yellow", bold=True))

    # Draw all the walls
    for wall in walls:
        camera.draw(wall)

    # Draw the player paddles and the ball
    camera.draw(p1)
    camera.draw(p2)
    camera.draw(ball)

    # ---- CHECKING FOR WIN ----
    if p1_score >= 10:
        camera.draw(gamebox.from_text(400, 100, "Red Wins!", 40, "Red", bold=False))
        gamebox.pause()
    if p2_score >= 10:
        camera.draw(gamebox.from_text(400, 100, "Yellow Wins!", 40, "Yellow", bold=False))
        gamebox.pause()
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
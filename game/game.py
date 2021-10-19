# Alisha Agrawal (aa3se)
"""
TRAINING WITH KIRBY
a single-player, side-scrolling 2D platform game where an
Animated Kirby must reach the end of his training.

REQUIREMENTS:
    1. user input
    2. graphics/images
    3. start screen
    4. small enough window

OPTIONAL:
    1. Animation
        a. Kirby
        b. Bricks
        c. Piccolo
    2. Enemies
        - Bricks -> move
    3. Collectibles
        - Stars -> add points and health
    4. Scrolling Level
        - game scrolls infinitely until certain conditions are met
            - conditions: 250 points and 10 bricks
    5. Health Bar
        - graphical
        - decreases and increases
        - health = 0 -> game over
"""

import pygame
import gamebox

#      ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
# ｡･:*:･ﾟ★,｡･:*:･ﾟ☆　VARIABLES ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
#      ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆

camera = gamebox.Camera(800, 600)
gravity = 7  # adds downward pull after jump
scroll_speed = 15  # allows for game to scroll infinitely
no_win = True  # whether or not the user has won
gamer_points = 0  # number of points the user has generated
health = 100  # starting health
time = 0  # starting time
game_on = False  # whether or not the game is on
first_game = True  # whether or not it is the first game
brick_count = 0  # number of bricks user has collected


#     ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
# ｡･:*:･ﾟ★,｡･:*:･ﾟ☆　SETUP　 ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
#     ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆


def setup():
    """
    contains all beginning positions of variables
    so that when a game restarts these variables
    will be placed at their beginning positions.
    """
    global gamer_points, health, time, brick_count
    camera.x = 0
    for stage in kirby_ani:
        stage.x = 100
    for brick in bricks_ani:
        brick.x = camera.x + 300
    for brick2 in bricks2_ani:
        brick2.x = camera.x + 450
    for new_star in stars:
        new_star.x = camera.x + 500
    gamer_points = 0
    health = 100
    time = 0
    brick_count = 0


#       ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
# ｡･:*:･ﾟ★,｡･:*:･ﾟ☆　START SCREEN　 ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
#       ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆


def draw_start_screen():
    """
    camera draws the start screen onto the screen
    """
    start_bg = gamebox.from_image(400, 800, "screenstart.png")
    start_bg.scale_by(0.5)
    start_bg.bottom = camera.bottom
    camera.draw(start_bg)


#       ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
# ｡･:*:･ﾟ★,｡･:*:･ﾟ☆　BACKGROUND　 ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
#       ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆

platform = gamebox.from_color(0, 555, "dark gray", 7000, 100)
background = gamebox.from_image(0, 0, "bg.jpg")


# IMAGE SOURCE: Gravit Designer: 2D Game Background


def draw_bg():
    """
    camera draws platform and background image
    and makes it so
    both platform and background are infinitely scrolling
    """
    platform.bottom = camera.bottom
    platform.right = camera.right
    background.bottom = camera.bottom
    background.right = camera.right
    camera.draw(background)
    camera.draw(platform)


#    ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
# ｡･:*:･ﾟ★,｡･:*:･ﾟ☆　HEALTH ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
#    ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆

one_bar = gamebox.from_image(500, 100, "01.png")
one_bar.scale_by(.20)
two_bars = gamebox.from_image(500, 100, "02.png")
two_bars.scale_by(.20)
three_bars = gamebox.from_image(500, 100, "03.png")
three_bars.scale_by(.20)
four_bars = gamebox.from_image(500, 100, "04.png")
four_bars.scale_by(.20)
five_bars = gamebox.from_image(500, 100, "05.png")
five_bars.scale_by(.20)
six_bars = gamebox.from_image(500, 100, "06.png")
six_bars.scale_by(.20)


# IMAGE SOURCE: Pixilart, Health Bar Sprite Sheet by Anonymous


def draw_healthbar():
    """
    camera draws certain points in the health bar
    depending on the amount of health Kirby has
    """
    if health <= 10:
        one_bar.x = camera.left + 700
        low_health = gamebox.from_text(0, 300, "YOUR HEALTH IS LOW", 36, "black")
        low_health.x = camera.left + 400
        camera.draw(one_bar)
        camera.draw(low_health)
    elif health <= 25:
        two_bars.x = camera.left + 700
        camera.draw(two_bars)
    elif health <= 50:
        three_bars.x = camera.left + 700
        camera.draw(three_bars)
    elif health <= 70:
        four_bars.x = camera.left + 700
        camera.draw(four_bars)
    elif health <= 90:
        five_bars.x = camera.left + 700
        camera.draw(five_bars)
    elif health <= 100:
        six_bars.x = camera.left + 700
        camera.draw(six_bars)


#    ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
# ｡･:*:･ﾟ★,｡･:*:･ﾟ☆　KIRBY ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
#    ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆

kirby = gamebox.load_sprite_sheet('kirby.png', 1, 5)
# SPRITE SOURCE: Sonicjeremy on DeviantArt

# ANIMATES KIRBY
kirby_ani = []
for image in kirby:
    k_stage = gamebox.from_image(0, 0, image)
    k_stage.scale_by(1.75)
    k_stage.bottom = platform.top
    k_stage.left = camera.left + 150
    kirby_ani.append(k_stage)


def draw_kirby(keys):
    """
    controls the animated kirby character using the parameter keys
    changes points and health according to how kirby interacts with
    stars and enemies (bricks)
    camera draws kirby on screen
    """
    global gamer_points, health, game_on, brick_count
    for kirby_stage in kirby_ani:
        kirby_stage.bottom = platform.top
        # CONTROLS
        if pygame.K_RIGHT in keys and kirby_stage.bottom_touches(platform):
            kirby_stage.x += 50
        if pygame.K_LEFT in keys and kirby_stage.bottom_touches(platform):
            kirby_stage.x -= 50
        if pygame.K_SPACE in keys and kirby_stage.bottom_touches(platform):
            kirby_stage.y -= 120
        kirby_stage.speedy += gravity
        kirby_stage.move_speed()
        kirby_stage.move_to_stop_overlapping(platform)
        # KIRBY TOUCHES STAR -> +15 POINTS +5 HEALTH
        for star_image in stars:
            if kirby_stage.touches(star_image):
                gamer_points += 5
                if health + 5 >= 100:
                    health = 100
                else:
                    health += 5
                star_image.x -= 1000
            for brick in bricks_ani:
                star_image.move_to_stop_overlapping(brick)
            for brick2 in bricks2_ani:
                star_image.move_to_stop_overlapping(brick2)
        for brick in bricks_ani:
            # KIRBY JUMPS BRICK  -> +15 POINTS
            if kirby_stage.bottom_touches(brick):
                gamer_points += 5
                brick_count += 1
                brick.x -= 1000
            # KIRBY TOUCHES BRICK -> -15 POINTS -15 HEALTH
            elif kirby_stage.touches(brick):
                if gamer_points - 5 <= 0:
                    gamer_points = 0
                else:
                    gamer_points -= 5
                health -= 5
                brick.x -= 1000
        for brick2 in bricks2_ani:
            # KIRBY JUMPS RED RED BRICK -> +30 POINTS
            if kirby_stage.bottom_touches(brick2):
                gamer_points += 10
                brick_count += 1
                brick2.x -= 1000
            # KIRBY TOUCHES RED BRICK -> -60 POINTS -30 HEALTH
            elif kirby_stage.touches(brick2):
                if gamer_points - 20 <= 0:
                    gamer_points = 0
                else:
                    gamer_points -= 20
                health -= 10
                brick2.x -= 1000
    camera.draw(kirby_ani[time % len(kirby_ani)])


#    ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
# ｡･:*:･ﾟ★,｡･:*:･ﾟ☆　STARS ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
#    ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆

stars = [gamebox.from_image(500, 0, 'star.png'),
         gamebox.from_image(1200, 0, 'star.png'),
         gamebox.from_image(1550, 0, 'star.png')]
# IMAGE SOURCE: Warp Star | Kirby Wiki | Fandom

for star in stars:
    star.scale_by(0.15)


def draw_stars():
    """
    makes stars appear "randomly" on screen
    camera draws stars on screen
    :return:
    """
    for star_image in stars:
        star_image.bottom = platform.top
        if star_image.right < camera.left:
            star_image.left = camera.right + 600
        camera.draw(star_image)


#      ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
# ｡･:*:･ﾟ★,｡･:*:･ﾟ☆　ENEMIES　 ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
#      ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆

bricks = gamebox.load_sprite_sheet('brick.png', 1, 3)
bricks2 = gamebox.load_sprite_sheet('redbrick.png', 1, 3)
# SPRITE SOURCE: Jesse's Custom Enemy Sprites P.2 | Pixel Art Maker

# BRICK ANIMATION
bricks_ani = []
for image in bricks:
    b_stage = gamebox.from_image(0, 0, image)
    b_stage.scale_by(0.55)
    b_stage.bottom = platform.top
    b_stage.left = camera.left + 600
    bricks_ani.append(b_stage)

# RED BRICK ANIMATION
bricks2_ani = []
for image in bricks2:
    b2_stage = gamebox.from_image(0, 0, image)
    b2_stage.scale_by(0.55)
    b2_stage.bottom = platform.top
    b2_stage.left = camera.left + 400
    bricks2_ani.append(b2_stage)


def draw_bricks():
    """
    makes animated enemies appear "randomly" on screen
    camera draws enemies on screen
    """
    for brick in bricks_ani:
        if brick.right < camera.left:
            brick.left = camera.right + 300
    camera.draw(bricks_ani[time % len(bricks_ani)])


def draw_bricks2():
    for brick2 in bricks2_ani:
        if brick2.right < camera.left:
            brick2.left = camera.right + 600
    camera.draw(bricks2_ani[time % len(bricks2_ani)])


#      ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
# ｡･:*:･ﾟ★,｡･:*:･ﾟ☆　PICCOLO　 ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
#      ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆

piccolo = gamebox.load_sprite_sheet('piccolo.png', 1, 8)
# SPRITE SOURCE: Fusion Dance Sprites by Thejunior142 on DeviantArt

# PICCOLO ANIMATION
piccolo_ani = []
for image in piccolo:
    p_stage = gamebox.from_image(0, 0, image)
    p_stage.scale_by(2)
    p_stage.bottom = platform.top
    piccolo_ani.append(p_stage)


def draw_piccolo():
    """
    camera draws piccolo onto the screen
    """
    for piccolo_stage in piccolo_ani:
        piccolo_stage.x = camera.left + 600
    camera.draw(piccolo_ani[time % len(piccolo_ani)])


#    ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
# ｡･:*:･ﾟ★,｡･:*:･ﾟ☆　TICK ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
#    ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆


def tick(keys):
    """
    all the drawing is done here for the game to occur
    """
    global first_game, game_on, gamer_points, health, time, no_win, scroll_speed, brick_count
    camera.clear('white')
    # FIRST GAME
    if first_game:
        draw_start_screen()
        # START GAME
        if pygame.K_SPACE in keys:
            game_on = True
            first_game = False
    else:
        draw_bg()
        draw_stars()
        draw_bricks()
        draw_bricks2()
        # TOTAL POINTS DISPLAY
        points = gamebox.from_text(80, 75, "TOTAL POINTS: " + str(gamer_points), 25, 'black')
        points.x = camera.left + 100
        # HEALTH BAR COUNT DISPLAY
        health_bar = gamebox.from_text(75, 75, "HEALTH: " + str(health), 25, 'black')
        health_bar.x = camera.left + 725
        # BRICK COUNT DISPLAY
        brick_count_text = gamebox.from_text(75, 100, "BRICK COUNT: " + str(brick_count // 3), 25, 'black')
        brick_count_text.x = camera.left + 100
        # USER HAS NOT WON
        if game_on and no_win:
            camera.x += scroll_speed
            time += 1
            # TIME DISPLAY
            time_passed = gamebox.from_text(90, 50, "TIME: " + str(time // 30), 25, 'black')
            time_passed.x = camera.left + 115
            camera.draw(health_bar)
            camera.draw(time_passed)
            camera.draw(brick_count_text)
            camera.draw(points)
            draw_kirby(keys)
            draw_healthbar()
            # KIRBY HEALTH DEPLETES -> GAME OVER
            if health <= 0:
                game_on = False
            for kirby_s in kirby_ani:
                # KIRBY MEETS PICCOLO -> GAME WIN
                for part in piccolo_ani:
                    if kirby_s.touches(part):
                        no_win = False
                # KIRBY OFF SCREEN -> GAME OVER
                if kirby_s.right <= camera.left or kirby_s.left >= camera.right:
                    game_on = False
            # ADD PICCOLO ON SCREEN IF CONDITIONS ARE MET
            if gamer_points >= 250 and brick_count >= 10:
                meet_piccolo = gamebox.from_text(0, 200, "GO MEET PICCOLO!", 50, 'black', True)
                meet_piccolo.x = camera.left + 400
                camera.draw(meet_piccolo)
                draw_piccolo()
        # USER HAS WON
        if not no_win:
            you_win = gamebox.from_text(0, 200, "YOU WON!", 40, 'black', True)
            you_win2 = gamebox.from_text(0, 400, "press space bar to play again", 40, 'black')
            you_win.x += camera.left + 400
            you_win2.x += camera.left + 400
            camera.draw(you_win)
            camera.draw(you_win2)
            # USER PLAYS AGAIN
            if pygame.K_SPACE in keys:
                setup()
                no_win = True
        # USER HAS LOST
        if not game_on:
            game_over = gamebox.from_text(0, 200, "GAME OVER:", 40, 'black', True)
            game_over2 = gamebox.from_text(0, 400, "press space bar to play again", 40, 'black')
            game_over.x += camera.left + 400
            game_over2.x += camera.left + 400
            camera.draw(game_over)
            camera.draw(game_over2)
            # USER PLAYS AGAIN
            if pygame.K_SPACE in keys:
                setup()
                game_on = True
    camera.display()


gamebox.timer_loop(30, tick)

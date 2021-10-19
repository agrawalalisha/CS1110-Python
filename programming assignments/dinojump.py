# Alisha Agrawal (aa3se)
"""
simplified version of google chrome 'there's no internet'
dinosaur jumping game
"""
import pygame
import gamebox

camera = gamebox.Camera(800, 600)
gravity = 4
scroll_speed = 20
points = 0
game_on = True


def setup():
    """
    resets all moving gameboxes to their original positions when game is restarted
    """
    global dinosaur, cactus1, cactus2, cactus3, cloud1, cloud2, cloud3, points
    dinosaur.x = 100
    cactus1.x = 600
    cactus2.x = 900
    cactus3.x = 1200
    cloud1.x = 100
    cloud2.x = 300
    cloud3.x = 500
    points = 0


# dinosaur

dinosaur = gamebox.from_color(100, 400, 'gray', 35, 55)


def dinosaur_jump(keys):
    """
    controls dinosaur; if space key is entered the dinosaur jumps
    :param keys:
    :return:
    """
    if pygame.K_SPACE in keys and dinosaur.bottom_touches(ground):
        dinosaur.speedy = -30
    dinosaur.speedy += gravity
    dinosaur.move_speed()
    dinosaur.left = camera.left + 100
    camera.draw(dinosaur)


# scrolling background

ground = gamebox.from_color(0, 0, 'tan', 5000, 75)
ground.bottom = camera.bottom


def draw_scenery():
    """
    keeps game going on continuously -> scroll
    places ground and allows cacti and clouds to continuously appear
    """
    ground.right = camera.right
    if cactus1.right < camera.left:
        cactus1.left = cactus2.right + 800
    if cactus2.right < camera.left:
        cactus2.left = cactus3.right + 900
    if cactus3.right < camera.left:
        cactus3.left = cactus1.right + 850
    if cloud1.right < camera.left:
        cloud1.left = cloud2.right + 400
    if cloud2.right < camera.left:
        cloud2.left = cloud3.right + 600
    if cloud3.right < camera.left:
        cloud3.left = cloud1.right + 800
    camera.draw(ground)
    draw_cacti()
    draw_clouds()


# cacti

cactus1 = gamebox.from_color(600, 0, 'dark green', 20, 40)
cactus2 = gamebox.from_color(900, 0, 'dark green', 40, 30)
cactus3 = gamebox.from_color(1200, 0, 'dark green', 30, 45)
cacti = [cactus1, cactus2, cactus3]


def draw_cacti():
    """
    adds all cacti into the game
    """
    for cactus in cacti:
        cactus.bottom = ground.top
        camera.draw(cactus)


# clouds
cloud1 = gamebox.from_color(100, 100, 'light gray', 200, 100)
cloud2 = gamebox.from_color(300, 100, 'light gray', 100, 80)
cloud3 = gamebox.from_color(500, 100, 'light gray', 150, 100)
clouds = [cloud1, cloud2, cloud3]


def draw_clouds():
    """
    adds all clouds into the game
    """
    for cloud in clouds:
        camera.draw(cloud)


def tick(keys):
    """
    does the drawing for the game to occur
    """
    global points
    global game_on
    camera.clear('white')
    draw_scenery()
    dinosaur.move_to_stop_overlapping(ground)
    points_gained = gamebox.from_text(75, 50, str(points), 36, 'black')
    points_gained.x = camera.left + 75
    camera.draw(points_gained)
    if game_on:
        camera.x += scroll_speed
        dinosaur_jump(keys)
        points += 1
        for cactus in cacti:
            if dinosaur.touches(cactus):
                game_on = False
    if not game_on:
        if pygame.K_SPACE in keys:
            camera.x = 0
            setup()
            game_on = True
    camera.display()


gamebox.timer_loop(30, tick)  # invokes the tick function 30 times per second

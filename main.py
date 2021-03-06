"""
Title: The Adventures of Anatole
Creators: Eric
Description:
"""

#Anatole and Camera Stuff and spawn
anatole = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . 7 7 7 7 7 7 7 . . . . .
    . . . 7 7 7 7 7 7 7 7 7 . . . .
    . . . 7 7 7 7 7 7 7 7 7 . . . .
    . . 7 7 7 7 7 7 7 7 7 7 7 . . .
    . . . d d f d d d f d d . . . .
    . . . . d d d d d d d . . . . .
    . . . . . . d d d . . . . . . .
    . . . . . . d d d . . . . . . .
    . 2 2 5 5 2 2 2 2 2 5 5 2 2 . .
    . 2 2 2 2 2 2 5 2 2 2 2 2 2 . .
    . d d 2 2 2 2 2 2 2 2 2 d d . .
    . d d 2 2 2 2 5 2 2 2 2 d d . .
    . d . 2 2 2 2 2 2 2 2 2 . d . .
    . . . . e e . . . e e . . . . .
    . . . e e e . . . e e e . . . .
"""), SpriteKind.player)
scene.camera_follow_sprite(anatole)


#anatole shooty shoot 
def on_event_pressed():
  projectile = sprites.create_projectile_from_sprite(img("""
      . . . . . . . . . . . . . . . .
      . . . . . . . . . . . . . . . .
      . . . . . . . . . . . . . . . .
      . . . . . . . . . . . . . . . .
      . . . . . . . . . . . . . . . .
      . . . . . . . . . . . . . . . .
      . . . . . . . . . . . . . . . .
      . . . . . . . . . . . . . . . .
      . . . . . . . 5 5 5 . . 5 5 . .
      . . . . 5 5 5 5 5 5 5 5 5 5 5 .
      . . . . 5 5 5 5 . . 5 5 5 5 . .
      . . . . . . . . . . . . . . . .
      . . . . . . . . . . . . . . . .
      . . . . . . . . . . . . . . . .
      . . . . . . . . . . . . . . . .
      . . . . . . . . . . . . . . . .
  """), anatole, 99999, 0)  
controller.B.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)


# Double Jump Function & Movement
controller.move_sprite(anatole, 100,0)
can_double_jump = True
def jump():
    global can_double_jump
    if can_double_jump:
     anatole.vy = -100
    can_double_jump = anatole.is_hitting_tile(CollisionDirection.BOTTOM)
controller.A.on_event(ControllerButtonEvent.PRESSED, jump)

def on_update():
    global can_double_jump
    if anatole.is_hitting_tile(CollisionDirection.BOTTOM):
        can_double_jump = True
game.on_update(on_update)
anatole.ay = 200

#Health Function (DO NOT CHANGE THE NUMBERS, HIGHER THAN 1 TENDS TO CAUSE ISSUES WITH SPAWNING, SO HE JUST DIES ON IMPACT NOW LOL.)
info.set_life(2)

#Lava Obstacle
scene.set_tile(2, img("""
    5 5 5 5 4 4 2 2 2 2 2 2 4 4 4 5
    4 4 4 5 5 4 4 2 2 2 2 2 4 5 5 5
    2 2 4 4 5 5 4 4 4 4 4 4 4 5 4 4
    4 4 2 4 4 5 5 4 5 5 5 5 5 5 4 2
    4 4 2 2 4 5 5 5 5 5 5 5 4 4 4 2
    4 4 2 4 5 5 5 5 5 4 4 4 4 2 2 4
    2 2 2 4 4 5 5 5 5 4 2 2 2 2 4 4
    4 4 2 2 4 4 5 5 5 4 2 2 2 4 4 4
    5 4 4 2 2 4 5 5 5 4 2 2 2 4 4 4
    5 5 4 4 2 4 4 5 5 4 2 2 2 2 4 4
    5 5 5 4 4 4 5 5 5 4 4 2 2 2 2 2
    2 5 5 2 5 5 5 5 5 5 4 4 4 2 2 2
    2 5 5 5 5 5 5 2 5 5 5 5 4 4 4 4
    2 5 5 5 2 2 2 2 2 2 5 5 5 5 5 5
    5 5 5 2 2 4 4 4 4 4 2 5 5 5 5 5
    5 5 2 2 4 4 4 4 4 4 4 2 2 5 5 5
"""), True)
def on_hit_tile(sprite):
    sprite.set_position(sprite.x-100, sprite.y)
    info.player1.change_life_by(-1)
scene.on_hit_tile(SpriteKind.player, 2, on_hit_tile)


#THIS IS STUFF WITH TILEMAP, DON'T TOUCH, IT WORKS AND I WOULD LIKE TO KEEP IT LIKE THAT.

# actual map
scene.set_tile_map(img("""
    333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    333........................................................................................................................................................................................................................................................................................................3
    333........................................................................................................................................................................................................................................................................................................3
    333........................................................................................................................................................................................................................................................................................................3
    333........................................................................................................................................................................................................................................................................................................3
    333........................................................................................................................................................................................................................................................................................................3
    333........................................................................................................................................................................................................................................................................................................3
    333........................................................................................................................................................................................................................................................................................................3
    333........................................................................................................................................................................................................................................................................................................3
    333........................................................................................................................................................................................................................................................................................................3
    333........................................................................................................................................................................................................................................................................................................3
    333........................................................................................................................................................................................................................................................................................................3
    333........................................................................................................................................................................................................................................................................................................3
    333.....................................5..................................................................................................................................................................................................................................................................3
    333...................................5.4.5................................................................................................................................................................................................................................................................3
    333.................................5.4.4.4.5..............................................................................................................................................................................................................................................................3
    333...............................5.4.4.4.4.4.5...............5............................................................................................................................................................................................................................................3
    333.............................5.4.4.4.4.4.4.4.5...........5.4.5..........................................................................................................................................................................................................................................3
    333...........................5.4.4.4.4.4.4.4.4.4.5.......5.4.4.4..........................................................................................................................................................................................................................................3
    333.........................5.4.4.4.4.4.4.4.4.4.4.4.5...5.4.4.4.4.............333333333............................................33333333..................................................................................................................................5.............................3
    33333333333333333333333333..4.4.4.4.4.4.4.4.4.4.4.4.4.5.4.4.4.4.4.333333..336.333333333...........................................3366633666.................................................................................................................................4.............................3
    33333333333333333333333333..4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.333333..666.663333366................5..5..5..5..5..5.33333333..............33333333333................................................................................................................5...4...5.........................3
    333333333333333333333333332222222222222222222222222222222222222222333333...6...6666666....63333333336..4..4..4..4..4..4.3333333322222222222222333333333333...............................................................................................................4...4...4.....................9...3
    333333333333333333333333332222222222222222222222222222222222222222333333...................633333336...4..4..4..4..4..4.33333333222222222222223333333333333...........................................................................................................5..4...4...4...5.................7...3
    333333333333333333333333332222222222222222222222222222222222222222333333....................6633336....4..4..4..4..4..4.333333332222222222222233333333333333...........................................................5..............................................4..4...4...4...4.................7...3
    333333333333333333333333332222222222222222222222222222222222222222333333......................6336.....4..4..4..4..4..4.3333333322222222222222333333333333333.....................5....................................4............................................5.4..4...4...4...4.................7...3
    333333333333333333333333332222222222222222222222222222222222222222333333.......................66......4..4..4..4..4..4.33333333222222222222223333333333333333.................5..4....5....5.......................5..4............................................4.4..4...4...4...4....5............7...3
    333333333333333333333333332222222222222222222222222222222222222222333333...............................4..4..4..4..4..4.333333333333333333333333333333333333333................4..4..5.4..5.4.....5.................4..4..5.5.5.5.5.5.5.5.5.5.5.5.5.......5.......5.4.4..4...4...4...4....4............8...3
    333333333333333333333333332222222222222222222222222222222222222222333333...............................4..4..4..4..4..4.33333333333333333333333333333333333333333333333333333..4..4..4.4..4.4.5.5.4..3333333333333..4..4..4.4.4.4.4.4.4.4.4.4.4.4.4.......4.......4.4.4..4...4...4...4....4....3333333333333
    333333333333333333333333332222222222222222222222222222222222222222333333...............................4..4..4..4..4..4.33333333333333333333333333333333333333333333333333333..4..4..4.4..4.4.4.4.4..3333333333333..4..4..4.4.4.4.4.4.4.4.4.4.4.4.4.......4.......4.4.4..4...4...4...4....4....3333333333333
    333333333333333333333333332222222222222222222222222222222222222222333333...............................4..4..4..4..4..4.333333333333333333333333333333333333333333333333333332222222222222222222222223333333333333222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333
    333333333333333333333333333333333333333333333333333333333333333333333333...............................4..4..4..4..4..4.333333333333333333333333333333333333333333333333333332222222222222222222222223333333333333222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333
    333333333333333333333333333333333333333333333333333333333333333333333333222222222222222222222222222222222222222222222222333333333333333333333333333333333333333333333333333332222222222222222222222223333333333333222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333
    333333333333333333333333333333333333333333333333333333333333333333333333222222222222222222222222222222222222222222222222333333333333333333333333333333333333333333333333333332222222222222222222222223333333333333222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333
"""))
#standard brick
scene.set_tile(3, img("""
    f f f f f f f f f f f f f f f f
    f e f f f 4 4 4 4 4 4 4 4 4 4 f
    f e e e f f f f 4 4 4 4 4 4 f f
    f e e e e e e e f f 4 f f f f f
    f e e e e e e e e e f f e e e f
    f e e e e e e e e e f e e e e f
    f e e e e e e e e f e e e e e f
    f e e e e e e e e f e e e e e f
    f e e e e e e e f f e e e e e f
    f e e e e e e e f 4 f e e e e f
    f e e e e e e f 4 4 4 f e e e f
    f e e e e e f 4 4 4 4 4 f f e f
    f f f f f f f 4 4 4 4 4 4 4 f f
    f 4 4 f f f 4 4 4 4 4 4 4 4 4 f
    f 4 4 4 4 f f f 4 4 4 4 4 4 4 f
    f f f f f f f f f f f f f f f f
"""), True)
#supposed "spawn block" (WIP)
scene.set_tile(15, img("""
    f f f f f f f f f f f f f f f f
    f e f f f 4 4 4 4 4 4 4 4 4 4 f
    f e e e f f f f 4 4 4 4 4 4 f f
    f e e e e e e e f f 4 f f f f f
    f e e e e e e e e e f f e e e f
    f e e e e e e e e e f e e e e f
    f e e e e e e e e f e e e e e f
    f e e e e e e e e f e e e e e f
    f e e e e e e e f f e e e e e f
    f e e e e e e e f 4 f e e e e f
    f e e e e e e f 4 4 4 f e e e f
    f e e e e e f 4 4 4 4 4 f f e f
    f f f f f f f 4 4 4 4 4 4 4 f f
    f 4 4 f f f 4 4 4 4 4 4 4 4 4 f
    f 4 4 4 4 f f f 4 4 4 4 4 4 4 f
    f f f f f f f f f f f f f f f f
"""), True)
#metal pole stuff
scene.set_tile(4, img("""
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
"""), True)
#top of metal pole 
scene.set_tile(5, img("""
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
"""), True)
#mossy stuff hanging off brick(?)
scene.set_tile(6, img("""
    f f f f f f f f f f f f f f f f
    f e f f f 4 4 4 4 4 4 7 4 4 4 f
    f e 7 e f f f f 4 4 4 7 4 4 f f
    f e 7 e e e e e f f 7 7 f f f f
    f e 7 7 e e e e e 7 7 7 e e e f
    f e e 7 e e e 7 7 7 f 7 7 e e f
    f e e 7 7 e 7 7 e f e e 7 e e f
    f e e e 7 e 7 e e f e e 7 e e f
    f f f e 7 7 7 e f f e e 7 7 e f
    7 . f f f 7 f f f 4 f 7 e 7 e f
    . 7 . . 7 7 . f f f f 7 e 7 7 f
    7 7 . 7 7 7 7 7 . . 7 7 f f 7 f
    . 7 7 7 . 7 7 7 . . 7 . . f 7 f
    . . 7 . 7 7 . 7 7 . 7 7 7 . 7 7
    7 7 . 7 7 7 7 7 7 7 7 . 7 7 7 .
    7 . . 7 . 7 . . . 7 . . . 7 . .
"""), True)
#end stuff (flag pole)
scene.set_tile(7, img("""
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
"""), True)
#bottom of pole 
scene.set_tile(8, img("""
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . 1 1 1 1 1 1 . . . . .
    . . . 1 1 1 1 1 1 1 1 1 1 . . .
    . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 .
"""), True)
#top of pole
scene.set_tile(9, img("""
    . . . . . . . 5 5 . . . . . . .
    . . . . . . . 5 5 . . . . . . .
    2 4 4 4 4 4 2 1 1 . . . . . . .
    4 2 4 4 4 2 4 1 1 . . . . . . .
    4 4 2 2 2 4 4 1 1 . . . . . . .
    4 4 2 2 2 4 4 1 1 . . . . . . .
    4 2 4 4 4 2 4 1 1 . . . . . . .
    2 4 4 4 4 4 2 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
    . . . . . . . 1 1 . . . . . . .
"""), True)

#background stuff 
scene.set_background_image(img("""
    eeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeee
    eeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeee
    eeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeee
    eeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeee
    eeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeee
    eeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeee
    eeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeee
    eeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeee
    eeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeee
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeee
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeee
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeee
    eeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeee
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeee
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
    eeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeee
"""))


#THE GIANT ENEMY SPIDER MK1
giant_enemy_spider = sprites.create(img("""
    . . . . f f f f f f f . . . . .
    . . . f f f f f f f f f . . . .
    . . . f f f f f f f f f . . . .
    . . . f f f f f f f f f . . . .
    . . . f f 2 f f f 2 f f . . . .
    . . . f f f f f f f f f . . . .
    . . . f 2 2 2 f f f f f . . . .
    . . . f f f f 2 2 f f f . . . .
    . . . . f f f f f f f . . . . .
    . . . . f f f f f f f . . . . .
    . . . f . . . . . . . f . . . .
    . . f . . . . . . . . . f . . .
    . . f . . . . . . . . . . f . .
    . f . . . . . . . . . . . f . .
    f . . . . . . . . . . . . . f .
    f . . . . . . . . . . . . . . f
"""))
tiles.place_on_tile(giant_enemy_spider, tiles.get_tile_location(6, 21))
def on_update2():
    if giant_enemy_spider.x >= 400:
        giant_enemy_spider.set_velocity(-50, 0)
    elif giant_enemy_spider.x <= 105:
        giant_enemy_spider.set_velocity(50, 0)
game.on_update(on_update2)

#THE GIANT ENEMY SPIDER MK2
somewhat_large_enemy_spider = sprites.create(img("""
    . . . . . f f f f f f . . . . .
    . . . . f f f f f f f f . . . .
    . . . f f f f f f f f f f . . .
    . . f f 2 2 f f f f 2 2 f f . .
    . f f f 2 2 f f f f 2 2 f f f .
    . f f f f f f 2 2 f f f f f f .
    . f f f f f f 2 2 f f f f f f .
    . f f f f f f f f f f f f f f .
    . f f f f f f f f f f f f f f .
    . . f f 2 2 2 2 2 2 2 2 f f . .
    . . . f f f f f f f f f f . . .
    . . . . f f f f f f f f . . . .
    . . . f . . . . . . . . f . . .
    . . f . . . . . . . . . . f . .
    . f . . . . . . . . . . . . f .
    f . . . . . . . . . . . . . . f
"""))
tiles.place_on_tile(somewhat_large_enemy_spider, tiles.get_tile_location(79, 20))
def on_update3():
    if somewhat_large_enemy_spider.x <= 1272:
        somewhat_large_enemy_spider.set_velocity(20, 0)
    elif somewhat_large_enemy_spider.x >= 1382:
        somewhat_large_enemy_spider.set_velocity(-20, 0)
game.on_update(on_update3)

#you touch enemy spiders
anatole.overlaps_with(somewhat_large_enemy_spider)
info.change_life_by(-1)


#if you finish level
def on_hit_tile2(sprite):
    game.splash("you win")
scene.on_hit_tile(SpriteKind.player, 7, on_hit_tile2)

def on_hit_tile3(sprite):
    game.splash("you win")
scene.on_hit_tile(SpriteKind.player, 8, on_hit_tile2)

tiles.place_on_tile(anatole, tiles.get_tile_location(5, 21))

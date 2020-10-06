/** 
Title: The Adventures of Anatole
Creators: Eric
Description:

 */
// Anatole and Camera Stuff and spawn
let anatole = sprites.create(img`
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
    . d d 2 2 2 2 2 2 2 2 2 d f f f
    . d d 2 2 2 2 5 2 2 2 2 d f . .
    . . . 2 2 2 2 2 2 2 2 2 . . . .
    . . . . f f . . . f f . . . . .
    . . . f f f . . . f f f . . . .
`, SpriteKind.Player)
scene.cameraFollowSprite(anatole)
// anatole shooty shoot 
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed() {
    let projectile = sprites.createProjectileFromSprite(img`
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
  `, anatole, 99999, 0)
})
//  Double Jump Function & Movement
controller.moveSprite(anatole, 100, 0)
let can_double_jump = true
controller.A.onEvent(ControllerButtonEvent.Pressed, function jump() {
    
    if (can_double_jump) {
        anatole.vy = -100
    }
    
    can_double_jump = anatole.isHittingTile(CollisionDirection.Bottom)
})
game.onUpdate(function on_update() {
    
    if (anatole.isHittingTile(CollisionDirection.Bottom)) {
        can_double_jump = true
    }
    
})
anatole.ay = 200
// Health Function (DO NOT CHANGE THE NUMBERS, HIGHER THAN 1 TENDS TO CAUSE ISSUES WITH SPAWNING, SO HE JUST DIES ON IMPACT NOW LOL.)
info.setLife(1)
// Lava Obstacle
scene.setTile(2, img`
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
`, true)
scene.onHitTile(SpriteKind.Player, 2, function on_hit_tile(sprite: Sprite) {
    sprite.setPosition(sprite.x - 100, sprite.y)
    info.player1.changeLifeBy(-1)
})
// THIS IS STUFF WITH TILEMAP, DON'T TOUCH, IT WORKS AND I WOULD LIKE TO KEEP IT LIKE THAT.
//  actual map
scene.setTileMap(img`
    333333333333333333333333333333333333333333333333333333333333333333333333....................................................................................................................................................................................................................................
    333333333333333333333333333333333333333333333333333333333333333333333333....................................................................................................................................................................................................................................
    333333333333333333333333333333333333333333333333333333333333333333333333....................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.........................................................................................................................................................................................................................................................................................................
    333.....................................5...................................................................................................................................................................................................................................................................
    333...................................5.4.5.................................................................................................................................................................................................................................................................
    333.................................5.4.4.4.5...............................................................................................................................................................................................................................................................
    333...............................5.4.4.4.4.4.5...............5.............................................................................................................................................................................................................................................
    333.............................5.4.4.4.4.4.4.4.5...........5.4.5...........................................................................................................................................................................................................................................
    333...........................5.4.4.4.4.4.4.4.4.4.5.......5.4.4.4...........................................................................................................................................................................................................................................
    333.........................5.4.4.4.4.4.4.4.4.4.4.4.5...5.4.4.4.4.............333333333.....................................................................................................................................................................................................................
    33333333333333333333333333..4.4.4.4.4.4.4.4.4.4.4.4.4.5.4.4.4.4.4.333333..336.333333333.....................................................................................................................................................................................................................
    33333333333333333333333333..4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.333333..666.663333366................5..5..5..5..5..5.33333333333333333333333333333333....................................................................................................................................................
    333333333333333333333333332222222222222222222222222222222222222222333333...6...6666666....63333333336..4..4..4..4..4..4.33333333333333333333333333333333....................................................................................................................................................
    333333333333333333333333332222222222222222222222222222222222222222333333...................633333336...4..4..4..4..4..4.33333333333333333333333333333333....................................................................................................................................................
    333333333333333333333333332222222222222222222222222222222222222222333333....................6633336....4..4..4..4..4..4.33333333333333333333333333333333....................................................................................................................................................
    333333333333333333333333332222222222222222222222222222222222222222333333......................6336.....4..4..4..4..4..4.33333333333333333333333333333333....................................................................................................................................................
    333333333333333333333333332222222222222222222222222222222222222222333333.......................66......4..4..4..4..4..4.33333333333333333333333333333333....................................................................................................................................................
    333333333333333333333333332222222222222222222222222222222222222222333333...............................4..4..4..4..4..4.33333333333333333333333333333333....................................................................................................................................................
    333333333333333333333333332222222222222222222222222222222222222222333333...............................4..4..4..4..4..4.33333333333333333333333333333333....................................................................................................................................................
    333333333333333333333333332222222222222222222222222222222222222222333333...............................4..4..4..4..4..4.33333333333333333333333333333333....................................................................................................................................................
    333333333333333333333333332222222222222222222222222222222222222222333333...............................4..4..4..4..4..4.33333333333333333333333333333333....................................................................................................................................................
    333333333333333333333333333333333333333333333333333333333333333333333333...............................4..4..4..4..4..4.33333333333333333333333333333333....................................................................................................................................................
    33333333333333333333333333333333333333333333333333333333333333333333333322222222222222222222222222222222222222222222222233333333333333333333333333333333....................................................................................................................................................
    33333333333333333333333333333333333333333333333333333333333333333333333322222222222222222222222222222222222222222222222233333333333333333333333333333333....................................................................................................................................................
`)
// standard brick
scene.setTile(3, img`
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
`, true)
// supposed "spawn block" (WIP)
scene.setTile(15, img`
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
`, true)
// metal pole stuff
scene.setTile(4, img`
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
`, true)
// top of metal pole 
scene.setTile(5, img`
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
`, true)
// mossy stuff hanging off brick(?)
scene.setTile(6, img`
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
`, true)
// background stuff 
scene.setBackgroundImage(img`
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
`)

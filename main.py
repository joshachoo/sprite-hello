msg = "Hello World!"
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . 6 6 6 6 6 6 6 6 6 6 6 6 6 6 . 
            . 6 6 6 6 6 6 6 6 6 6 6 6 6 6 . 
            . 6 6 f f 6 6 6 6 6 6 f f 6 6 . 
            . 6 6 f f 6 6 6 6 6 6 f f 6 6 . 
            . 6 6 6 6 6 6 6 6 6 6 6 6 6 6 . 
            . 6 6 6 6 6 c c c c 6 6 6 6 6 . 
            . 6 6 6 6 6 6 c c 6 6 6 6 6 6 . 
            . 6 6 6 6 6 6 6 6 6 6 6 6 6 6 . 
            . 6 6 6 3 3 3 3 3 3 3 3 6 6 6 . 
            . 6 6 6 6 6 6 6 6 6 6 6 6 6 6 . 
            . . 6 6 6 6 6 6 6 6 6 6 6 6 . .
    """),
    SpriteKind.player)
scene.set_background_color(4)
mySprite.say(msg)
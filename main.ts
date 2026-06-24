let my_lemon = sprites.create(img`
. . . . 5 5 5 5 . . . .
. . . 5 5 5 5 5 5 . . .
. . 5 5 5 5 5 5 5 5 . .
. 5 5 5 5 5 5 5 5 5 5 .
. 5 5 5 5 5 5 5 5 5 5 .
. . 5 5 5 5 5 5 5 5 . .
. . . 5 5 5 5 5 5 . . .
. . . . 5 5 5 5 . . . .
`, SpriteKind.Player)
controller.moveSprite(my_lemon, 100, 100)
my_lemon.setStayInScreen(true)
info.setScore(0)
if (info.score() >= 50) {
    game.splash("BOSS TIME")
}

game.onUpdateInterval(1000, function spawn_enemy() {
    let enemy = sprites.create(img`
    2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2
    `, SpriteKind.Enemy)
    enemy.x = randint(0, 160)
    enemy.y = 0
    enemy.vy = 50 + info.score() * 2
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function hit_enemy(player: Sprite, enemy: Sprite) {
    game.over(false)
})
tiles.setTilemap(tilemap`level1`)
effects.starField.startScreenEffect()
game.onUpdateInterval(100, function add_score() {
    info.changeScoreBy(1)
})

my_lemon = sprites.create(img("""
. . . . 5 5 5 5 . . . .
. . . 5 5 5 5 5 5 . . .
. . 5 5 5 5 5 5 5 5 . .
. 5 5 5 5 5 5 5 5 5 5 .
. 5 5 5 5 5 5 5 5 5 5 .
. . 5 5 5 5 5 5 5 5 . .
. . . 5 5 5 5 5 5 . . .
. . . . 5 5 5 5 . . . .
"""), SpriteKind.player)

controller.move_sprite(my_lemon, 100, 100)
my_lemon.set_stay_in_screen(True)

info.set_score(0)
if info.score() >= 50:
    game.splash("BOSS TIME")

def spawn_enemy():
    enemy = sprites.create(img("""
    2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2
    """), SpriteKind.enemy)
    enemy.x = randint(0, 160)
    enemy.y = 0
    enemy.vy = 50 + info.score() * 2

game.on_update_interval(1000, spawn_enemy)

def hit_enemy(player, enemy):
    game.over(False)

sprites.on_overlap(SpriteKind.player,
                   SpriteKind.enemy,
                   hit_enemy)

tiles.set_tilemap(tilemap("""level1"""))
effects.star_field.start_screen_effect()

def add_score():
    info.change_score_by(1)

game.on_update_interval(100, add_score)

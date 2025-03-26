from pyray import check_collision_recs, check_collision_circle_rec

def colision_rect(rect1, rect2):
    return check_collision_recs(rect1, rect2)

def colision_rect_circle(vector, radius, player):
    return check_collision_circle_rec(vector, radius, player)
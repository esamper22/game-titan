from pyray import check_collision_recs, check_collision_circle_rec

def colision_rect(rect1, rect2):
    try:
        return check_collision_recs(rect1, rect2)
    except Exception as e:
        print(f"Error en colision_rect: {e}")
        return False

def colision_rect_circle(vector, radius, player):
    try:
        return check_collision_circle_rec(vector, radius, player)
    except Exception as e:
        print(f"Error en colision_rect_circle: {e}")
        return False
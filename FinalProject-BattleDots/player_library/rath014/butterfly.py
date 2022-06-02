import math
import random

my_dots = {}


def init():
    return("🦋")
last_x = 0
last_y = 0
def run(db_cursor , state):

    #get all my dots
    rows = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
    fetch_rows = rows.fetchall()
    #how many dots I have left
    num_rows = len(fetch_rows) 
    #find spawning location
    my_flag = db_cursor.execute(f"select x, y from main_game_field as gf, owner where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
    #foods = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = 'Food'")
    #enemies = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name != '{state['NAME']}' and owner.name != 'Food'")
    
    for row in fetch_rows:

        #get all the foods
        foods = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name != '{state['NAME']}' and owner.name = 'Food'")
        fetch_foods = foods.fetchall()
        #how many foods are left
        num_foods = len(fetch_foods)

        #get all the enemies
        enemies = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name != '{state['NAME']}' and owner.name != 'Food'")
        fetch_enemies = enemies.fetchall()
        #how many enemies are left
        num_enemies = len(fetch_enemies)
        
        #if no foods or enemies left, flutter around randomly
        if num_foods == 0 and num_enemies == 0:
            x_direct = random.choice([-1, 0, 1])
            y_direct = random.choice([-1, 0, 1])
            
        else:
            closest_x = state['MAX_X']
            closest_y = state['MAX_Y']
            #variable to find the smallest dist between my dot and a food/enemy
            smallest_dist = (closest_x * closest_y)**2

            #if there is food left, find smallest distance between my dot and a food
            if num_foods > 0:
                for food in fetch_foods:
                    dist = math.sqrt((row[0]-food[0])**2+(row[1]-food[1])**2)
                    if dist < smallest_dist:
                        closest_x = food[0]
                        closest_y = food[1]
                        smallest_dist = dist

            #if there are enemies left, find smallest distance between my dot and an enemy
            if num_enemies > 0:
                for enemy in fetch_enemies:
                    dist = math.sqrt((row[0]-enemy[0])**2+(row[1]-enemy[1])**2)
                    if dist < smallest_dist:
                        closest_x = enemy[0]
                        closest_y = enemy[1]
                        smallest_dist = dist
            #calculate offset based on the location of food/enemy
            if closest_x < row[0]:
                x_direct = -1
            elif closest_x > row[0]:
                x_direct = 1
            else:
                x_direct = 0
            if closest_y < row[1]:
                y_direct = -1
            elif closest_y > row[1]:
                y_direct = 1
            else:
                y_direct = 0

        
        #move my dot
        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + x_direct}, {row[1] + y_direct}, 'MOVE')")
        #global last_x
        #global last_y
        last_x = row[0] + x_direct
        last_y = row[1] + y_direct

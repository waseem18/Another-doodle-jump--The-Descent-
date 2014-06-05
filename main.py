#The Descent
import simplegui, codeskulptor
import random

#constants
runs = 0
person_vel = 8.0
block_vel_inc = 0.02
width = 600.0
height = 600.0
canvas_width = 800.0
canvas_height = 600.0
block_width = 150.0
block_height = 20.0
spike_top_height = 20.0
distance = 0
last_distance = 0
y_vel = -1.0
distance_diff_ini = 2
distance_diff = 4
person_half_width = 30.0
person_half_height = 42.0
fall_acc = 0.5
left_right_vel = 3.0
display = 0
in_play = 0
restart_state = 0
game_over_state = 0
scores = set()
last_spawned_block = 0
initial_play = 1
break_time = 0
score = 0
score2 = 0
bonus = 0
bonus2 = 0
explosion_group = set()
message_set = set()
explosion_time = 0
break_block = 0
display_start = 1
display_how_to = 0
display_intro = 1
display_high_score = 0
display_how_to_button = 1
display_high_score_button = 1
display_mode_selection = 0
scr = set()
display_high_score = 0
game_over_tp = 0
you_break = 0
you2_break = 0
you_explode = 0
you2_explode = 0
you_game_over = 0
you2_game_over = 0
s500 = 0
s1000 = 0
s5000 = 0
s10000 = 0
p1_win = 0
p2_win = 0
break_set = set()
mode = 1
respawn_zombie_set = set()
name = "Player 1"
name2 = "Player 2"
message_center_pos = [width / 2 - 60, height / 2 -60]
dic = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
dic2 = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

#image_info class
class image_info:
    def __init__(self, center, size, radius = 0, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_animated(self):
        return self.animated
    
    
PREFIX = codeskulptor.file2url('demos-')[:-6] + "descent/"

#images
background_image = simplegui.load_image(PREFIX + "background.png")

break_image = simplegui.load_image(PREFIX + "break.png")
break_info = image_info([75,10], [150,20])

break2_image = simplegui.load_image(PREFIX + "break2.png")

break3_image = simplegui.load_image(PREFIX + "break3.png")

break4_image = simplegui.load_image(PREFIX + "break4.png")

break5_image = simplegui.load_image(PREFIX + "break5.png")
                                    
break6_image = simplegui.load_image(PREFIX + "break6.png")

break7_image = simplegui.load_image(PREFIX + "break7.png")
                                    
normal_image = simplegui.load_image(PREFIX + "normal.png")
normal_info = image_info([75,10], [150,20])


how_to_button_image = simplegui.load_image(PREFIX + "how_to_button.png")
how_to_button_info = image_info([125,25], [250,50])

p1_mode_image = simplegui.load_image(PREFIX + "1p_mode.png")
p1_mode_info = image_info([125,25], [250,50])

p2_mode_image = simplegui.load_image(PREFIX + "2p_mode.png")
p2_mode_info = image_info([125,25], [250,50])

how_to_image = simplegui.load_image(PREFIX + "how_to.png")
how_to_info = image_info([250,200], [500,400])

high_score_button_image = simplegui.load_image(PREFIX + "high_score_button.png")
high_score_button_info = image_info([182,25], [364,50])

lamp_image = simplegui.load_image(PREFIX + "lamp.png")
lamp_info = image_info([17,27], [35,55])

person_image = simplegui.load_image(PREFIX + "person.png")
person_info = image_info([300,415], [600,830])

person2_image = simplegui.load_image(PREFIX + "person2.png")

person2_right_image = simplegui.load_image(PREFIX + "person2_right.png")

person_right_image = simplegui.load_image(PREFIX + "person_right.png")
person_right_info = image_info([300,415], [600,830])

spike_top_image = simplegui.load_image(PREFIX + "spike_top.png")
spike_top_info = image_info([300,10], [600,20])

spike_image = simplegui.load_image(PREFIX + "spike.png")
spike_info = image_info([75,10], [150,20])

spring_image = simplegui.load_image(PREFIX + "spring.png")
spring_info = image_info([75,10], [150,20])

start_image = simplegui.load_image(PREFIX + "start.png")
start_info = image_info([50,25], [100,50])

left_block_image = simplegui.load_image(PREFIX + "left_block.png")
left_block_info = image_info([75,10], [150,20])

right_block_image = simplegui.load_image(PREFIX + "right_block.png")
right_block_info = image_info([75,10], [150,20])

intro_image = simplegui.load_image(PREFIX + "intro.png")
intro_info = image_info([250,200], [500,400])

diamond_image = simplegui.load_image(PREFIX + "diamond_25_25.png")
diamond_info = image_info([13,13], [25,25])

gold_image = simplegui.load_image(PREFIX + "gold_30_23.png")
gold_info = image_info([15,12], [30,23])

bomb_image = simplegui.load_image(PREFIX + "bomb_24_24.png")
bomb_info = image_info([12,12], [24,24])

pork_image = simplegui.load_image(PREFIX + "pork_chop_25_25.png")
pork_info = image_info([13,13], [25,25])

red_stone_image = simplegui.load_image(PREFIX + "red_stone_23_23.png")
red_stone_info = image_info([12,12], [23,23])

zombie_image = simplegui.load_image(PREFIX + "zombie_381_48.png")
zombie_info = image_info([23,24], [47,48])

zombie_reverse_image = simplegui.load_image(PREFIX + "zombie_reverse_381_48.png")
zombie_reverse_info = image_info([23,24], [47,48])

explosion_sound = simplegui.load_sound(PREFIX + "bomb.mp3")

crumble_sound = simplegui.load_sound(PREFIX + "Crumble%20Sound.mp3")

background_music = simplegui.load_sound(PREFIX + "background%20music.mp3")

spring_sound = simplegui.load_sound(PREFIX + "spring.mp3")

get_item_sound = simplegui.load_sound(PREFIX + "gotitem.mp3")

zombie_sound = simplegui.load_sound(PREFIX + "Zombie.mp3")

explosion_info = image_info([64, 64], [128, 128])
explosion_image = simplegui.load_image(PREFIX + "explosion_alpha.png")

crumble_sound.set_volume(0.5)

#message helper functions
def hex_to_dec(string):
    a = string[0]
    b = string[1]
    num1 = dic[a]
    num2 = dic[b]
    result = num1 * 16 + num2
    return result
    
def hex_to_rgb(color):
    r = color[1] + color[2]
    g = color[3] + color[4] 
    b = color[5] + color[6]
    r = hex_to_dec(r)
    g = hex_to_dec(g)
    b = hex_to_dec(b)
    return [r,g,b]

def rgb_to_hex(color):
    result = "#"
    for i in range(0,3):
        dig1 = int (color[i] / 16)
        dig2 = int (color[i] % 16)
        result += dic2[dig1]
        result += dic2[dig2]
    return result

#message class
class message:
    def __init__(self, amessage, pos, size, color, frame, font, fade):
        self.message = amessage
        self.pos = pos
        self.size = size
        self.frame = frame
        self.fade = fade
        self.age = 0
        self.font = font
        self.color = hex_to_rgb(color)
        self.r = self.color[0]
        self.g = self.color[1]
        self.b = self.color[2]
        self.rstep = float(self.r) / frame
        self.gstep = float(self.g) / frame
        self.bstep = float(self.b) / frame
        self.r = 0.0
        self.g = 0.0
        self.b = 0.0
        self.posstep = - 20.0 / frame
        self.pos0 = self.pos[0]
        self.pos1 = self.pos[1] + 10.0
        self.remove = 0
    
    def update(self):
        if self.age < self.frame:
            self.age += 1
            self.r += self.rstep
            self.g += self.gstep
            self.b += self.bstep
            self.pos1 += self.posstep
        elif self.age < self.frame * 2 and self.fade:
            self.age += 1
            self.r -= self.rstep
            self.g -= self.gstep
            self.b -= self.bstep
            self.pos1 += self.posstep
        if self.age == self.frame * 2 and self.fade:
            self.remove = 1
            
    def draw(self, canvas):
        canvas.draw_text(self.message, [self.pos0, self.pos1], self.size, rgb_to_hex([self.r, self.g, self.b]), self.font)
        
    def get_remove_status(self):
        return self.remove
    
#sprite class
class sprite:
    def __init__(self, pos, x_vel, y_vel, tp, block, sound = None):
        self.vel = [x_vel,y_vel]
        self.tp = tp
        self.animated = 0
        self.image = 0
        self.center = 0
        self.size = 0
        self.remove = 0
        self.age = 0
        self.block = block
        self.acc = 0
        self.fall = 1
        if self.tp == "diamond":
            self.image = diamond_image
            self.center = diamond_info.get_center()
            self.size = diamond_info.get_size()
            self.pos = [pos[0], pos[1] - block_height / 2 - self.size[1] / 2]
        elif self.tp == "gold":
            self.image = gold_image
            self.center = gold_info.get_center()
            self.size = gold_info.get_size()
            self.pos = [pos[0], pos[1] - block_height / 2 - self.size[1] / 2]
        elif self.tp == "bomb":
            self.image = bomb_image
            self.center = bomb_info.get_center()
            self.size = bomb_info.get_size()
            self.pos = [pos[0], pos[1] - block_height / 2 - self.size[1] / 2]
        elif self.tp == "pork":
            self.image = pork_image
            self.center = pork_info.get_center()
            self.size = pork_info.get_size()
            self.pos = [pos[0], pos[1] - block_height / 2 - self.size[1] / 2]
        elif self.tp == "red_stone":
            self.image = red_stone_image
            self.center = red_stone_info.get_center()
            self.size = red_stone_info.get_size()
            self.pos = [pos[0], pos[1] - block_height / 2 - self.size[1] / 2]
        elif self.tp == "zombie":
            zombie_sound.rewind()
            zombie_sound.play()
            if self.vel[0] < 0:
                self.image = zombie_reverse_image
            else:
                self.image = zombie_image
            self.center = zombie_info.get_center()
            self.size = zombie_info.get_size()
            self.animated = 1
            self.image_center_ini = [23,24]
            self.pos = [pos[0], pos[1] - block_height / 2 - self.size[1] / 2]
        elif self.tp == "explosion":
            self.image = explosion_image
            self.center = explosion_info.get_center()
            self.size = explosion_info.get_size()
            self.animated = 1
            self.image_center_ini = [64,64]
            self.pos = [pos[0], pos[1]]
               
    
    def check_which_to_fall_on(self):
        global display, break_time
        for block in block_set:
            if (block.get_pos()[0] - block_width / 2 - 10 <= self.pos[0] <= block.get_pos()[0] + block_width / 2 + 10) and (block.get_pos()[1] - block_height / 2 - self.vel[1] <= self.pos[1] + self.center[1] <= block.get_pos()[1] - block_height / 2 + self.vel[1]):
                self.block = block
                return 1
            
    def set_fall(self):
        self.fall = 1
        self.acc = fall_acc
            
    def update(self):
        global you_explode, you2_explode, respawn_zombie_set
        if self.tp != "zombie":
            self.vel[0] = self.block.get_vel()[0]
            
        if self.tp == "zombie" and self.pos[0] + self.vel[0] < self.block.get_pos()[0] - 70:
            diff = -(self.vel[0] - self.block.get_vel()[0])
            self.vel[0] = self.block.get_vel()[0] + diff
            self.image = zombie_image
            
        if self.tp == "zombie" and self.pos[0] + self.vel[0] > self.block.get_pos()[0] + 70:
            diff = -(self.vel[0] - self.block.get_vel()[0])
            self.vel[0] = self.block.get_vel()[0] + diff
            self.image = zombie_reverse_image
            
        global bonus, bonus2
        if self.fall:
            if self.check_which_to_fall_on():
                self.acc = 0
                self.vel[1] = self.block.get_vel()[1]
                self.pos[1] = self.block.get_pos()[1] - self.center[1] - block_height / 2
                self.fall = 0
        else:
            if self.pos[0] < self.block.get_pos()[0] - block_width / 2 - 10 or self.pos[0] > self.block.get_pos()[0] + block_width / 2 + 10:
                self.fall = 1
                self.acc = fall_acc
                
        self.vel[1] += self.acc
        if self.tp == "zombie":
            self.age += 0.05
        if self.tp == "explosion":
            self.age += 1
        if self.tp == "explosion" and self.age >= 24:
            self.remove = 1
        for i in range(0,2):
            self.pos[i] += self.vel[i]
        self.pos[0] = self.pos[0] % width
        if self.pos[0] - self.size[0] / 2 - 3 < you.get_pos()[0] < self.pos[0] + self.size[0] / 2 + 3:
            if self.pos[1] + self.center[1] - 6 < you.get_pos()[1] + person_half_height < self.pos[1] + self.center[1] + 6:
                if self.tp == "diamond":
                    bonus += 1000
                    get_item_sound.rewind()
                    get_item_sound.play()
                    message_set.add(message("Bonus +1000", message_center_pos, 30, "#FFFFFF", 30, "serif", 1))
                if self.tp == "gold":
                    bonus += 500
                    get_item_sound.rewind()
                    get_item_sound.play()
                    message_set.add(message("Bonus +500", message_center_pos, 30, "#FFFFFF", 30, "serif", 1))
                if self.tp == "red_stone":
                    bonus += 250
                    get_item_sound.rewind()
                    get_item_sound.play()
                    message_set.add(message("Bonus +250", message_center_pos, 30, "#FFFFFF", 30, "serif", 1))
                if self.tp == "bomb":
                    timer_explosion.start()   
                    you_explode = 1
                if self.tp == "pork":
                    you.add_health()
                    get_item_sound.rewind()
                    get_item_sound.play()
                    message_set.add(message("Health +2", [message_center_pos[0], message_center_pos[1] + 30], 30, "#FFFFFF", 30, "serif", 1))
                if self.tp == "zombie":
                    you.deduct_health_zombie()
                    zombie_sound.rewind()
                    zombie_sound.play()
                    respawn_zombie_set.add((self.block, self.vel[0], 0))
                    timer_zombie.start()
                    message_set.add(message("Health -2", [message_center_pos[0], message_center_pos[1] + 30], 30, "#FFFFFF", 30, "serif", 1))
                self.remove = 1
                
        if mode == 2 and self.pos[0] - self.size[0] / 2 - 3 < you2.get_pos()[0] < self.pos[0] + self.size[0] / 2 + 3:
            if self.pos[1] + self.center[1] - 6 < you2.get_pos()[1] + person_half_height < self.pos[1] + self.center[1] + 6:
                if self.tp == "diamond":
                    bonus2 += 1000
                    get_item_sound.rewind()
                    get_item_sound.play()
                    message_set.add(message("Bonus +1000", message_center_pos, 30, "#FFFFFF", 30, "serif", 1))
                if self.tp == "gold":
                    bonus2 += 500
                    get_item_sound.rewind()
                    get_item_sound.play()
                    message_set.add(message("Bonus +500", message_center_pos, 30, "#FFFFFF", 30, "serif", 1))
                if self.tp == "red_stone":
                    bonus2 += 250
                    get_item_sound.rewind()
                    get_item_sound.play()
                    message_set.add(message("Bonus +250", message_center_pos, 30, "#FFFFFF", 30, "serif", 1))
                if self.tp == "bomb":
                    you2_explode = 1
                    timer_explosion.start()   
                if self.tp == "pork":
                    you2.add_health()
                    get_item_sound.rewind()
                    get_item_sound.play()
                    message_set.add(message("Health +2", [message_center_pos[0], message_center_pos[1] + 27], 30, "#FFFFFF", 30, "serif", 1))
                if self.tp == "zombie":
                    you2.deduct_health_zombie()
                    zombie_sound.rewind()
                    zombie_sound.play()
                    respawn_zombie_set.add((self.block, self.vel[0], 0))
                    timer_zombie.start()
                    message_set.add(message("Health -2", [message_center_pos[0], message_center_pos[1] + 30], 30, "#FFFFFF", 30, "serif", 1))
                self.remove = 1
                
    def get_block(self):
        return self.block
    
    def out_of_range(self):
        if self.pos[1] < 0:
            return 1
        else:
            return 0
   
    
    def remove_block(self):
        block_set.remove(self.block)
        
    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    def get_type(self):
        return self.tp
    
    def draw(self, canvas):
        if not self.animated:
            canvas.draw_image(self.image, self.center, self.size, self.pos, self.size)
        else:
            if self.tp == "zombie":
                step = int(self.age % 8)
                size = self.size[0]
                pos = [0,0]
                pos[0] = self.image_center_ini[0] + size * (step)
                pos[1] = self.center[1]
                canvas.draw_image(self.image, pos, self.size, self.pos, self.size)
            elif self.tp == "explosion":
                step = self.age
                size = self.size[0]
                pos = [0,0]
                pos[0] = self.image_center_ini[0] + size * (step)
                pos[1] = self.center[1]
                canvas.draw_image(self.image, pos, self.size, self.pos, [self.size[0] * 3, self.size[1] * 3])
                
    def get_remove_status(self):
        return self.remove
    
#brick class
class block:
    def __init__(self, pos, x_vel, y_vel, tp):
        self.vel = [x_vel,y_vel]
        self.pos = pos
        self.tp = tp
        self.animated = 0
        self.age = 0
        self.started = 0
        self.effective1 = 1
        self.effective2 = 1
        if self.tp == "spike":
            self.image = spike_image
            self.center = spike_info.get_center()
            self.size = spike_info.get_size()
        elif self.tp == "normal":
            self.image = normal_image
            self.center = normal_info.get_center()
            self.size = normal_info.get_size()
        elif self.tp == "spring":
            self.image = spring_image
            self.center = spring_info.get_center()
            self.size = spring_info.get_size()
        elif self.tp == "break":
            self.image = break_image
            self.center = break_info.get_center()
            self.size = break_info.get_size()
            self.animated = 1
        elif self.tp == "left_block":
            self.image = left_block_image
            self.center = left_block_info.get_center()
            self.size = left_block_info.get_size()
        elif self.tp == "right_block":
            self.image = right_block_image
            self.center = right_block_info.get_center()
            self.size = right_block_info.get_size()
            
    def update(self):
        for i in range(0,2):
            self.pos[i] += self.vel[i]
        if self.pos[0] > width - block_width / 2 or self.pos[0] < block_width / 2:
            self.vel[0] = -self.vel[0]
            if you.get_block() == self:
                you.change_speed(2 * self.vel[0])
            if you2.get_block() == self:
                you2.change_speed(2 * self.vel[0])
            
    def out_of_range(self):
        if self.pos[1] < 0:
            return 1
        else:
            return 0
    
    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    def get_effective(self, name):
        if name == 1:
            return self.effective1
        elif name == 2:
            return self.effective2
    
    def set_effective_0(self, name):
        if name == 1:
            self.effective1 = 0
        elif name == 2:
            self.effective2 = 0
        
    def get_type(self):
        return self.tp
    
    def start(self):
        self.started = 1
        
    def stop_start(self):
        self.started = 0
        
    def draw(self, canvas):
        #draw two pictures for screen wrap
        canvas.draw_image(self.image, self.center, self.size, self.pos, self.size)
        canvas.draw_image(self.image, self.center, self.size, [self.pos[0] - width, self.pos[1]], self.size)
        if self.animated and self.started:
            if 10 < self.age <= 20:
                self.image = break2_image
            if 20 < self.age <= 30:
                self.image = break3_image
            if 30 < self.age <= 40:
                self.image = break4_image
            if 40 < self.age <= 50:
                self.image = break5_image
            if self.age > 50:
                self.image = break6_image
#            if self.age > 60:
#                self.image = break7_image
            self.age += 1
            

#person class
class person:
    def __init__(self, pos, vel, in_play, name):
        self.vel = vel
        self.pos = pos
        self.image = person_image
        self.center = person_info.get_center()
        self.size = person_info.get_size()
        self.acc = 0
        self.health = 10
        self.fall = 1
        self.block = 0
        self.display_size = [self.size[0] / 10, self.size[1] / 10]
        self.on_spike = 0
        self.in_play = in_play
        self.on_left = 0
        self.on_right = 0
        self.last_vel_inc = 0
        self.face_left = 1
        self.speed_change = 0
        self.name = name
        self.alive = 1
        if self.name == 2:
            self.image = person2_image
            
    def change_speed(self, speed):
        self.vel[0] += speed
        self.speed_change = speed
    
    def reset_vertical_vel(self):
        self.vel[1] = 0
        
    def set_alive(self):
        self.alive = 1
        
    def left(self):
        if self.in_play:
            self.vel[0] -= person_vel
            self.face_left = 1
            
    def right(self):
        if self.in_play:
            self.vel[0] += person_vel
            self.face_left = 0
    
    def get_health(self):
        return self.health
    
    def reset_left(self):
        if self.in_play:
            self.vel[0] += person_vel
        
    def reset_right(self):
        if self.in_play:
            self.vel[0] -= person_vel
        
    
    #deduct health when falling on spike
    def deduct_health(self):
        if self.health - 2 <= 0:
            self.health = 0
        else:
            self.health -= 2
        if self.health <= 4:
            message_set.add(message("Low Health", [message_center_pos[0], message_center_pos[1] + 50], 30, "#FFFFFF", 30, "serif", 1))
       
    #deduct health when hitting the top
    def deduct_health_top(self):
        if self.health - 0.2 <= 0:
            self.health = 0
        else:
            self.health -= 0.2
        
    
    def add_health(self):
        if self.health <= 8:
            self.health += 2
        else:
            self.health = 10
        
    def set_fall(self):
        if self.block != 0:
            if self.block.get_effective(self.name) and self.block.get_type() == "spring":
                self.block.set_effective_0(self.name)
                
        self.fall = 1
        self.acc = fall_acc
        
    def deduct_health_zombie(self):
        if self.health - 2 <= 0:
            self.health = 0
        else:
            self.health -= 2
        
    def remove_block(self):
        a = 0
        for ablock in block_set:
            if ablock == self.block:
                a = 1
        if a:
            block_set.remove(self.block)
    
    def explode(self):
        message_set.add(message("Health -2", [message_center_pos[0], message_center_pos[1] + 30], 30, "#FFFFFF", 30, "serif", 1))
        explosion = sprite([self.pos[0], self.block.get_pos()[1]], 0, 0, "explosion", self.block, explosion_sound)
        explosion_group.add(explosion)
        self.remove_block()
        self.set_fall()
        self.deduct_health()
        
    def check_which_to_fall_on(self):
        global display, break_time, break_block, you_break, you2_break, you_explode, you2_explode
        for block in block_set:
            if (block.get_pos()[0] - block_width / 2 - 10 <= self.pos[0] <= block.get_pos()[0] + block_width / 2 + 10) and (block.get_pos()[1] - block_height / 2 - self.vel[1] <= self.pos[1] + person_half_height <= block.get_pos()[1] - block_height / 2 + self.vel[1]) and block.get_effective(self.name):
                self.block = block
                if block.get_type() == "spike" and block.get_effective(self.name) and self.alive:
                    self.vel[0] = self.vel[0] - self.last_vel_inc + block.get_vel()[0]
                    self.last_vel_inc = block.get_vel()[0]
                    if self.on_left:
                        self.vel[0] += left_right_vel
                    if self.on_right:
                        self.vel[0] -= left_right_vel
                    self.on_left = 0
                    self.on_right = 0
                    
                    self.deduct_health()
                    message_set.add(message("Health -2", [message_center_pos[0], message_center_pos[1] + 30], 30, "#FFFFFF", 30, "serif", 1))
                    self.on_spike = 1
                    self.vel[0] -= self.speed_change
                    self.speed_change = 0
                    display = 1
                    #timer2.stop()
                    break_time = 0
                    
                elif block.get_type() == "break" and block.get_effective(self.name) and self.alive:
                    self.vel[0] -= self.speed_change
                    self.speed_change = 0
                    crumble_sound.rewind()
                    crumble_sound.play()
                    self.vel[0] = self.vel[0] - self.last_vel_inc + block.get_vel()[0]
                    self.last_vel_inc = block.get_vel()[0]
                    if self.on_left:
                        self.vel[0] += left_right_vel
                    if self.on_right:
                        self.vel[0] -= left_right_vel
                    self.on_left = 0
                    self.on_right = 0
                    break_set.add((self.block,0))
                    self.on_spike = 0
                    self.vel[1] = 0
                    self.fall = 0
                    break_block = self.block
                    if self.name == 1:
                        you_break = 1
                    if self.name == 2:
                        you2_break = 1
                    timer2.start()
                    self.block.start()
                    
                    
                elif block.get_type() == "spring" and block.get_effective(self.name) and self.alive:
                    self.vel[0] -= self.speed_change
                    self.speed_change = 0
                    spring_sound.rewind()
                    spring_sound.play()
                    self.vel[0] = self.vel[0] - self.last_vel_inc + block.get_vel()[0]
                    self.last_vel_inc = block.get_vel()[0]
                    if self.on_left:
                        self.vel[0] += left_right_vel
                    if self.on_right:
                        self.vel[0] -= left_right_vel
                    self.on_left = 0
                    self.on_right = 0
                    self.on_spike = 0
                    
                    self.vel[1] = - 12
                    self.fall = 1
                    self.acc = fall_acc
                    #timer2.stop()
                    break_time = 0
                    if self.health <= 9:
                        self.health += 1
                    return 0
                
                elif block.get_type() == "left_block" and block.get_effective(self.name) and self.alive:
                    self.vel[0] -= self.speed_change
                    self.speed_change = 0
                    self.vel[0] = self.vel[0] - self.last_vel_inc + block.get_vel()[0]
                    self.last_vel_inc = block.get_vel()[0]
                    if self.on_left:
                        self.vel[0] += left_right_vel
                    if self.on_right:
                        self.vel[0] -= left_right_vel
                    self.on_left = 1
                    self.on_right = 0
                    self.on_spike = 0
                    self.vel[0] -= left_right_vel 
                    #timer2.stop()
                    break_time = 0
                    
                elif block.get_type() == "right_block" and block.get_effective(self.name) and self.alive:
                    self.vel[0] -= self.speed_change
                    self.speed_change = 0
                    self.vel[0] = self.vel[0] - self.last_vel_inc + block.get_vel()[0]
                    self.last_vel_inc = block.get_vel()[0]
                    if self.on_left:
                        self.vel[0] += left_right_vel
                    if self.on_right:
                        self.vel[0] -= left_right_vel
                    self.on_right = 1
                    self.on_left = 0
                    self.on_spike = 0
                    self.vel[0] += left_right_vel
                    #timer2.stop()
                    break_time = 0
                   
                elif self.alive:
                    self.vel[0] -= self.speed_change
                    self.speed_change = 0
                    self.vel[0] = self.vel[0] - self.last_vel_inc + block.get_vel()[0]
                    self.last_vel_inc = block.get_vel()[0]
                    if self.on_left:
                        self.vel[0] += left_right_vel
                    if self.on_right:
                        self.vel[0] -= left_right_vel
                    self.on_left = 0
                    self.on_right = 0
                    self.on_spike = 0
                    
                    self.on_left_right = 0
                    #timer2.stop()
                    break_time = 0
                    
                return 1

    def update(self):
        global you_game_over, you2_game_over, break_set
        temp = 0
        for ablock in block_set:
            if self.block == ablock:
                temp = 1
        if temp == 0:
            
            self.set_fall()
        if self.fall:
            if self.check_which_to_fall_on():
                self.acc = 0
                self.vel[1] = self.block.get_vel()[1]
                self.pos[1] = self.block.get_pos()[1] - person_half_height - block_height / 2
                self.fall = 0
        else:
            if self.pos[0] < self.block.get_pos()[0] - block_width / 2 - 10 or self.pos[0] > self.block.get_pos()[0] + block_width / 2 + 10:
                self.fall = 1
                copy_set = set(break_set)
                for item in copy_set:
                    if mode == 1 and self.block == item[0]:
                        break_set.remove(item)
                    if mode == 2 and (self.block == item[0] and self.name == 1 and you2.get_block() != item[0]) or (self.block == item[0] and self.name == 2 and you.get_block() != item[0]):
                        break_set.remove(item)
                        
                self.block.stop_start()
                self.acc = fall_acc
                
        self.vel[1] += self.acc
        for i in range(0,2):
            self.pos[i] += self.vel[i]

        self.pos[0] = self.pos[0] % width
        if self.pos[1] >= height + person_half_height:
            if mode == 2:
                if self.name == 1:
                    you_game_over = 1
                    self.health = 0
                if self.name == 2:
                    you2_game_over = 1
                    self.health = 0
                if you_game_over and you2_game_over:
                    game_over("fall")
            if mode == 1:
                game_over("fall")
        if self.pos[1] <= person_half_height - 10:
            if mode == 2:
                if self.name == 1:
                    you_game_over = 1
                    self.health = 0
                if self.name == 2:
                    you2_game_over = 1
                    self.health = 0
                if you_game_over and you2_game_over:
                    game_over("crush")
            if mode == 1:
                game_over("crush")
        if 0 - person_half_height < self.pos[1] < person_half_height + spike_top_height:
            self.deduct_health_top()
        if self.health <= 0:
            if mode == 2:
                self.alive = 0
                if self.name == 1:
                    you_game_over = 1
                    self.health = 0
                if self.name == 2:
                    you2_game_over = 1
                    self.health = 0
                if you_game_over and you2_game_over:
                    game_over("health")
            if mode == 1:
                game_over("health")
            
    def get_vel(self):
        return self.vel
    
    def get_pos(self):
        return self.pos
    
    def draw(self, canvas):
        if self.on_spike == 0 and self.face_left:
            if self.name == 1 and you_game_over == 0:
                canvas.draw_image(self.image, self.center, self.size, self.pos, self.display_size)
            elif self.name == 2 and you2_game_over == 0:
                canvas.draw_image(self.image, self.center, self.size, self.pos, self.display_size)
        elif self.on_spike and self.face_left:
            timer.start()
            if display:
                if self.name == 1 and you_game_over == 0:
                    canvas.draw_image(self.image, [self.center[0] + self.size[0], self.center[1]], self.size, self.pos, self.display_size)
                elif self.name == 2 and you2_game_over == 0:
                    canvas.draw_image(self.image, [self.center[0] + self.size[0], self.center[1]], self.size, self.pos, self.display_size)
            else:
                if self.name == 1 and you_game_over == 0:
                    canvas.draw_image(self.image, self.center, self.size, self.pos, self.display_size)
                elif self.name == 2 and you2_game_over == 0:
                    canvas.draw_image(self.image, self.center, self.size, self.pos, self.display_size)
        if self.on_spike == 0 and self.face_left == 0:
            if self.name == 1 and you_game_over == 0:
                canvas.draw_image(person_right_image, self.center, self.size, self.pos, self.display_size)
            elif self.name == 2 and you2_game_over == 0:
                canvas.draw_image(person2_right_image, self.center, self.size, self.pos, self.display_size)
        elif self.on_spike and self.face_left == 0:
            timer.start()
            if self.name == 1 and you_game_over == 0:
                if display:
                    canvas.draw_image(person_right_image, [self.center[0] + self.size[0], self.center[1]], self.size, self.pos, self.display_size)
                else:
                    canvas.draw_image(person_right_image, self.center, self.size, self.pos, self.display_size)
            if self.name == 2 and you2_game_over == 0:
                if display:
                    canvas.draw_image(person2_right_image, [self.center[0] + self.size[0], self.center[1]], self.size, self.pos, self.display_size)
                else:
                    canvas.draw_image(person2_right_image, self.center, self.size, self.pos, self.display_size)
        
    def get_health(self):
        return self.health

    def reset_pos(self):
        if self.name == 1:
            self.pos = [width / 2 + 20, height /2]
        elif self.name == 2:
            self.pos = [width / 2 - 20, height /2]    
    
    def reset_vel(self):
        self.vel = [0,0]
        self.on_left = 0
        self.on_right = 0
        self.on_spike = 0
    
    def reset_health(self):
        self.health = 10.0
        
    def get_block(self):
        return self.block

class sscore():
    def __init__(self):
        self.scores = []
    
    def add(self, val, name):
        self.scores.append([val, name])
        
    def return_1_score(self, lst):
        cur = 0
        maxi = 0
        for a in lst:
            if a[0]>cur:
                cur = a[0]
                maxi = a
        return maxi
    
    def return_2_score(self, lst):
        scores_copy = list(self.scores)
        scores_copy.remove(self.return_1_score(self.get_scores()))
        return self.return_1_score(scores_copy)
    
    def return_3_score(self, lst):
        scores_copy = list(self.scores)
        scores_copy.remove(self.return_1_score(scores_copy))
        scores_copy.remove(self.return_2_score(scores_copy))
        return self.return_1_score(scores_copy)
    
    def get_scores(self):
        return self.scores
    
#initialization
you = person([width / 2 + 20, height / 2], [0,0], 1, 1)
you2 = person([width / 2 - 20, height / 2], [0,0], 1, 2)
block_set = set()
sprite_set = set()
explosion_group = set()
scr = sscore()

#start game 
def start_game():
    global you, you2, you_game_over, display_start, display_mode_selection, you2_game_over, block_set, scr, in_play, initial_play, display_how_to, display_intro, explosion_group, break_block, display_high_score_button
    in_play = 1
    scr = sscore()
    break_block = 0
    initial_play = 0
    display_start = 0
    display_how_to = 0
    display_intro = 0
    display_high_score_button = 0
    display_mode_selection = 0
    you_game_over = 0
    you2_game_over = 0
    explosion_group = set()
    
    message_set.add(message("Welcome", [width / 2 - 80, height / 2 - 50], 50, "#FFFFFF", 30, "serif", 1))
    
    #create a set of blocks
    block_set = set()
    
    #create an instance of person and initial blocks
    pos0 = width / 2
    pos1 = block_height / 2 + height / 1.6
    you.set_fall()
    you2.set_fall()
    y_vel = -1 - distance / 20
    block_set.add(block([pos0, pos1], 0, y_vel, "normal"))
    pos0 = random.randrange(block_width / 2, width + 1 - block_width / 2)
    pos1 = block_height / 2 + height / 1.3
    y_vel = -1 - distance / 20
    block_set.add(block([pos0, pos1], 0, y_vel, "normal"))
    pos0 = random.randrange(block_width / 2, width + 1 - block_width / 2)
    pos1 = block_height / 2 + height / 1.0
    y_vel = -1 - distance / 20
    block_set.add(block([pos0, pos1], 0, y_vel, "normal"))
    pos0 = random.randrange(block_width / 2, width + 1 - block_width / 2)
    pos1 = block_height / 2 + height / 0.8
    y_vel = -1 - distance / 20
    block_set.add(block([pos0, pos1], 0, y_vel, "normal"))

#restart game
def restart():
    global you, you2, p1_win, p2_win, s500, s1000, s5000, s10000, respawn_zombie_set, display_high_score, break_set, block_set, display_start, display_mode_selection, you_game_over, you2_game_over, sprite_set, display_how_to, display_high_score_button, display_intro, in_play, distance, game_over_state, initial_play, score, score2, bonus, bonus2, explosion_group, break_block, message_set
    in_play = 1
    you.reset_vertical_vel()
    you2.reset_vertical_vel()
    s500 = 0
    s1000 = 0
    s5000 = 0
    s10000 = 0
    you.set_alive()
    you2.set_alive()
    display_how_to = 0
    respawn_zombie_set = set()
    display_high_score = 0
    break_set = set()
    display_intro = 0
    display_start = 0
    display_high_score_button = 0
    display_mode_selection = 0
    break_block = 0
    initial_play = 0
    distance = 0
    score = 0
    score2 = 0
    bonus = 0
    bonus2 = 0
    game_over_state = 0
    you_game_over = 0
    you2_game_over = 0
    
    #create a set of blocks
    block_set = set()
    sprite_set = set()
    explosion_group = set()
    message_set = set()
    
    #create an instance of person and initial blocks
    you.reset_pos()
    you.set_fall()
    you.reset_health()
    you2.reset_pos()
    you2.set_fall()
    you2.reset_health()
    pos0 = width / 2
    pos1 = block_height / 2 + height / 1.6
    y_vel = -1 - distance / 20
    block_set.add(block([pos0, pos1], 0, y_vel, "normal"))
    pos0 = random.randrange(block_width / 2, width + 1 - block_width / 2)
    pos1 = block_height / 2 + height / 1.3
    y_vel = -1 - distance / 20
    block_set.add(block([pos0, pos1], 0, y_vel, "normal"))
    pos0 = random.randrange(block_width / 2, width + 1 - block_width / 2)
    pos1 = block_height / 2 + height / 1.0
    y_vel = -1 - distance / 20
    block_set.add(block([pos0, pos1], 0, y_vel, "normal"))
    pos0 = random.randrange(block_width / 2, width + 1 - block_width / 2)
    pos1 = block_height / 2 + height / 0.8
    y_vel = -1 - distance / 20
    block_set.add(block([pos0, pos1], 0, y_vel, "normal"))
    
# Handler for mouse click
def click(cpos):
    global in_play, p1_win, p2_win, display_how_to, history_mode, mode, display_high_score, display_intro, display_start, display_mode_selection, display_how_to_button, display_high_score_button, display_high_score
    if display_mode_selection:
        if restart_state == 0:
            if (width / 2 - 120 - p1_mode_info.get_size()[0] / 2 <= cpos[0] <= width / 2 - 120 + p1_mode_info.get_size()[0] / 2) and (height - 100 - p1_mode_info.get_size()[1] / 2 <= cpos[1] <= height - 100 + p1_mode_info.get_size()[1] / 2):
                mode = 1
                start_game()
            if (width / 2 + 120 - p2_mode_info.get_size()[0] / 2 <= cpos[0] <= width / 2 + 120 + p2_mode_info.get_size()[0] / 2) and (height - 100 - p2_mode_info.get_size()[1] / 2 <= cpos[1] <= height - 100 + p2_mode_info.get_size()[1] / 2):
                mode = 2
                start_game()    
        if restart_state:
            if (width / 2 - 120 - p1_mode_info.get_size()[0] / 2 <= cpos[0] <= width / 2 - 120 + p1_mode_info.get_size()[0] / 2) and (height - 100 - p1_mode_info.get_size()[1] / 2 <= cpos[1] <= height - 100 + p1_mode_info.get_size()[1] / 2):
                mode = 1
                p1_win = 0
                p2_win = 0
                restart()
            if (width / 2 + 120 - p2_mode_info.get_size()[0] / 2 <= cpos[0] <= width / 2 + 120 + p2_mode_info.get_size()[0] / 2) and (height - 100 - p2_mode_info.get_size()[1] / 2 <= cpos[1] <= height - 100 + p2_mode_info.get_size()[1] / 2):
                mode = 2
                restart()
                
    if in_play == 0 and restart_state == 0:
        if (width / 2 - start_info.get_size()[0] / 2 <= cpos[0] <= width / 2 + start_info.get_size()[0] / 2) and (height - 100 - start_info.get_size()[1] / 2 <= cpos[1] <= height - 100 + start_info.get_size()[1] / 2):
            display_mode_selection = 1
            display_start = 0
            display_how_to = 0
            display_how_to_button = 0
            display_intro = 0
            display_high_score_button = 0
            display_high_score = 0
            
    if in_play == 0 and restart_state == 1:
        if (width / 2 - start_info.get_size()[0] / 2 <= cpos[0] <= width / 2 + start_info.get_size()[0] / 2) and (height - 100 - start_info.get_size()[1] / 2 <= cpos[1] <= height - 100 + start_info.get_size()[1] / 2):
            display_mode_selection = 1
            display_start = 0
            display_how_to = 0
            display_how_to_button = 0
            display_intro = 0
            display_high_score_button = 0
            display_high_score = 0
            
    if (width / 2 - how_to_button_info.get_size()[0] / 2 <= cpos[0] <= width / 2 + how_to_button_info.get_size()[0] / 2) and (height - 150 - how_to_button_info.get_size()[1] / 2 <= cpos[1] <= height - 150 + how_to_button_info.get_size()[1] / 2):
        if display_how_to == 0 and display_high_score == 0 and display_high_score_button:
            display_how_to = 1
            if initial_play:
                display_start = 1
                display_mode_selection = 0
            else:
                display_start = 0
                display_mode_selection = 1
            display_how_to_button = 0
            display_intro = 0
            display_high_score_button = 0
            display_high_score = 0
        
    if (width / 2 - high_score_button_info.get_size()[0] / 2 <= cpos[0] <= width / 2 + high_score_button_info.get_size()[0] / 2) and (height - 200 - high_score_button_info.get_size()[1] / 2 <= cpos[1] <= height - 200 + high_score_button_info.get_size()[1] / 2):
        if display_high_score == 0 and display_how_to == 0 and display_high_score_button:
            display_how_to = 0
            if initial_play:
                display_start = 1
                display_mode_selection = 0
            else:
                display_start = 0
                display_mode_selection = 1
            display_how_to_button = 0
            display_intro = 0
            display_high_score_button = 0
            display_high_score = 1
            
#keydown handler

def keydn(key):
    if key == simplegui.KEY_MAP['left']:
        you.left()
    elif key == simplegui.KEY_MAP['right']:
        you.right()
    elif key == simplegui.KEY_MAP['down']:
        you.set_fall()
    elif key == simplegui.KEY_MAP['a']:
        you2.left()
    elif key == simplegui.KEY_MAP['d']:
        you2.right()
    elif key == simplegui.KEY_MAP['s']:
        you2.set_fall()
        
#keyup handler

def keyup(key):
    if key == simplegui.KEY_MAP['left']:
        you.reset_left()
    elif key == simplegui.KEY_MAP['right']:
        you.reset_right()
    elif key == simplegui.KEY_MAP['a']:
        you2.reset_left()
    elif key == simplegui.KEY_MAP['d']:
        you2.reset_right()
            
#check if block is out of range and remove it
def check_remove_block(block_set):
    block_set_copy = set(block_set)
    for block in block_set_copy:
        if block.out_of_range():
            block_set.remove(block)

#check to remove sprite
def check_remove_sprite(sprite_set):
    sprite_set_copy = set(sprite_set)
    for sprite in sprite_set_copy:
        if sprite.get_remove_status() or sprite.out_of_range():
            sprite_set.remove(sprite)

def check_remove_explosion(explosion_group):
    explosion_set_copy = set(explosion_group)
    for sprite in explosion_set_copy:
        if sprite.get_remove_status():
            explosion_group.remove(sprite)

def check_remove_message(message_set):
    message_set_copy = set(message_set)
    for message in message_set_copy:
        if message.get_remove_status():
            message_set.remove(message)

def check_remove_explosion_block(pos):
    block_set_copy = set(block_set)
    for block in block_set_copy:
        if (block.get_pos()[0] - pos[0]) * (block.get_pos()[0] - pos[0]) + (block.get_pos()[1] - pos[1]) * (block.get_pos()[1] - pos[1]) < 40000:
            block_set.remove(block)
            

#spawn sprites
def spawn_sprite(block):
    pos = block.get_pos()
    vel = block.get_vel()
    temp_pos = random.randrange(0, 65)
    temp_sign = random.randrange(0,2)
    if temp_sign:
        temp_pos = - temp_pos
    temp = random.randrange(0,6)
    #sprite_set.add(sprite([pos[0] + temp_pos, pos[1]], vel[0], vel[1], "zombie", block))
    if temp == 0:
        tp = "diamond"
        sprite_set.add(sprite([pos[0] + temp_pos, pos[1]], vel[0], vel[1], tp, block))
    if temp == 1:
        tp = "gold"
        sprite_set.add(sprite([pos[0] + temp_pos, pos[1]], vel[0], vel[1], tp, block))
    if temp == 2 and block.get_type() != "break":
        tp = "bomb"
        sprite_set.add(sprite([pos[0] + temp_pos, pos[1]], vel[0], vel[1], tp, block))
    if temp == 3:
        tp = "pork"
        sprite_set.add(sprite([pos[0] + temp_pos, pos[1]], vel[0], vel[1], tp, block))
    if temp == 4:
        tp = "red_stone"
        sprite_set.add(sprite([pos[0] + temp_pos, pos[1]], vel[0], vel[1], tp, block))
    if temp == 5:
        tp = "zombie"
        temp_vel_0 = (random.randrange(0,20) + vel[0]) / 10.0
        sprite_set.add(sprite([pos[0] + temp_pos, pos[1]], temp_vel_0, vel[1], tp, block))
    
   
#spawn blocks
def spawn_block():
    global y_vel, distance, last_distance, distance_diff_ini, distance_diff, last_spawned_block
    distance += y_vel * 1 / 60.0
    last_distance += y_vel * 1 / 60.0
    temp_dis = -random.randrange(distance_diff_ini, distance_diff)
    if last_distance <= temp_dis:
        pos0 = random.randrange(block_width / 2, width + 1 - block_width / 2)
        pos1 = block_height / 2 + height
        y_vel = -1 + distance * block_vel_inc
        if y_vel < -5.0:
            y_vel = -5.0
        x_vel = 0
        if distance < -10.0:
            temp1 = random.randrange(0,5)
            if temp1 == 0:
                temp_x_vel = random.randrange(0,10)
                x_vel = temp_x_vel / 10.0
                temp_sign = random.randrange(0,2)
                if temp_sign:
                    x_vel = - x_vel
        else:
            x_vel = 0
        if last_spawned_block == "break":
            temp = random.randrange(1,6)
            if temp == 1:
                tp = "spike"
            elif temp == 2:
                tp = "normal"
            elif temp == 3:
                tp = "spring"
            elif temp == 4:
                tp = "left_block"
            elif temp == 5:
                tp = "right_block"
        else:  
            temp = random.randrange(1,7)
            if temp == 1:
                tp = "spike"
            elif temp == 2:
                tp = "normal"
            elif temp == 3:
                tp = "spring"
            elif temp == 4:
                tp = "break"
            elif temp == 5:
                tp = "left_block"
            elif temp == 6:
                tp = "right_block"
        y_vel_copy = float(y_vel)
        ablock = block([pos0, pos1], x_vel, y_vel_copy, tp)
        block_set.add(ablock)
        last_spawned_block = tp
        temp = random.randrange(0,5)
        if temp < 3:
            spawn_sprite(ablock)
        
        
        last_distance = 0
    
# draw handler
def draw(canvas):
    global distance, score, score2, bonus, bonus2, s500, s1000, s5000, s10000
    
    
    if in_play:
        canvas.draw_image(background_image, [width / 2, height / 2], [width, height], [width / 2, height / 2], [width, height])
 
        you.update()
        you.draw(canvas)
        if mode == 1 and 450 < (bonus + score) < 500 and not s500:
            message_set.add(message("A good start!", [message_center_pos[0], 200], 30, "#FFFFFF", 30, "serif", 1))
            s500 = 1
        if mode == 1 and 900 < (bonus + score) < 1000 and not s1000:
            message_set.add(message("Good!", [message_center_pos[0] + 20, 200], 30, "#FFFFFF", 30, "serif", 1))
            s1000 = 1
        if mode == 1 and 4500 < (bonus + score) < 5000 and not s5000:
            message_set.add(message("Awesome!", [message_center_pos[0], 200], 30, "#FFFFFF", 30, "serif", 1))
            s5000 = 1
        if mode == 1 and 9500 < (bonus + score) < 10000 and not s10000:
            message_set.add(message("Marvellous!", [message_center_pos[0], 200], 30, "#FFFFFF", 30, "serif", 1))
            s10000 = 1
        if mode == 2:
            you2.update()
            you2.draw(canvas)
        spawn_block()
        check_remove_block(block_set)
        check_remove_sprite(sprite_set)
        check_remove_explosion(explosion_group)
        
        for ablock in block_set:
            ablock.update()
            ablock.draw(canvas)
        for asprite in sprite_set:
            asprite.update()
            asprite.draw(canvas)
        for aexplosion in explosion_group:
            aexplosion.update()
            aexplosion.draw(canvas)
        if not you_game_over:
            score = - int (distance * 100)
        if not you2_game_over:
            score2 = - int (distance * 100)
        
        if mode == 2:
            if you_game_over == 0 and you2_game_over == 1:
                if (score + bonus) > (score2 + bonus2):
                    game_over("type")
            elif you_game_over == 1 and you2_game_over == 0:
                if (score + bonus) < (score2 + bonus2):
                    game_over("type")
            
            
    else:
        canvas.draw_image(background_image, [width / 2, height / 2], [width, height], [width / 2, height / 2], [width, height])

        if not initial_play and mode == 1:
            high = 1
            for ascore in scores:
                if int(score + bonus) < ascore:
                    high = 0
                if int(score2 + bonus2) < ascore:
                    high = 0
            if high and not display_how_to and not display_high_score:
                canvas.draw_text("High score!", (width - 370, height / 2 + 10), 30, 'orange', 'serif')
        
        if display_high_score:
            if runs == 0:
                canvas.draw_text("No scores yet", (width - 370, height / 2), 30, 'red', 'serif')
            if runs >= 1:
                canvas.draw_text(str(scr.return_1_score(scr.get_scores())[0]) + ": " + str(scr.return_1_score(scr.get_scores())[1]), (width - 390, height / 2), 30, 'red', 'serif')
            if runs >= 2:
                canvas.draw_text(str(scr.return_2_score(scr.get_scores())[0]) + ": " + str(scr.return_2_score(scr.get_scores())[1]), (width - 390, height / 2 + 50), 30, 'red', 'serif')
            if runs >= 3:
                canvas.draw_text(str(scr.return_3_score(scr.get_scores())[0]) + ": " + str(scr.return_3_score(scr.get_scores())[1]), (width - 390, height / 2 + 100), 30, 'red', 'serif')
            
        if not initial_play and display_how_to_button:
            canvas.draw_image(how_to_button_image, how_to_button_info.get_center(),
                        how_to_button_info.get_size(),
                        [width / 2, height - 150],
                        how_to_button_info.get_size())
            
        if not initial_play and display_high_score_button:
            canvas.draw_image(high_score_button_image, high_score_button_info.get_center(),
                        high_score_button_info.get_size(),
                        [width / 2, height - 200],
                        high_score_button_info.get_size())
            
        if display_mode_selection:
            canvas.draw_image(p1_mode_image, p1_mode_info.get_center(),
                        p1_mode_info.get_size(),
                        [width / 2 - 120, height - 100],
                        p1_mode_info.get_size())
            
            canvas.draw_image(p2_mode_image, p2_mode_info.get_center(),
                        p2_mode_info.get_size(),
                        [width / 2 + 120, height - 100],
                        p2_mode_info.get_size())
            

        
    if initial_play and not in_play:
        if display_intro:
            canvas.draw_image(intro_image, intro_info.get_center(),
                            intro_info.get_size(),
                            [width / 2, height / 2 - 30 ],
                            intro_info.get_size())
            
        if display_how_to_button:
            canvas.draw_image(how_to_button_image, how_to_button_info.get_center(),
                        how_to_button_info.get_size(),
                        [width / 2, height - 150],
                        how_to_button_info.get_size())
            
        if display_high_score_button:
            canvas.draw_image(high_score_button_image, high_score_button_info.get_center(),
                        high_score_button_info.get_size(),
                        [width / 2, height - 200],
                        high_score_button_info.get_size())
            
        if display_mode_selection:
            canvas.draw_image(p1_mode_image, p1_mode_info.get_center(),
                        p1_mode_info.get_size(),
                        [width / 2 - 120, height - 100],
                        p1_mode_info.get_size())
            
            canvas.draw_image(p2_mode_image, p2_mode_info.get_center(),
                        p2_mode_info.get_size(),
                        [width / 2 + 120, height - 100],
                        p2_mode_info.get_size())
            
        if display_start:
            canvas.draw_image(start_image, start_info.get_center(),
                      start_info.get_size(),
                      [width / 2, height - 100],
                      start_info.get_size())
    
    #draw split line
    canvas.draw_line([width, 0], [width, height], 5, "gray")
    canvas.draw_polygon([[width,0], [canvas_width, 0], [canvas_width, height], [width, height]], 1, "black", "black")
    
    #draw score
    
    canvas.draw_text("P1 Score: " + str(score + bonus), (canvas_width - 170, 130), 25, 'gold', 'serif')
    if mode == 2:
        canvas.draw_text("P2 Score: " + str(score2 + bonus2), (canvas_width - 170, 160), 25, 'gold', 'serif')
        
    if in_play:
        canvas.draw_text("P1 Health:", [width + 20, 20], 20, "yellow")
        health_width = you.get_health() / 10.0 * 170
        health_width2 = you2.get_health() / 10.0 * 170
        canvas.draw_line([width + 20, 40], [width + 20 + health_width, 40], 20, "red")
        if mode == 2:
            canvas.draw_text("P2 Health:", [width + 20, 70], 20, "yellow")
            canvas.draw_line([width + 20, 90], [width + 20 + health_width2, 90], 20, "red")
    
    for amessage in message_set:
        amessage.update()
        amessage.draw(canvas) 
    
    check_remove_message(message_set)
    
    if game_over_state:
        if mode == 1:
            if 0 <= int(score + bonus) <= 500 and not display_how_to and not display_high_score:
                canvas.draw_text("Oops. Just try again.", (width / 2 - 120, height / 2 - 30), 30, 'gold', 'serif')
            if 501 <= int(score + bonus) <= 1000 and not display_how_to and not display_high_score:
                canvas.draw_text("You can do better!", (width / 2 - 110, height / 2 - 30), 30, 'gold', 'serif')
            if 1001 <= int(score + bonus) <= 5000 and not display_how_to and not display_high_score:
                canvas.draw_text("You got it! Have another try.", (width / 2 - 160, height / 2 - 30), 30, 'gold', 'serif')
            if 5001 <= int(score + bonus) <= 10000 and not display_how_to and not display_high_score:
                canvas.draw_text("Awesome!", (width / 2 - 55, height / 2 - 30), 30, 'gold', 'serif')
            if int(score + bonus) > 10000 and not display_how_to and not display_high_score:
                canvas.draw_text("Marvellous!", (width / 2 - 60, height / 2 - 30), 30, 'gold', 'serif')
        
        if not display_how_to and not display_high_score:
            if mode == 1:
                canvas.draw_text("P1 score: " + str(int(score + bonus)), (width / 2 - 80, height / 2 - 70), 30, 'gold', 'serif')
            if mode == 2:
                canvas.draw_text("P1 vs P2:  " + str(p1_win) + ":" + str(p2_win), (width / 2 - 80, height / 2 - 40), 30, 'gold', 'serif')
    
    #draw top spike
    canvas.draw_image(spike_top_image, spike_top_info.get_center(),
                      spike_top_info.get_size(),
                      spike_top_info.get_center(),
                      spike_top_info.get_size())
    #draw lamps
    canvas.draw_image(lamp_image, lamp_info.get_center(),
                      lamp_info.get_size(),
                      [34,50],
                      lamp_info.get_size())
    
    canvas.draw_image(lamp_image, lamp_info.get_center(),
                      lamp_info.get_size(),
                      [width - 33,50],
                      lamp_info.get_size())
    
    if display_how_to:
        canvas.draw_image(how_to_image, how_to_info.get_center(),
                          how_to_info.get_size(),
                          [width / 2, height / 2 - 30 ],
                          how_to_info.get_size())
        
    
        
#game over screen
def game_over(typ):
    global distance, p1_win, p2_win, display, last_distance, display_mode_selection, display_start, game_over_tp, display_high_score, runs, scr, y_vel, in_play, display_high_score_button, restart_state, game_over_state, scores, score, display_how_to_button
    display = 0
    display_start = 0
    display_mode_selection = 1
    if (score + bonus) > (score2 + bonus2) and mode == 2:
        message_set.add(message(str(name) + " wins!", (width / 2 - 80, height / 2 + 50), 30, "#FFFFFF", 30, "serif", 1))
        p1_win += 1
    elif (score + bonus) < (score2 + bonus2) and mode == 2:
        message_set.add(message(str(name2) + " wins!", (width / 2 - 80, height / 2 + 50), 30, "#FFFFFF", 30, "serif", 1))
        p2_win += 1
    elif mode == 2:
        message_set.add(message("Tie", (width / 2 , height / 2 + 50), 30, "#FFFFFF", 30, "serif", 1))
    if game_over_state != 1:
        scores.add(int(score + bonus))
        scr.add(int(score + bonus), name)
        runs += 1
        if mode == 2:
            scr.add(int(score2 + bonus2), name2)
    game_over_state = 1
    last_distance = 0
    display_high_score_button = 1
    y_vel = -1.0
    in_play = 0
    restart_state = 1
    display_how_to_button = 1
    
    display_high_score = 0
    if mode == 1:
        if typ == "fall":
            game_over_tp = "You fell off the blocks"
        elif typ == "crush":
            game_over_tp = "You crushed your head"
        elif typ == "health":
            game_over_tp = "You ran out of health"
        
#input handler
def input_handler(text):
    global name
    name = text

def input_handler2(text):
    global name2
    name2 = text
    
#timer handler
def tick():
    global display
    timer.stop()
    display = 0

def tick_break():
    global break_time, break_block, you_break, you2_break, break_set
    
    copy_set = set(break_set)
    for item in copy_set:
        if item[1] < 5:
            break_set.add((item[0], item[1] + 1))
            break_set.remove(item)
        elif item[1] == 5:
            for sprite in sprite_set:
                if sprite.get_block() == item[0]:
                    sprite.set_fall()
            if you.get_block() == item[0]:
                you.remove_block()
            if you2.get_block() == item[0] and mode == 2:
                you2.remove_block()
            flag = 0
            for block in block_set:
                if block == item[0]:
                    flag = 1
            if flag:
                block_set.remove(item[0])
            break_set.remove(item)
          

def tick_explosion():
    global explosion_time, you_explode, you2_explode
    if explosion_time == 0:
        explosion_time += 1
    elif explosion_time == 1:
        timer_explosion.stop()
        if you_explode:
            if mode == 2 and you.get_block() == you2.get_block():
                you2.set_fall()
            you.explode()
            you_explode = 0
            check_remove_explosion_block(you.get_pos())
        if you2_explode and mode == 2:
            if you.get_block() == you2.get_block():
                you.set_fall()
            you2.explode()
            you2_explode = 0
            check_remove_explosion_block(you2.get_pos())
        explosion_sound.rewind()
        explosion_sound.play()

        for sprite in sprite_set:
            sprite.set_fall()
        explosion_time = 0
        
def respawn_zombie(block, vel):
    temp_pos = random.randrange(0, 65)
    temp_sign = random.randrange(0,2)
    if temp_sign:
        temp_pos = - temp_pos
        sprite_set.add(sprite([block.get_pos()[0] + temp_pos, block.get_pos()[1] + block_height / 2 - 12], vel, block.get_vel()[1], "zombie", block))

def tick_zombie():
    global respawn_zombie_set
    copy_set = set(respawn_zombie_set)
    for everything in copy_set:
        if everything[2] >= 2:
            respawn_zombie(everything[0], everything[1])
            respawn_zombie_set.remove(everything)
        else:
            respawn_zombie_set.add((everything[0], everything[1], everything[2] + 1))
            respawn_zombie_set.remove(everything)
            
def replay():
    background_music.rewind()
    background_music.play()

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("The descent", canvas_width, canvas_height)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_keydown_handler(keydn)
frame.set_keyup_handler(keyup)
inp = frame.add_input('Player 1 name: (press Enter):', input_handler, 150)
inp2 = frame.add_input('Player 2 name (press Enter):', input_handler2, 150)
timer = simplegui.create_timer(1000, tick)
timer2 = simplegui.create_timer(100, tick_break)
timer_explosion = simplegui.create_timer(100, tick_explosion)
timer_zombie = simplegui.create_timer(100, tick_zombie)
timer_background = simplegui.create_timer(13000, replay)
timer_background.start()
background_music.set_volume(0.4)
background_music.rewind()
background_music.play()

# Start the frame animation
frame.start()

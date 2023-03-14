from ursina import *

block_pick_global = 1
grass_texture = None
stone_texture = None
brick_texture = None
dirt_texture = None
punch_sound = None
# texture_block_pick = None


# 更新创建方式
def update_block_pick(block_pick):
    global block_pick_global
    block_pick_global = block_pick


# 加载对应的texture
def load_block_texture():
    global grass_texture, stone_texture, brick_texture, dirt_texture
    global punch_sound
    grass_texture = load_texture('assets/grass_block.png')
    stone_texture = load_texture('assets/stone_block.png')
    brick_texture = load_texture('assets/brick_block.png')
    dirt_texture = load_texture('assets/dirt_block.png')
    punch_sound = Audio('assets/punch_sound.wav', loop=False, autoplay=False)


# 默认创建草坪方块
class Block(Button):
    def __init__(self, position=(0, 0, 0), texture_block=grass_texture):
        global grass_texture
        self.texture_block = grass_texture
        # self.texture_block = texture_block
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',             # 模型使用立方体
            origin_y=0.5,
            texture=texture_block,   # 显示内容
            color=color.color(0, 0, random.uniform(0.9, 1)),  # 利用RGB生成不同颜色的方块
            # highlight_color=color.green,  # 触碰到立方体为白色
            scale=0.5
        )

    def input(self, key):
        global grass_texture, stone_texture, brick_texture, dirt_texture
        global block_pick_global
        if self.hovered:
            # 左键，朝鼠标指向方向创建方块
            if key == 'left mouse down':
                punch_sound.play()
                # if held_keys['1']: block = Block(position=self.position + mouse.normal, texture_block=grass_texture)
                # if held_keys['2']: block = Block(position=self.position + mouse.normal, texture_block=stone_texture)
                # if held_keys['3']: block = Block(position=self.position + mouse.normal, texture_block=brick_texture)
                # if held_keys['4']: block = Block(position=self.position + mouse.normal, texture_block=dirt_texture)
                if block_pick_global == 1: block = Block(position=self.position + mouse.normal, texture_block=grass_texture)
                if block_pick_global == 2: block = Block(position=self.position + mouse.normal, texture_block=stone_texture)
                if block_pick_global == 3: block = Block(position=self.position + mouse.normal, texture_block=brick_texture)
                if block_pick_global == 4: block = Block(position=self.position + mouse.normal, texture_block=dirt_texture)

                # block = Block(position=self.position + mouse.normal, texture_block=self.texture_block)
            # 右键， 摧毁方块
            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)


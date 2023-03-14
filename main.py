from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# import block
import block
from block import *
from sky import *
from hand import *


class Sky(Entity):
    def __init__(self, texture_sky=None):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=texture_sky,
            scale=random.randrange(200,300),
            double_sided=True
        )


app = Ursina()


window.fps_counter.enabled = False  # 隐藏屏幕右上角的帧数
window.exit_button.visible = False  # 沉浸式感觉

block_pick = 1

# 应该删掉，暂时存在bug
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')

punch_sound = Audio('assets/punch_sound.wav', loop=False, autoplay=False)

sky_texture = load_texture('assets/skybox.png')

# 将加载到的texture放在block文件
# 注意加载过程必须在app = Ursina()后面
load_block_texture()






# held_keys
# 该函数会被自动调用， ursina的机制
# 页面每次刷新，调用该函数
def update():
    # 生成方块类型选择
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    update_block_pick(block_pick)

    # 手的动画实现
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

# 生成指定数量和位置的模块， 8*1*8
for z in range(8):
    for x in range(8):
        block = Block(position=(x, 0, z), texture_block=grass_texture)

player = FirstPersonController()

hand = Hand()
sky = Sky(texture_sky=sky_texture)


app.run()
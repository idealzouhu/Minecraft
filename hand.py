from ursina import *


class Hand(Entity):
    def __init__(self):
        hand_texture = load_texture('assets/arm_texture.png')
        super().__init__(
            parent=camera.ui,     # 手的特殊设置, 表示显示方式
            model='assets/arm',   # 使用自己制作的模型
            texture=hand_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6),
            double_sided=True  # 表示球体的两面都显示sky_texture
        )

    # 手动的时候，简单地移动， 实现动画效果
    def active(self):
        self.position = Vec2(0.3, -0.5)

    # 手不动的时候，回到初始位置
    def passive(self):
        self.position = Vec2(0.4, -0.6)
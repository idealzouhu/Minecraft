# from ursina import *
#
#
# class Sky(Entity):
#     def __init__(self, texture_sky=None):
#         super().__init__(
#             parent=scene,
#             model='sphere',
#             texture=texture_sky,
#             scale=random.randrange(200,300),
#             double_sided=True
#         )

# class Sky(Entity):
#     def __init__(self):
#         sky_texture = load_texture('assets/skybox.png')
#         super().__init__(
#             parent=scene,
#             model='sphere',  # 球体
#             texture=sky_texture,
#             scale=100,
#             double_sided=True,  # 表示球体的两面都显示sky_texture
#             position=(0, 0, 0)
#         )

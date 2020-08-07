# blender --background --python 12_cloth.py --render-anim -- </path/to/output/directory>/<name> <resolution_percentage> <num_samples>
# ffmpeg -r 24 -i </path/to/output/directory>/<name>%04d.png -pix_fmt yuv420p out.mp4

import bpy
import sys
import math
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/foolyc/workspace/blender-cli-rendering")
import utils
import external.cc0assetsloader as loader



# Scene Building
scene = bpy.data.scenes["Scene"]
world = scene.world

cloth_object = bpy.data.objects['cloth']
cloth_object.rotation_euler[2] = 0
# utils.set_animation(scene, fps=24, frame_start=1, frame_end=48)


camera_object = bpy.data.objects['Camera']


# change state
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.object.mode_set(mode='OBJECT')

cloth_object.vertex_groups.new(name="g0")
# add vertex to group, must be object mode
cloth_object.vertex_groups["g0"].add([0], 1.0, 'ADD')


bpy.context.scene.render.filepath = "/home/foolyc/"

scene.frame_set(50)
bpy.context.scene.render.filepath = "/home/foolyc/1.png"
bpy.ops.render.render(write_still=True)
# bpy.ops.render.render(animation=True, write_still=True)
# bpy.ops.render.play_rendered_anim()
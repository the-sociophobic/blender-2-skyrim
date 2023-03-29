# Copy this code into Blender Scripting console. Run
import bpy

for i in bpy.data.images:
    i.filepath = i.filepath.replace('.dds', '.png')
    i.name = i.name.replace('.dds', '.png')
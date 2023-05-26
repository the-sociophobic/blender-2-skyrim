from collections import defaultdict
import bpy
context = bpy.context
ob = context.object

me = ob.data
slots = ob.material_slots
def getmname(idx):
    if idx < len(slots):
        name = slots[idx].name
        name = name if name else "None"
    else:
        name = "None"
    return name
    
matdic = defaultdict(list)

for f in me.polygons:
    matdic[getmname(f.material_index)].append(f.index)
    

while len(slots) > len(matdic):
    ob.active_material_index = 1
    bpy.ops.object.material_slot_remove()
    
while len(slots) < len(matdic):
    bpy.ops.object.material_slot_add()
for i, (name, faces) in enumerate(matdic.items()):
    slots[i].material = bpy.data.materials.get(name)
    for f in faces:
        me.polygons[f].material_index = i
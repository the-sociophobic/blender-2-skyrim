from os import walk
from wand import image

# relative path to the folder with .dds textures
mypath = ['./textures']

f = []
for (path) in mypath:
  for (dirpath, dirnames, filenames) in walk(path):
      mypath.extend(map(lambda dirname: dirpath + '/' + dirname, dirnames))
      f.extend(map(lambda filename: (filename, dirpath), filenames))
      break

for file in f:
  if file[0].endswith('.dds'):
    try:
      new_filename = file[0][0:-3] + 'png'
      with image.Image(filename = file[1] + '/' + file[0]) as img:
        img.compression = "no"
        img.save(filename = file[1] + '/' + new_filename)
      print(file)
    except Exception:
      print('failed ' + file[0])

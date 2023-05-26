## Blender2Skyrim

This is a toolset for extracting Skyrim models. Extracting Skyrim models using Blender most of the time. Blender. Not some poorly-updated-funmade-toolset.

1. Get Skyrim original installation on Windows PC
2. Downlad [Bethesda Archive Extractor](https://www.nexusmods.com/fallout4/mods/78/?tab=files) from NexusMods
3. Use it to unarchive folders: textures, meshes
4. Move extracted folders to this project folder (from now on you no longer need Windiws. Use any python-runnable device)
5. Install freetype ImageMagick. i.e. with brew for MacOS:

```
brew install freetype ImageMagick
```

6. Open create-pngs.py. Specify which folders you want to use. i.e. ['./textures/armor', './textures/terrain']. Save

```
python3 create-pngs.py
```

7. Install [Blender niftools addon](https://github.com/niftools/blender_niftools_addon/releases)
8. Blender → File → Import → .nif. Open smth from project/meshes
9. Copy relink-textures.py into Blender Scripting console. Run
10. File → External Data → ✅ Automatically Pack Resources

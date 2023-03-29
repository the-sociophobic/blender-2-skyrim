## Blender2Skyrim

This is a toolset for extracting Skyrim models. Extracting Skyrim models using Blender most of the time. Blender and not some 2-commits-per-year-funmade-toolset.

1. Get Skyrim original installation on Windows PC
2. Downlad nexusmods.com/fallout4/mods/78/?tab=files
3. Use it to unarchive textures and meshes folders
4. Move extracted folders to your project folder
5. Run create-pngs.py

### python3 create-pngs.py

7. Open Blender
8. Install github.com/niftools/blender_niftools_addon/releases to Blender
9. File → Import → .nif. Open smth from project/meshes
10. Copy relink-textures.py into Blender Scripting console. Run

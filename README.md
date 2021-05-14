# Load Obj Sequence as Shape Keys
Blender Script.

## Description
This script loads set of OBJ files as shape keys of the active object. Each created shape key's name will be the same as the OBJ files'.

This script is originally made by cmomoney at ["Merging multiple OBJ files into one file with shape keys"](https://blender.stackexchange.com/questions/58147/merging-multiple-obj-files-into-one-file-with-shape-keys), and I fixed bugs of it and changed a little.

What I (@konoha18537007) changed is below :
  - Fixed several bugs of logic on deleting imported objs,
  - Changed to use annotation for declaring member valiables,
  - Changed to use blend file's path for the file IO dialog's default path.

## Usage
1. Select the target object.

2. Run this script by "File" > "Import" > "Obj As Shapekey(.obj)".

## Installation
Edit > Preferences > Add-ons > Install... and select Load_Obj_Sequence_as_Shape_Keys.py

## Notice
* If a shape key with the same name already exists on the target object, a shape key with the name like 'foo.001' will be added (not over written).

## License
* As the original script was published at blender Stack Exchange, this script is also distributed under the terms of [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
  - [blender Stack Exchange license](https://blender.stackexchange.com/help/licensing)
 

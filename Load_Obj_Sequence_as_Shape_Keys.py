bl_info = {
    'name': 'Load Obj Sequence as Shape Keys',
    'author': 'cmomoney',
    'version': (0, 2),
    'blender': (2, 80, 0),
    'category': 'Import-Export',
    'location': 'File > Import',
    'wiki_url': ''}

#######################################################################
# License : 
# CC BY-SA 4.0.
# https://blender.stackexchange.com/help/licensing
# https://creativecommons.org/licenses/by-sa/4.0/

# This addon is originally made by cmomoney.
# https://blender.stackexchange.com/questions/58147/merging-multiple-obj-files-into-one-file-with-shape-keys
#
# What I (@konoha18537007) changed : 
#  - Fixed bugs of logic on deleting the imported objs.
#  - Changed to use annotation for declaring member valiables.
#  - Changed to use blend file's path for the file IO dialog's default path.
#######################################################################


import bpy, os
from bpy.props import *

class LoadObjAsShapekey(bpy.types.Operator):
    bl_idname = 'load.obj_as_shapekey'
    bl_label = 'Import OBJ as Shape Keys'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Import Obj sequence as shape key(s)"

    filepath : StringProperty(name="File path", description="File filepath of Obj", maxlen=4096, default="")
    filter_folder : BoolProperty(name="Filter folders", description="", default=True, options={'HIDDEN'})
    filter_glob : StringProperty(default="*.obj", options={'HIDDEN'})
    files : CollectionProperty(name='File path', type=bpy.types.OperatorFileListElement)
    filename_ext = '.obj'

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        # self.filepath : the file's absolute path selected at the last in the IO dialog
        # self.files    : list of selected files ( [bpy.types.OperatorFileListElement]

        _dir = os.path.split(self.filepath)[0]
        files = [file.name for file in self.files] # selected file names without dir path
        files.sort()

        # add all ojs in sequence as shape keys
        o = bpy.context.active_object
        imported_objs = [] # list of imported obj name
        for f in files:
            objs_pre = list(bpy.data.objects.keys())

            if o.data.shape_keys is None:
                sks_pre = []
            else:
                sks_pre = list(o.data.shape_keys.key_blocks)

            # obj import
            bpy.ops.import_scene.obj(filepath=os.path.join(_dir, f),split_mode='OFF') # split_mode='OFF' : keep vertex order
            if len(bpy.data.objects.keys()) > len(objs_pre):
                bpy.ops.object.join_shapes()
                imported_objs.append(list(set(bpy.data.objects.keys()) - set(objs_pre))[0])
            else:
                # obj import error
                continue

            if len(o.data.shape_keys.key_blocks) > len(sks_pre):
                o.data.shape_keys.key_blocks[-1].interpolation = 'KEY_LINEAR'                

        # delete objs
        bpy.ops.object.select_all(action='DESELECT')
        for imported_obj in imported_objs:
            bpy.context.view_layer.objects.active = bpy.data.objects[imported_obj]
            bpy.data.objects[imported_obj].select_set(state=True)
            bpy.ops.object.delete()
            bpy.ops.object.select_all(action='DESELECT')

        # reselect object and make active
        bpy.context.view_layer.objects.active = o
        o.select_set(state=True)
        return{'FINISHED'}

    def invoke(self, context, event):
        self.filepath = os.path.join(os.path.dirname(bpy.data.filepath) ,"")
        wm = context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def menu_func_import(self, context):
    self.layout.operator(LoadObjAsShapekey.bl_idname, text="Obj As Shapekey(.obj)")

def register():
    bpy.utils.register_class(LoadObjAsShapekey)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(LoadObjAsShapekey)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()

import maya.cmds as cmds

selected_joints = cmds.ls(selection=True, type='joint')

if selected_joints:
    for joint in selected_joints:
        cmds.setAttr(joint + ".segmentScaleCompensate", 0)
else:
    print("No joints selected.")
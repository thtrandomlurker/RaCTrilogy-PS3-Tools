import bpy
obj = bpy.context.active_object

names = [
["VertGroup_1", "Pelvis"],
["VertGroup_2", "Spine_1"],
["VertGroup_3", "Spine_2"],
["VertGroup_4", "Spine_3"],
["VertGroup_5", "Spine_4"],
["VertGroup_6", "Spine_5"],
["VertGroup_7", "Neck"],
["VertGroup_8", "Head"],
["VertGroup_41", "L_Ear_1"],
["VertGroup_42", "L_Ear_2"],
["VertGroup_43", "L_Ear_3"],
["VertGroup_44", "R_Ear_1"],
["VertGroup_45", "R_Ear_2"],
["VertGroup_46", "R_Ear_3"],
["VertGroup_52", "R_Shoulder"],
["VertGroup_53", "R_Arm"],
["VertGroup_54", "R_Elbow"],
["VertGroup_55", "R_Wrist"],
["VertGroup_56", "R_Hand"],
["VertGroup_57", "R_Index_1"],
["VertGroup_58", "R_Index_2"],
["VertGroup_59", "R_Index_3"],
["VertGroup_60", "R_Middle_1"],
["VertGroup_61", "R_Middle_2"],
["VertGroup_62", "R_Middle_3"],
["VertGroup_63", "R_Ring_1"],
["VertGroup_64", "R_Ring_2"],
["VertGroup_65", "R_Ring_3"],
["VertGroup_66", "R_Pinky_1"],
["VertGroup_67", "R_Pinky_2"],
["VertGroup_68", "R_Pinky_3"],
["VertGroup_69", "R_Thumb_1"],
["VertGroup_70", "R_Thumb_2"],
["VertGroup_72", "L_Shoulder"],
["VertGroup_73", "L_Arm"],
["VertGroup_74", "L_Elbow"],
["VertGroup_75", "L_Wrist"],
["VertGroup_76", "L_Hand"],
["VertGroup_77", "L_Index_1"],
["VertGroup_78", "L_Index_2"],
["VertGroup_79", "L_Index_3"],
["VertGroup_80", "L_Middle_1"],
["VertGroup_81", "L_Middle_2"],
["VertGroup_82", "L_Middle_3"],
["VertGroup_83", "L_Ring_1"],
["VertGroup_84", "L_Ring_2"],
["VertGroup_85", "L_Ring_3"],
["VertGroup_86", "L_Pinky_1"],
["VertGroup_87", "L_Pinky_2"],
["VertGroup_88", "L_Pinky_3"],
["VertGroup_89", "L_Thumb_1"],
["VertGroup_90", "L_Thumb_2"],
["VertGroup_92", "R_Leg"],
["VertGroup_93", "R_Knee"],
["VertGroup_94", "R_Foot"],
["VertGroup_95", "R_Toe_1"],
["VertGroup_96", "R_Toe_2"],
["VertGroup_97", "R_Toe_3"],
["VertGroup_98", "L_Leg"],
["VertGroup_99", "L_Knee"],
["VertGroup_100", "L_Foot"],
["VertGroup_101", "L_Toe_1"],
["VertGroup_102", "L_Toe_2"],
["VertGroup_103", "L_Toe_3"],
["VertGroup_104", "Tail_1"],
["VertGroup_105", "Tail_2"],
["VertGroup_106", "Tail_3"],
["VertGroup_107", "Tail_4"],
["VertGroup_108", "Tail_5"],
["VertGroup_109", "Tail_6"],
["VertGroup_110", "Tail_7"],
]

for grp, name in names:
    group = obj.vertex_groups.get(grp)
    if group is None:
        continue
    else:
        group.name = name
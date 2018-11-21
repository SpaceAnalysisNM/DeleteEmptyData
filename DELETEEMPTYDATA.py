import arcpy
from arcpy import env
env.workspace = r''
fds = arcpy.ListDatasets("","FEATURE")
for fd in fds:
    fcs = arcpy.ListFeatureClasses("", "", fd)
    for fc in fcs:
        result = int(arcpy.GetCount_management(fc))
        if result == "0":
            print fc
            arcpy.Delete_management(fc)

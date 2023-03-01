# Idea: Copy python code from ArcGIS Pro
# ArcGIS Pro -> Geoprocessing -> Find Tools -> Create Fishnet


import arcpy  # type: ignore

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\LPA\Projects\GeomProject\GeomProject.gdb"
srWGS84 = arcpy.SpatialReference("WGS 1984")

arcpy.management.CreateFishnet(
    "FishnetLines", "0 0", "0 1", 1, 1, 10, 15, None, "LABELS", "DEFAULT", "POLYLINE"
)

if arcpy.Exists("FishnetPoints"):
    arcpy.management.Delete("FishnetPoints")
arcpy.management.Rename("FishnetLines_label", "FishnetPoints")
arcpy.management.CreateFishnet(
    "FishnetPolys", "0 0", "0 1", 1, 1, 4, 6, None, "NO_LABELS", "DEFAULT", "POLYGON"
)

for geomType in ["Polys", "Lines", "Points"]:
    arcpy.management.DefineProjection(f"Fishnet{geomType}", srWGS84)
print("\nScript completed!")

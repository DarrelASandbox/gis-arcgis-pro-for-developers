import arcpy  # type: ignore


def print_msg(msg):
    print(msg)
    arcpy.AddMessage(msg)


arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"01-LPA\Data\Sample.gdb"

fc = arcpy.GetParameterAsText(0)
if fc == "":
    fc = r"01-LPA\Data\ne_10m_admin_0_countries.shp"

# Copy all the countries in the feature shapefile into a `.gdb` with a feature class name "Countries"
arcpy.management.CopyFeatures(fc, "Countries")
numFeats = arcpy.management.GetCount(fc)
print(f"{fc} has {numFeats} number of feature(s).")

arcpy.CreateFileGDB_management(r"01-LPA\Data", "Sample.gdb")
arcpy.analysis.Select(fc, "India", "NAME = 'India'")


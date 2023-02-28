# NOTES:
#   - Pathing may need to hardcore path to drive

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


###########################################################################


arcpy.env.workspace = r"01-LPA"
wsList = arcpy.ListWorkspaces()
gdbListAll = []
for workspace in wsList:
    arcpy.env.workspace = workspace
    gdbList = arcpy.ListWorkspaces("", "FileGDB")
    # print("{0} contains {1}".format(workspace, gdblist))
    gdbListAll += gdbList
print(f"List of file geodatabases:\n{gdbListAll}")


# Listing Workspaces, Feature Datasets and Feature Classes
for gdb in gdbListAll:
    arcpy.env.workspace = gdb
    print(f"\nFeature classes in {gdb}:\n{arcpy.ListFeatureClasses()}")
    print(f"Feature datasets in {gdb}:\n{arcpy.ListDatasets('', 'Feature')}")
    fdList = arcpy.ListDatasets("", "Feature")
    for fd in fdList:
        arcpy.env.workspace = rf"{gdb}\{fd}"
        print(
            f"\nFeatures classess in feature dataset {arcpy.env.workspace}:\n{arcpy.ListFeatureClasses()}"
        )


# Listing Tables
for gdb in gdbListAll:
    arcpy.env.workspace = gdb
    print(f"\nTables in {gdb}:\n{arcpy.ListTables()}")


# Listing Fields
arcpy.env.workspace = r"01-LPA\Data\Sample.gdb"
for tbl in arcpy.ListTAbles():
    fieldObjectList = arcpy.ListFields(tbl)
    fieldNameTypeList = [[x.name, x.type] for x in fieldObjectList]
    print(f"\nFields in {arcpy.env.workspace}\\{tbl}:\n{fieldNameTypeList}")


# `arcpy.da.describe` and `arcpy.describe` are both functions in the ArcPy module of ArcGIS Pro that are used to describe datasets. However, they have some differences in their functionality and the types of datasets they can describe.

# `arcpy.describe` is a general function that can be used to describe a wide range of datasets, including feature classes, tables, rasters, and workspaces. The function returns a Describe object that contains properties such as the data type, spatial reference, and field information. `arcpy.describe` is useful for quickly getting basic information about a dataset.

# On the other hand, `arcpy.da.describe` is a more specialized function that is used specifically to describe feature classes and tables. It returns a Python dictionary containing information about the fields in the dataset, such as their name, data type, and length. `arcpy.da.describe` is useful for working with feature classes and tables in a more granular way, such as when iterating over the fields to perform data analysis or manipulation.

# In summary, `arcpy.describe` is a general function that can describe a wide range of datasets, while `arcpy.da.describe` is a more specialized function for describing feature classes and tables in a more detailed way.


# Path to different file type
dataElement = r"01-LPA\Data\Sample.gdb"


# `arcpy.Describe()`
desc = arcpy.Describe(dataElement)
print(f"Describing {dataElement}:")
print("Name: " + desc.name)
print("DataType: " + desc.dataType)
print("CatalogPath: " + desc.catalogPath)
print("Children:")

for child in desc.children:
    if child.dataType == "FeatureDataset":
        pass
    else:
        if hasattr(child, "shapeType"):
            print(f"{child.name} is a {child.dataType} of shapeType {child.shapeType}")
            print(f"with Extent: {child.extent}")
        else:
            print(f"{child.name} has no shapeType, it is a {child.dataType} type.")

        for field in child.fields:
            print(f"{field.name}, {field.type}")


# `arcpy.da.Describe()`
descDictionary = arcpy.da.Describe(dataElement)
for i, key in enumerate(descDictionary):
    print(f"{i+1}, {key}, {descDictionary[key]}")


###########################################################################


# arcpy.da.Walk()
workspace = r"01-LPA\Data"
dataList = []

for dirpath, dirnames, filenames in arcpy.da.Walk(workspace):
# for dirpath, dirnames, filenames in arcpy.da.Walk(
#     workspace, datatype="FeatureClass", type=["Point", "Polyline"]
# ):
# for dirpath, dirnames, filenames in arcpy.da.Walk(
#     workspace,datatype="RasterDataset",type=["JPG","PNG","TIF"]):
    for filename in filenames:
        dataList.append(rf"{dirpath}\{filename}")

print(dataList)
print(f"\nFound data elements in {workspace}")
print("\nScript completed!")


###########################################################################

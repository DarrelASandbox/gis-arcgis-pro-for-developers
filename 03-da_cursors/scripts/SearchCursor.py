import arcpy


shp = r"C:\LPA\Data\ne_10m_admin_0_countries.shp"
print([field.name for field in arcpy.ListFields(shp)])

with arcpy.da.SearchCursor(shp, ["NAME", "CONTINENT", "POP_EST"], "FID < 10") as cursor:
    for row in cursor:
        print(f"{row[2]} people in {row[0]}")


###########################################################################


with arcpy.da.SearchCursor(
    shp, ["NAME", "SHAPE@XY", "SHAPE@AREA", "SHAPE@LENGTH", "SHAPE@"], "FID < 10"
) as cursor:
    for row in cursor:
        print(f"Centroid of {row[0]} is at {row[1]}")
        print(f"its area is {row[2]} and its perimeter is {row[3]}")
        print(f"and it has {row[4].partCount} polygon(s)")
        print(f"with a total of {row[4].pointCount} vertices")

###########################################################################


countryContinentList = [
    [row[0], row[1]]
    for row in arcpy.da.SearchCursor(shp, ["NAME", "CONTINENT"], "FID < 10")
]
print(countryContinentList)
print(countryContinentList[2])
print(countryContinentList[2][1])


###########################################################################


fidCountryDict = {}
with arcpy.da.SearchCursor(shp, ["FID", "NAME"], "FID < 10") as cursor:
    for row in cursor:
        fidCountryDict[row[0]] = row[1]
fidCountryDict = {
    row[0]: row[1] for row in arcpy.da.SearchCursor(shp, ["FID", "NAME"], "FID < 10")
}
print(fidCountryDict)
print(fidCountryDict[4])

fid3FieldsDict = {
    row[0]: [row[1], row[2], f"{row[3]:,}"]
    for row in arcpy.da.SearchCursor(
        shp, ["FID", "NAME", "CONTINENT", "POP_EST"], "FID < 10"
    )
}
print(fid3FieldsDict)
print(fid3FieldsDict[4])
print(fid3FieldsDict[4][2])

print("\nScript completed!")

import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\LPA\Projects\GeomProject\GeomProject.gdb"

geomList = arcpy.CopyFeatures_management("FishnetPolys", arcpy.Geometry())
area = 0.0
for geom in geomList:
    if area == 0.0:
        sr = geom.spatialReference
    area += geom.area
print("Total area: {area}")
print("Spatial Reference: {sr.name}")

pt = arcpy.Point(2.5, 1.75)
ptGeom = arcpy.PointGeometry(pt, sr)
pt2 = arcpy.Point(7.5, 1.25)
ptGeom2 = arcpy.PointGeometry(pt2, sr)
pt3 = arcpy.Point(2.75, 1.5)
ptGeom3 = arcpy.PointGeometry(pt3, sr)
arcpy.CopyFeatures_management([ptGeom, ptGeom2, ptGeom3], "PtGeom")

coordLists = [
    [(1.1, 2.4), (4.9, 2.6), (3.2, 7.3)],
    [(6.1, 8.8), (5.2, 7.6), (7.1, 2.3), (9.1, 5.3)],
]

multiPtGeom = []
for coordList in coordLists:
    multiPtGeom.append(
        arcpy.Multipoint(
            arcpy.Array([arcpy.Point(*coords) for coords in coordList]), sr
        )
    )

arcpy.CopyFeatures_management(multiPtGeom, "MultiPtGeom")


polylineGeom = []
for coordList in coordLists:
    polylineGeom.append(
        arcpy.Polyline(arcpy.Array([arcpy.Point(*coords) for coords in coordList]), sr)
    )
arcpy.CopyFeatures_management(polylineGeom, "PolylineGeom")

polygonGeom = []
for coordList in coordLists:
    polygonGeom.append(
        arcpy.Polygon(arcpy.Array([arcpy.Point(*coords) for coords in coordList]), sr)
    )
arcpy.CopyFeatures_management(polygonGeom, "PolygonGeom")

arrayList = []
for coordList in coordLists:
    arrayList.append(arcpy.Array([arcpy.Point(*coords) for coords in coordList]))
multiPartPolyGeom = arcpy.Polygon(arcpy.Array(arrayList), sr)
arcpy.CopyFeatures_management(multiPartPolyGeom, "MultiPartPolyGeom")

arrayList = []
for coordList in coordLists:
    arrayList.append(arcpy.Array([arcpy.Point(*coords) for coords in coordList]))
multiPartLineGeom = arcpy.Polyline(arcpy.Array(arrayList), sr)
arcpy.CopyFeatures_management(multiPartLineGeom, "MultiPartLineGeom")

bufferGeom = multiPartLineGeom.buffer(0.5)
arcpy.CopyFeatures_management(bufferGeom, "BufferGeom")

convexHullGeom = multiPartPolyGeom.convexHull()
arcpy.CopyFeatures_management(convexHullGeom, "ConvexHullGeom")

circleCenter = arcpy.Point(5, 3)
circleCenterGeom = arcpy.PointGeometry(circleCenter, sr)

print(f"Distance from 2.5,1.75 to 5,3 is {ptGeom.distanceTo(circleCenterGeom)}")

circleGeom = circleCenterGeom.buffer(3)
arcpy.CopyFeatures_management(circleGeom, "CircleGeom")

intersectGeom = circleGeom.intersect(multiPartPolyGeom, 4)
arcpy.CopyFeatures_management(intersectGeom, "IntersectGeom")

intersectGeomList = []
for i in range(0, intersectGeom.partCount):
    intersectGeomList.append(arcpy.Polygon(arcpy.Array(intersectGeom.getPart(i)), sr))
arcpy.CopyFeatures_management(intersectGeomList, "IntersectSinglePartGeom")

print("\nScript completed!")

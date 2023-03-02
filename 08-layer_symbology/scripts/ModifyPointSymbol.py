import arcpy

aprx = arcpy.mp.ArcGISProject(r"C:\LPA\Projects\SymbologyProject\SymbologyProject.aprx")
mapx = aprx.listMaps("Map")[0]
lyr = mapx.listLayers("State Capitals")[0]

sym = lyr.symbology
sym.renderer.symbol.applySymbolFromGallery("Airport")
sym.renderer.symbol.color = {'RGB' : [255, 0, 0, 75]}
sym.renderer.symbol.size = 20
sym.renderer.symbol.angle = 45
lyr.symbology = sym
aprx.save()

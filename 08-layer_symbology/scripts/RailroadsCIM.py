import arcpy

aprx = arcpy.mp.ArcGISProject(r"C:\LPA\Projects\SymbologyProject\SymbologyProject.aprx")
mapx = aprx.listMaps("Map")[0]
lyrx = mapx.listLayers("Railroads")[0]

cim_def = lyrx.getDefinition("V2")

shapeMarkerSymLyr = cim_def.renderer.symbol.symbol.symbolLayers[0]
solidStrokeSymLyr = cim_def.renderer.symbol.symbol.symbolLayers[1]

solidStrokeSymLyr.color.values = [0,0,0,100]
solidStrokeSymLyr.width = 2

lineMarkerSymLyr = shapeMarkerSymLyr.markerGraphics[0].symbol.symbolLayers[0]
lineMarkerSymLyr.color.values = [0,0,0,100]
lineMarkerSymLyr.width = 1

shapeMarkerSymLyr.size = 10
shapeMarkerSymLyr.markerPlacement.placementTemplate = [7.5,25]

lyrx.setDefinition(cim_def)
aprx.save()


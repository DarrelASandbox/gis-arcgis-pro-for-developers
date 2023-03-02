import arcpy,os

arcpy.env.overwriteOutput = True

# Project object
aprx = arcpy.mp.ArcGISProject(
    r"C:\LPA\Projects\MapSeriesProject\MapSeriesProject.aprx")

# Map objects
mainMap = aprx.listMaps("Main Map")[0]
overviewMap = aprx.listMaps("Overview Map")[0]

# Layer objects
countriesLayer = mainMap.listLayers("Countries")[0]

# Layout object
lyt = aprx.listLayouts()[0]

# Map Frame objects
mainMapFrame = lyt.listElements('MAPFRAME_ELEMENT',"Main Map Frame")[0]
overviewMapFrame = lyt.listElements('MAPFRAME_ELEMENT',"Overview Map Frame")[0]

# Set what to zoom to, zoom to it and then zoom out by 5%
countriesLayer.definitionQuery = "NAME = 'Austria'"
selCountryExtent = mainMapFrame.getLayerExtent(countriesLayer)
mainMapFrame.camera.setExtent(selCountryExtent)
mainMapFrame.camera.scale = mainMapFrame.camera.scale * 1.05

# Export to PDF and open in Adobe Acrobat Reader
lyt.exportToPDF(r"C:\LPA\PDFs\test.pdf")
os.startfile(r"C:\LPA\PDFs\test.pdf")

# Delete project object
del aprx


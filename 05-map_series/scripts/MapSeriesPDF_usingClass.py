import arcpy

aprx = arcpy.mp.ArcGISProject(
    r"C:\LPA\Projects\MapSeriesProject\MapSeriesProject.aprx")
lyt = aprx.listLayouts("Layout")[0]
mapSeries = lyt.mapSeries
mapSeries.exportToPDF(r"C:\LPA\PDFs\LayoutFromClass.pdf","RANGE","1-10")
del aprx

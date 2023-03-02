import arcpy, pprint


def print_source(layerName):
    lyr2Print = mapx.listLayers(layerName)[0]
    print(f"{lyr2Print.name}: {lyr2Print.dataSource}")


def print_dict(dict2Print):
    pprint.pprint(dict2Print)


aprx = arcpy.mp.ArcGISProject(
    r"C:\LPA\Projects\DataSourceProject\DataSourceProject.aprx"
)

mapx = aprx.listMaps()[0]
print_source("Countries")

lyr = mapx.listLayers("Countries")[0]
defaultGDB = r"C:\LPA\Projects\DataSourceProject\DataSourceProject.gdb"
lyr.dataSource = rf"{defaultGDB}\Countries_African"
origConnPropDict = lyr.connectionProperties
print_dict(origConnPropDict)

newConnPropDict = {
    "connection_info": {"database": defaultGDB},
    "dataset": "Countries_African",
    "workspace_factory": "File Geodatabase",
}

lyr.updateConnectionProperties(origConnPropDict, newConnPropDict)

print_dict(newConnPropDict)
print_source("Countries")


del aprx

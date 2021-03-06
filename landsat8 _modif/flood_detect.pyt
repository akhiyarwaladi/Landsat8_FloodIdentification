import arcpy
import data_process as dp
import os

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Flood Detection Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Flood Detection Toolbox"
        self.description = ""
        self.canRunInBackground = False
        self.params = arcpy.GetParameterInfo()

    def getParameterInfo(self):
        """Define parameter definitions"""
        pre_flood = arcpy.Parameter(
                displayName= "Data sebelum banjir (pre flood)",
                name = "pre_flood",
                datatype = "DEFolder",
                parameterType = "Required",
                direction = "Input"
            )
        post_flood = arcpy.Parameter(
                displayName= "Data setelah banjir (post flood)",
                name = "post_flood",
                datatype = "DEFolder",
                parameterType = "Required",
                direction = "Input"
            )
        threshold_opt1 = arcpy.Parameter(
                displayName= "Default",
                name = "threshold_opt1",
                datatype = "GPBoolean",
                
                direction = "Input"
            )
        threshold_opt1.category = "Options"
        # Second parameter
        threshold_default = arcpy.Parameter(
                displayName="Default by source",
                name="threshold_default",
                datatype="Field",
                
                direction="Input"
            )
        threshold_default.filter.list = ["Gao(deltaNDWI >= 0.094 ; duringNDWI >= 0.161)", "McFeeters(deltaNDWI >= 0.228 ; duringNDWI >= 0.548)"]
        threshold_default.enabled = False
        threshold_default.category = "Options"

        threshold_opt2 = arcpy.Parameter(
                displayName= "Define",
                name = "threshold_opt2",
                datatype = "GPBoolean",
                
                direction = "Input"
            )
        threshold_opt2.category = "Options"
        threshold_define1 = arcpy.Parameter(
                displayName="Delta NDWI",
                name="threshold_define1",
                datatype="String",
                
                direction="Input"
            )
        threshold_define2 = arcpy.Parameter(
                displayName="Post NDWI",
                name="threshold_define2",
                datatype="String",
                
                direction="Input"
            )
        threshold_define1.enabled = False
        threshold_define1.category = "Options"
        threshold_define2.enabled = False
        threshold_define2.category = "Options"
        
        # projection = arcpy.Parameter(
        #         displayName= "Projeksi data (ke utm sesuai zona)",
        #         name = "projection",
        #         datatype = "GPSpatialReference",
        #         parameterType = "Required",
        #         direction = "Input"
        #     )
        out_process = arcpy.Parameter(
                displayName = "Folder keluaran hasil praproses",
                name = "out_process",
                datatype = "DEFolder",
                parameterType = "Required",
                direction = "Output"
            )
        projection = arcpy.Parameter(
                displayName= "Projeksi data (ke utm sesuai zona)",
                name = "projection",
                datatype = "DEShapefile",
                parameterType = "Required",
                direction = "Input"
            )
        #params = [pre_flood, post_flood, projection, out_process]
        params = [pre_flood, post_flood, threshold_opt1, threshold_default, threshold_opt2, threshold_define1, threshold_define2, out_process, projection]


        # if self.params[2].value:
        #     self.params[3].enabled = True
        # else:
        #     self.params[3].enabled = False
        return params



    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        tOpt1 = parameters[2]
        tValue1 = parameters[3]

        tOpt2 = parameters[4]
        tValue21 = parameters[5]
        tValue22 = parameters[6]

        if tOpt1.value == True:
            tValue1.enabled = True
           
        else:
            tValue1.enabled = False

        if tOpt2.value == True:
            tValue21.enabled = True
            tValue22.enabled = True
        else:
            tValue21.enabled = False
            tValue22.enabled = False

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):

        utm_zone12 = "PROJCS['NAD_1983_UTM_Zone_12N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-111.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "NEAREST", "30", "WGS_1984_(ITRF00)_To_NAD_1983", "", "PROJCS['WGS_84_UTM_zone_12N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['false_easting',500000.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',-111.0],PARAMETER['scale_factor',0.9996],PARAMETER['latitude_of_origin',0.0],UNIT['Meter',1.0]]"
        """The source code of the tool."""
        pre_flood = parameters[0].valueAsText
        post_flood = parameters[1].valueAsText
        projection = utm_zone12
        out_process = parameters[2].valueAsText
        inFC = parameters[3].valueAsText
        SR = arcpy.Describe(inFC).spatialReference
        
        # messages.addMessage(
        #     '\n'+pre_flood+'\n'+post_flood+'\n'+projection+'\n'
        # )
        
        os.mkdir(out_process)
        dp.process_landsat(pre_flood, SR, out_process, "_PreFlood")
        dp.process_landsat(post_flood, SR, out_process, "_PostFlood")
        dp.diffNDWI(out_process, os.path.basename(pre_flood), os.path.basename(post_flood))
        dp.pixelExtraction(out_process, os.path.basename(pre_flood), os.path.basename(post_flood))
        dp.createRandomPoint(out_process)
        dp.valuesToPoint(out_process)
        return

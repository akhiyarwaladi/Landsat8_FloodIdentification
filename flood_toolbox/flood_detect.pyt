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

        landsat_number = arcpy.Parameter(
                displayName= "Data Landsat ke-",
                name = "landsat_7",
                datatype = "String",
                direction = "Input"
            )
        landsat_number.filter.list = ['Landsat8', 'Landsat7']

        pre_flood = arcpy.Parameter(
                displayName= "Folder Data sebelum banjir (pre flood)",
                name = "pre_flood",
                datatype = "DEFolder",
                parameterType = "Required",
                direction = "Input"
            )

        post_flood = arcpy.Parameter(
                displayName= "Folder Data setelah banjir (post flood)",
                name = "post_flood",
                datatype = "DEFolder",
                parameterType = "Required",
                direction = "Input"
            )
        ###############################################THRESHOLD###################################################
        threshold_opt1 = arcpy.Parameter(
                displayName= "Default",
                name = "threshold_opt1",
                datatype = "GPBoolean",
                parameterType = "Optional",
                direction = "Input"
            )

        threshold_opt1.category = "Threshold Classification"
        
        threshold_default = arcpy.Parameter(
                displayName="Default by source",
                name="threshold_default",
                datatype="String",
                parameterType = "Optional",          
                direction="Input"
            )
        threshold_default.filter.list = ["Gao(deltaNDWI >= 0.094 ; duringNDWI >= 0.161)", "McFeeters(deltaNDWI >= 0.228 ; duringNDWI >= 0.548)"]
        threshold_default.enabled = False
        threshold_default.category = "Threshold Classification"

        threshold_opt2 = arcpy.Parameter(
                displayName= "Define",
                name = "threshold_opt2",
                datatype = "GPBoolean", 
                parameterType = "Optional",          
                direction = "Input"
            )
        threshold_opt2.category = "Threshold Classification"

        threshold_define1 = arcpy.Parameter(
                displayName="Delta NDWI",
                name="threshold_define1",
                datatype="String",       
                parameterType = "Optional",       
                direction="Input"
            )

        threshold_define2 = arcpy.Parameter(
                displayName="Post NDWI",
                name="threshold_define2",
                datatype="String",   
                parameterType = "Optional",          
                direction="Input"
            )
        threshold_define1.enabled = False
        threshold_define1.category = "Threshold Classification"
        threshold_define2.enabled = False
        threshold_define2.category = "Threshold Classification"
        
        ####################################### END THRESHOLD ######################################################

        out_process = arcpy.Parameter(
                displayName = "Folder keluaran hasil praproses",
                name = "out_process",
                datatype = "DEFolder",
                parameterType = "Required",
                direction = "Output"
            )

        projection = arcpy.Parameter(
                displayName= "Shapefile projeksi data ke utm sesuai zona",
                name = "projection",
                datatype = "DEShapefile",
                parameterType = "Required",
                direction = "Input"
            )

        ####################################### CLOUD MASK ######################################################
        masktype_list = arcpy.Parameter(
                displayName= "Mask Type",
                name = "masktype_list",
                datatype = "String",
                direction = "Input"
            )
        masktype_list.filter.list = ['Cloud', 'Cirrus', 'Snow', 'Vegetation', 'Water']
        masktype_list.category = 'Cloud Masking'


        confidence_list = arcpy.Parameter(
                displayName= "Confidence Level",
                name = "confidence_list",
                datatype = "String",
                direction = "Input"
            )
        confidence_list.filter.list = ['High', 'Medium', 'Low', 'None']
        confidence_list.category = 'Cloud Masking'

        ################################### END CLOUD MASK ######################################################
        
        params = [landsat_number, pre_flood, post_flood, threshold_opt1, threshold_default, threshold_opt2, threshold_define1, 
        threshold_define2, out_process, projection, masktype_list, confidence_list]

        return params



    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""


        tOpt1 = parameters[3]
        tValue1 = parameters[4]

        tOpt2 = parameters[5]
        tValue21 = parameters[6]
        tValue22 = parameters[7]

        if tOpt1.value == True:
            tValue1.enabled = True
            tOpt2.enabled = False
           
        else:
            tValue1.enabled = False
            tOpt2.enabled = True

        if tOpt2.value == True:
            tValue21.enabled = True
            tValue22.enabled = True
            tOpt1.enabled = False
        else:
            tValue21.enabled = False
            tValue22.enabled = False
            tOpt1.enabled = True

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):

        utm_zone12 = "PROJCS['NAD_1983_UTM_Zone_12N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-111.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "NEAREST", "30", "WGS_1984_(ITRF00)_To_NAD_1983", "", "PROJCS['WGS_84_UTM_zone_12N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['false_easting',500000.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',-111.0],PARAMETER['scale_factor',0.9996],PARAMETER['latitude_of_origin',0.0],UNIT['Meter',1.0]]"
        projection = utm_zone12
        """The source code of the tool."""

        pre_flood = parameters[1].valueAsText
        post_flood = parameters[2].valueAsText
        out_process = parameters[8].valueAsText
        inFC = parameters[9].valueAsText
        SR = arcpy.Describe(inFC).spatialReference

        masktype = parameters[10].valueAsText
        confidence = parameters[11].valueAsText
        cummulative = 'false'

        # messages.addMessage(
        #     '\n'+pre_flood+'\n'+post_flood+'\n'+projection+'\n'
        # )
        
        os.mkdir(out_process)
        dp.mask_cloud(pre_flood, masktype, confidence, cummulative, out_process)
        dp.mask_cloud(post_flood, masktype, confidence, cummulative, out_process)
        dp.process_landsat(pre_flood, SR, out_process, "_PreFlood")
        dp.process_landsat(post_flood, SR, out_process, "_PostFlood")
        # dp.diffNDWI(out_process, os.path.basename(pre_flood), os.path.basename(post_flood))
        # dp.pixelExtraction(out_process, os.path.basename(pre_flood), os.path.basename(post_flood))
        # dp.createRandomPoint(out_process)
        # dp.valuesToPoint(out_process)
        return

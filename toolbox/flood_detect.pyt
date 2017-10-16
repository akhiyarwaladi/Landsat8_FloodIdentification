import arcpy
import data_process as dp

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

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
        projection = arcpy.Parameter(
                displayName= "Projeksi data (ke utm sesuai zona)",
                name = "projection",
                datatype = "GPSpatialReference",
                parameterType = "Required",
                direction = "Input"
            )
        params = [pre_flood, post_flood, projection]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        pre_flood = parameters[0].valueAsText
        post_flood = parameters[1].valueAsText
        projection = parameters[2].valueAsText
        messages .addMessage(
                '\n'+pre_flood+'\n'+post_flood+'\n'+projection+'\n'
            )
        dp.process_landsat(pre_flood, projection)
        return

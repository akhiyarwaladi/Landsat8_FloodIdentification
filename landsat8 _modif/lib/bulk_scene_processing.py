import arcpy as ap
import landsat8_modif as ls

ls_dir = ap.GetParameterAsText(0)
proj = ap.GetParameterAsText(1)
#post_dir = ap.GetParameterAsText(2)

ap.AddMessage("Landsat8.py Version: " + str(ls.version))

ap.AddMessage("Begin bulk processing of the landsat scene.")
ls.process_landsat(ls_dir, proj)
ap.AddMessage("Completed bulk processing.")

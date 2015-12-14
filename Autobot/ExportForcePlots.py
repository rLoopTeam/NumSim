# ----------------------------------------------
# Script Recorded by ANSYS Maxwell Version 2015.2.0
# 19:10:23  Dec 11, 2015
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("AnsoftMaxwell.MaxwellScriptInterface")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("eddyBrake001")
oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
oModule = oDesign.GetModule("ReportSetup")
def exportForcePlots(directory,vel,gap):
  oModule.ExportToFile("XY Plot 1","{}/{}_{}.csv".format(directory,vel,gap))

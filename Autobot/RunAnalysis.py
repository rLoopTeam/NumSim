# ----------------------------------------------
# Script Recorded by ANSYS Maxwell Version 2015.2.0
# 18:54:54  Dec 11, 2015
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("AnsoftMaxwell.MaxwellScriptInterface")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("eddyBrake001")
oProject.Save()
oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
def runAnalysis():
  oDesign.Analyze("Setup1")

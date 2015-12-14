# ----------------------------------------------
# Script Recorded by ANSYS Maxwell Version 2015.2.0
# 12:11:05  Dec 12, 2015
# ----------------------------------------------
#import ScriptEnv
#ScriptEnv.Initialize("AnsoftMaxwell.MaxwellScriptInterface")
#oDesktop.RestoreWindow()
#oProject = oDesktop.SetActiveProject("eddyBrake001")

def _copyModel(oProject,designName):
  oProject.CopyDesign(designName)
  oProject.Paste()

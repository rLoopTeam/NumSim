# ----------------------------------------------
# Script Recorded by ANSYS Maxwell Version 2015.2.0
# 18:53:48  Dec 11, 2015
# ----------------------------------------------
#import ScriptEnv
#ScriptEnv.Initialize("AnsoftMaxwell.MaxwellScriptInterface")
#oDesktop.RestoreWindow()
#oProject = oDesktop.SetActiveProject("eddyBrake001")
#oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
#oModule = oDesign.GetModule("ModelSetup")


def _setVelocity(vel,oModule):
  oModule.EditMotionSetup("MotionSetup1", 
    [
      "NAME:Data",
      "Move Type:="    , "Translate",
      "Coordinate System:="  , "Global",
      "PostProcessing Coordinate System:=", "Global",
      "Axis:="    , "X",
      "Is Positive:="    , True,
      "InitPos:="    , "0mm",
      "TranslatePeriodic:="  , True,
      "Consider Mechanical Transient:=", False,
      "Velocity:="    , "{}m_per_sec".format(vel)
    ])
  oModule.EditMotionSetup("MotionSetup2", 
    [
      "NAME:Data",
      "Move Type:="    , "Translate",
      "Coordinate System:="  , "Global",
      "PostProcessing Coordinate System:=", "Global",
      "Axis:="    , "X",
      "Is Positive:="    , True,
      "InitPos:="    , "0mm",
      "TranslatePeriodic:="  , True,
      "Consider Mechanical Transient:=", False,
      "Velocity:="    , "{}m_per_sec".format(vel)
    ])

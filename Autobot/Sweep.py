import ScriptEnv
ScriptEnv.Initialize("AnsoftMaxwell.MaxwellScriptInterface")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("eddyBrake001")
oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
oModule = oDesign.GetModule("ModelSetup")

from EddyBrakeModel import EddyBrakeModel

ebm = EddyBrakeModel(oModule)
ebm.setVelocity(55)
from SetGap import _setGap
from SetVelocity import _setVelocity

class EddyBrakeModel():

  def __init__(self,oDesktop,projectName,designName):
    self.projectName = projectName
    self.designName = designName

    self.oProject = oDesktop.SetActiveProject(projectName)
    self.oDesign = self.oProject.SetActiveDesign(designName)
    self.oDesktop = oDesktop


  def setVelocity(self,vel):

    self.oDesign.ChangeProperty(
      [
        "NAME:AllTabs",
        [
          "NAME:LocalVariableTab",
          ["NAME:PropServers", "LocalVariables"],
          [
            "NAME:ChangedProps",
            [
              "NAME:v",
              "Value:="    , "{}m_per_sec".format(vel)
            ]
          ]
        ]
      ])

  def setGap(self,gap):

    self.oDesign.ChangeProperty(
      [
        "NAME:AllTabs",
        [
          "NAME:LocalVariableTab",
          [
            "NAME:PropServers", 
            "LocalVariables"
          ],
          [
            "NAME:ChangedProps",
            [
              "NAME:h",
              "Value:="    , "{}".format(gap)
            ]
          ]
        ]
      ])

  def copy(self,newName=None):

    designNames = []
    for design in self.oProject.GetDesigns():
      designNames.append(design.GetName())

    self.oProject.CopyDesign(self.designName)
    self.oProject.Paste()

    newDesignNames = []
    for design in self.oProject.GetDesigns():
      if not design.GetName() in designNames:
        break

    pasteName = design.GetName()     
    
    cpy = EddyBrakeModel(self.oDesktop,self.projectName,pasteName)
    
    if newName:
      cpy.rename(newName)

    return cpy


  def rename(self,newName):
    self.oDesign.RenameDesignInstance(self.designName,newName)
    self.designName = newName


  def runAnalysis(self):
    self.oDesign.Analyze("Setup1")

  def exportForcePlot(self,filename):
    oModule = self.oDesign.GetModule("ReportSetup")
    oModule.ExportToFile("XY Plot 1","{}".format(filename))

# ----------------------------------------------
# Script Recorded by ANSYS Maxwell Version 2015.2.0
# 18:50:15  Dec 11, 2015
# ----------------------------------------------
#import ScriptEnv
#ScriptEnv.Initialize("AnsoftMaxwell.MaxwellScriptInterface")
#oDesktop.RestoreWindow()
#oProject = oDesktop.SetActiveProject("eddyBrake001")
#oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
#oEditor = oDesign.SetActiveEditor("3D Modeler")

def _setGap(height,oEditor):
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DCmdTab",
                [
                    "NAME:PropServers", 
                    "mag1:CreateRectangle:1"
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Position",
                        "X:="            , "0mm",
                        "Y:="            , "{}mm".format(height),
                        "Z:="            , "0mm"
                    ]
                ]
            ]
        ])
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DCmdTab",
                [
                    "NAME:PropServers", 
                    "mag2:CreateRectangle:1"
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Position",
                        "X:="            , "50mm",
                        "Y:="            , "{}mm".format(height),
                        "Z:="            , "0mm"
                    ]
                ]
            ]
        ])
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DCmdTab",
                [
                    "NAME:PropServers", 
                    "mag3:CreateRectangle:1"
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Position",
                        "X:="            , "0mm",
                        "Y:="            , "-{}mm".format(height),
                        "Z:="            , "0mm"
                    ]
                ]
            ]
        ])
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DCmdTab",
                [
                    "NAME:PropServers", 
                    "mag4:CreateRectangle:1"
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Position",
                        "X:="            , "50mm",
                        "Y:="            , "-{}mm".format(height),
                        "Z:="            , "0mm"
                    ]
                ]
            ]
        ])

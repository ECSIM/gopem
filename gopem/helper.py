# -*- coding: utf-8 -*-
"""GOPEM helper."""
import os
import sys
from opem.Params import Amphlett_InputParams as A
from opem.Params import Chamberline_InputParams as C
from opem.Params import Larminiee_InputParams as L
from opem.Params import Padulles_InputParams as P
from opem.Params import Padulles2_InputParams as P2
from opem.Params import Padulles_Amphlett_InputParams as PA
from opem.Params import Padulles_Hauer_InputParams as PH
from opem.Params import Version as OPEM_Version

Version = 0.2

ScriptDir = os.path.dirname(os.path.realpath(__file__))
ParentDir = os.path.abspath(os.path.join(ScriptDir, os.pardir))
if not hasattr(sys, "frozen"):
    IconPath = os.path.join(ParentDir,"rsrc","icon.ico")
else:
    IconPath = os.path.join(sys.prefix, "icon.ico")

VersionText = 'GOPEM(v{0}) / OPEM(v{1}) '.format(str(Version),
                                                 str(OPEM_Version))
ReportTitle = "Do you want to have a generated report for this analysis ?"
PrintTitle = "Console print"
TestTitle = "Use Test Data"
AnalyzingMessage = "Analyzing ..."
DownloadLink = '<a href="https://github.com/ECSIM/gopem/releases/download/v{1}/GOPEM-{1}.exe">Download</a>'
UpdateUrl = "http://www.ecsim.ir/opem/gopem_update.html"
VersionMessage = """
<br/>
<br/>
Your version : {0}
<br/>
<br/>
Current version : {1}
<br/>
<br/>
"""

CiteMessage = """
Hi!
<br/>
When you want to use this software in your research projects and reports, we appreciate if you cite us.
<br/>
<br/>
<a href="https://doi.org/10.21105/joss.00676">Paper Link</a>
<br/>
<a href="http://www.ecsim.ir/opem/OPEM.bib">BibTeX Link</a>
"""
UpdateMessage1 = "You are running the latest version.\n" + VersionMessage


UpdateMessage2 = "A newer version of the GOPEM is available to download.\n" + \
    VersionMessage + "\n" + DownloadLink

UpdateMessage3 = "Update check failed!\n" + VersionMessage + "\n"

ReportMessage = "Report has been saved successfully in current folder!"
PlotMessage = "Plot has been saved successfully!"

InputParam = {
    "Amphlett_Analysis (Static)": A,
    "Larminiee_Analysis (Static)": L,
    "Chamberline_Kim_Analysis (Static)": C,
    "Padulles_Analysis I (Dynamic)": P,
    "Padulles_Analysis II (Dynamic)": P2,
    "Padulles_Hauer Analysis (Dynamic)": PH,
    "Padulles_Amphlett Analysis (Dynamic)": PA
}

UnitTable = {
    "P": ["Power", "W"],
    "I": ["Current", "A"],
    "V": ["Voltage", "V"],
    "EFF": ["Efficiency", None],
    "Ph": ["Power-Thermal", "W"],
    "Eta_Active": ["Eta Activation", "V"],
    "Eta_Conc": ["Eta Concentration", "V"],
    "Eta_Ohmic": ["Eta Ohmic", "V"],
    "VE": ["Estimated Voltage", "V"],
    "PO2": ["PO2", "atm"],
    "PH2": ["PH2", "atm"],
    "PH2O": ["PH2O", "atm"]}

ColorList = ["Black", "Blue", "Green", "Red", "Cyan", "Magenta", "Yellow"]

MarkerTable = {
    "Point": ".",
    "Pixel": "o",
    "Circle": "o",
    "Square": "s",
    "Pentagon": "p",
    "Star": "*",
    "Plus": "+",
    "Vline": "|",
    "Hline": "_",
    "None": ""}
MarkerList = list(sorted(MarkerTable.keys()))
MarkerList.insert(0, MarkerList.pop(MarkerList.index("None")))

StyleTable = {"Solid": "-", "Dashed": "--", "Dash-Dot": "-.", "Dotted": ":"}
StyleList = list(sorted(StyleTable.keys()))
StyleList.insert(0, StyleList.pop(StyleList.index("Solid")))

ScaleList = ["Linear", "Log"]
WidthList = list(range(1, 11))

FontSizeList = list(range(1,56))
TitleFontDefault = 15
AxesFontDefault = 11
"""GOPEM helper."""
from opem.Params import Amphlett_InputParams as A
from opem.Params import Chamberline_InputParams as C
from opem.Params import Larminiee_InputParams as L
from opem.Params import Padulles_InputParams as P
from opem.Params import Padulles2_InputParams as P2
from opem.Params import Padulles_Amphlett_InputParams as PA
from opem.Params import Padulles_Hauer_InputParams as PH

Version = 0.2
UpdateUrl = "http://www.ecsim.ir/opem/gopem_update.html"
VersionMessage = """

Your version : {0}

Current version : {1}

"""

UpdateMessage1 = "You are running the latest version.\n" + VersionMessage




UpdateMessage2 = "A newer version of the GOPEM is available to download.\n" + VersionMessage


UpdateMessage3 = "Update check failed!\n" + VersionMessage

ReportMessage = "Report has been saved in current folder!"
InputParam = {
    "Amphlett_Analysis (Static)": A,
    "Larminiee_Analysis (Static)": L,
    "Chamberline_Kim_Analysis (Static)": C,
    "Padulles_Analysis I (Dynamic)": P,
    "Padulles_Analysis II (Dynamic)": P2,
    "Padulles_Hauer Analysis (Dynamic)": PH,
    "Padulles_Amphlett Analysis (Dynamic)": PA
}

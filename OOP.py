class HiddenBox:
    def __init__(self,BoxName,Creator,DateHidden,GameLocation):
        self.__BoxName = BoxName
        self.__Creator = Creator
        self.__DateHidden = DateHidden
        self.__GameLocation = GameLocation
        self.__LastFinds = [(0)*2 for i in range(10)]
        self.__Active = False
    def GetBoxName(self):
        return self.__BoxName
    def GetGameLocation(self):
        return self.__GameLocation
TheBoxes = [HiddenBox("","","","") for i in range(10000)]
NumBoxes = 0
def NewBox(TheBoxes,NumBoxes):
    Name = input("input name")
    Creator = input("input creator")
    DateHidden = input("input date")
    GameLoc = input("input game location")
    TheBoxes[NumBoxes] = HiddenBox(Name,Creator,DateHidden,GameLoc)
    return NumBoxes+1
NumBoxes = NewBox(TheBoxes,NumBoxes)
class PuzzleBox(HiddenBox):
    def __init__(self,BoxName,Creator,DateHidden,GameLocation,PuzzleText,Solution):
        HiddenBox.__init__(self,BoxName,Creator,DateHidden,GameLocation)
        self.__PuzzleText = PuzzleText
        self.__Solution = Solution

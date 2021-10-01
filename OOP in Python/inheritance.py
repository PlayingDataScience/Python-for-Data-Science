class Champion(object):
       
    def __init__(self, name):
        self.name = name
   
    def getName(self):
        return self.name
   
    def isChamp(self):
        return False
   
   
class Champ(Champion):
   
    def isChamp(self):
        return True
   
chmp = Champion("Name1") 
print(chmp.getName(), chmp.isChamp())
   
chmp = Champion("Name2")
print(chmp.getName(), chmp.isChamp())

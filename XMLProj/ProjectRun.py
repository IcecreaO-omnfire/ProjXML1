
from ProjectImport import *
b=ShowBase()
def xmlprocess():
    file=open("details.xml")
    filetext=file.read()
    e=xmlparse.fromstring(filetext)
    data=e
    for sections in data:
        if sections.tag=="model":
            if sections.attrib["name"]=="Box2Resized.egg":
                GlobalVariables.box=loader.loadModel("Model/Box2Resized.egg")
                GlobalVariables.boxcollision=GlobalVariables.box.attachNewNode(CollisionNode("BoxCollisionNodes"))
                for section2 in sections: 
                    if section2.tag=="modelsection":
                        boxbounds(GlobalVariables.boxcollision.node(),GlobalVariables.box.find(section2.text))
                GlobalVariables.box.reparentTo(render)
                GlobalVariables.boxcollision.show()


def boxbounds(boxcollision,boxspace):
    bounds1=boxspace.getTightBounds()
    collision=CollisionBox(bounds1[0],bounds1[1])
    boxcollision.addSolid(collision)
    return collision

b.xmlprocess=xmlprocess
b.xmlprocess()
b.run()

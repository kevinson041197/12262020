def buildPyramind(x,y,z,base):
    height=(base//2)+1
    for i in range(height):
        x1=x+i
        y1=y+i
        z1=z+i
        
        x2=x+base-i
        z2=z+base-i
        mc.setBlocks(x1,y1,z1,x2,y,z2,24)


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
base=int(input("base:"))
buildPyramind(x,y,z,base)
























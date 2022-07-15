from graphics import *
import math

def createmorepolygons(polygonlist):
    newlist = []
    for i in range(len(polygonlist)):
        newlist.append(polygonlist[i])
        try:
            x1 = (polygonlist[i][0] + polygonlist[i + 1][0] + polygonlist[i + 2][0]) / 2
            y1 = (polygonlist[i][1] + polygonlist[i + 1][1] + polygonlist[i + 2][1]) / 2
            z1 = (polygonlist[i][2] + polygonlist[i + 1][2] + polygonlist[i + 2][2]) / 2
        except:
            x1 = (polygonlist[i][0] + polygonlist[0][0]) / 2
            y1 = (polygonlist[i][1] + polygonlist[0][1]) / 2
            z1 = (polygonlist[i][2] + polygonlist[0][2]) / 2

        newlist.append([x1, y1, z1, polygonlist[i][3]])
        try:
            newlist.append(polygonlist[i + 1])
        except:
            newlist.append(polygonlist[0])
    return newlist



def darken(hexcode, dark):
    hecxcodedict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    rgb = [(hecxcodedict[hexcode[1]] * 16) + hecxcodedict[hexcode[2]],
           (hecxcodedict[hexcode[3]] * 16) + hecxcodedict[hexcode[4]],
           (hecxcodedict[hexcode[5]] * 16) + hecxcodedict[hexcode[6]]]
    sorte = [rgb[0], rgb[1], rgb[2]]
    sorte.sort()
    lower = sorte[0]
    middle = sorte[1]
    higher = sorte[-1]
    newrgb = []
    for x in rgb:
        if x == lower:
            l = x + (middle - x) * dark
            if l > 255:
                l = 255
            if l < 0:
                l = 0

            newrgb.append(l)
        elif x == higher:
            l = x - (x - middle) * dark
            if l > 255:
                l = 255
            if l < 0:
                l = 0
            newrgb.append(l)
        else:
            l = x
            if l > 255:
                l = 255
            if l < 0:
                l = 0
            newrgb.append(l)
    hexcodereturn = "#" + hecxcodedict[int(math.floor(newrgb[0] / 16))] + hecxcodedict[
        int(math.floor(newrgb[0]) % 16)] + \
                    hecxcodedict[int(math.floor(newrgb[1] / 16))] + hecxcodedict[int(math.floor(newrgb[1]) % 16)] + \
                    hecxcodedict[
                        int(math.floor(newrgb[2] / 16))] + hecxcodedict[int(math.floor(newrgb[2]) % 16)]
    return hexcodereturn


def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
def direction(x1, y1, z1, x2, y2, z2):
    vectorX = x2 - x1

    vectorY = y2 - y1

    vectorZ = z2 - z1

    if vectorX == 0:
        vectorX = 0.00000001
    if vectorY == 0:
        vectorY = 0.000000001
    if vectorZ == 0:
        vectorZ = 0.0000000001

    angle = math.atan(vectorY / vectorX)

    angle1 = math.atan(vectorX / vectorZ)

    if vectorX > 0 and vectorY > 0:
        angle = angle
    elif vectorX < 0 and vectorY > 0:
        angle = abs(0.5 * math.pi - (angle + math.pi)) + 0.5 * math.pi
    elif vectorX < 0 and vectorY < 0:
        angle = angle + math.pi
    elif vectorX > 0 and vectorY > 0:
        angle = abs(0.5 * math.pi - (angle + math.pi)) + 1.5 * math.pi

    if vectorZ > 0 and vectorX > 0:
        angle1 = angle1
    elif vectorZ < 0 and vectorX > 0:
        angle1 = abs(0.5 * math.pi - (angle1 + math.pi)) + 0.5 * math.pi
    elif vectorZ < 0 and vectorX < 0:
        angle1 = angle1 + math.pi
    elif vectorZ > 0 and vectorX > 0:
        angle1 = abs(0.5 * math.pi - (angle1 + math.pi)) + 1.5 * math.pi

    angle = (0.5*math.pi -  angle) % (2 * math.pi)
    angle1 = (0.5*math.pi -  angle1) % (2 * math.pi)
    if angle<0:
        angle = 2*math.pi + angle
    if angle1 < 0:
        angle1 = 2 * math.pi + angle1
    return angle, angle1

def draw(polygonlist2d, Polygon_list, CameraX, CameraY, CameraZ, win, i,darknesscoefficient):
    p1 = polygonlist2d[i][0], polygonlist2d[i][1]
    p2 = polygonlist2d[i + 1][0], polygonlist2d[i + 1][1]
    p3 = polygonlist2d[i + 2][0], polygonlist2d[i + 2][1]

    if polygonlist2d[i][0] > 300 or polygonlist2d[i][0] < -300 or polygonlist2d[i][1] > 300 or polygonlist2d[i][
        1] < -300 or \
            polygonlist2d[i + 1][0] > 300 or polygonlist2d[i + 1][0] < -300 or polygonlist2d[i + 1][1] > 300 or \
            polygonlist2d[i + 1][1] < -300 or polygonlist2d[i + 2][0] > 300 or polygonlist2d[i + 2][0] < -300 or \
            polygonlist2d[i + 2][1] > 300 or polygonlist2d[i + 2][1] < -300:
        return

    layer = Polygon(Point(p1[0], p1[1]), Point(p2[0], p2[1]), Point(p3[0], p3[1]), Point(p1[0], p1[1]))

    hexcode = darken(Polygon_list[i][3], darknesscoefficient)

    if len(Polygon_list[i]) > 3:
        layer.setFill(hexcode)

    if len(Polygon_list[i]) > 4:
        layer.setOutline(hexcode)

    layer.draw(win)


def main(main, win):
    CameraX = 0
    CameraY = 0
    CameraZ = 0
    CameraPhi = 0
    CameraTheta = 0
    main = [[main[x], main[x + 1], main[x + 2]] for x in range(0, len(main), 3)]
    while True:
        polygonlist2d = []
        maindist = [max([distance(main[x][0][0], main[x][0][1], main[x][0][2], CameraX, CameraY, CameraZ) ,distance(
            main[x][1][0], main[x][1][1], main[x][1][2], CameraX, CameraY, CameraZ) ,distance(main[x][2][0],
                                                                                               main[x][2][1],
                                                                                               main[x][2][2], CameraX,
                                                                                               CameraY, CameraZ)])
                    for x in range(len(main))]
        intermediary = [x for _, x in sorted(zip(maindist, main))]
        intermediary.reverse()
        Polygon_list = []
        for i in range(len(intermediary)):
            for x in range(len(intermediary[i])):
                Polygon_list.append(intermediary[i][x])
        for x in Polygon_list:
            r = direction(CameraX, CameraY, CameraZ, x[0], x[1], x[2])
            r = r[0]-CameraTheta-math.pi,r[1]-CameraPhi-math.pi

            if r[0]<0:
                r = 2*math.pi + r[0],r[1]
            if r[0]>2*math.pi:
                r = r[0]-2*math.pi,r[1]
            if r[1]<0:
                r = r[0],2*math.pi + r[1]
            if r[1] > 2*math.pi:
                r = r[0], r[1] - 2*math.pi
            if 1.5*math.pi>r[0]>0.5*math.pi and 1.5*math.pi>r[1]>0.5*math.pi:
                polygonlist2d.append([(r[1]-math.pi)*(400/math.pi),(r[0]-math.pi)*(400/math.pi)])
            else:
                polygonlist2d.append(["NAN", "NAN"])
        print(polygonlist2d)
        p = win.find_all()
        lool = []
        for i in range(0,len(Polygon_list)):
            lool.append(distance(Polygon_list[i][0], Polygon_list[i][1], Polygon_list[i][2], CameraX, CameraY,
                                       CameraZ))
        for i in range(0,len(lool)):
            lool[i] = (lool[i]-min(lool))/max(lool)
        for i in range(0, len(polygonlist2d), 3):
            if polygonlist2d[i][0] != "NAN" and polygonlist2d[i + 1][0] != "NAN" and polygonlist2d[i + 2][0] != "NAN":
                draw(polygonlist2d, Polygon_list, CameraX, CameraY, CameraZ, win, i,lool[i])
        for item in p:
            win.delete(item)
        win.update()
        pressedkey = win.checkKey()
        if pressedkey == "w":
            CameraTheta += 0.1 * math.pi
            if CameraTheta > 2 * math.pi:
                CameraTheta = CameraTheta - (2 * math.pi)
        if pressedkey == "s":
            CameraTheta -= 0.1 * math.pi
            if CameraTheta < 0:
                CameraTheta = 2 * math.pi + CameraTheta
        if pressedkey == "a":
            CameraPhi -= 0.1 * math.pi
            if CameraPhi < 0:
                CameraPhi = (2 * math.pi) + CameraPhi

        elif pressedkey == "d":
            CameraPhi += 0.1 * math.pi

            if CameraPhi > 2 * math.pi:
                CameraPhi = CameraPhi - (2 * math.pi)
        if pressedkey == "i":
            CameraX += math.sin(CameraTheta) * math.cos(CameraPhi) * 0.1
            CameraY += math.cos(CameraTheta) * math.cos(CameraPhi) * 0.1
            CameraZ += math.sin(CameraPhi) * 0.1
        if pressedkey == "k":
            CameraX -= math.sin(CameraTheta) * math.cos(CameraPhi) * 0.1
            CameraY -= math.cos(CameraTheta) * math.cos(CameraPhi) * 0.1
            CameraZ -= math.sin(CameraPhi) * 0.1

        print(CameraTheta)
        print(CameraPhi)


pyramid = [[2, 2, 2, "#00FFAA"], [4, 2, 2, "#00FFAA"], [3, 4, 2, "#00FFAA"], [3, 4, 2, "#00FFAA"], [4, 2, 2, "#00FFAA"],
           [3, 2, 3, "#00FFAA"], [3, 2, 3, "#00FFAA"], [3, 4, 2, "#00FFAA"], [2, 2, 2, "#00FFAA"],
           [2, 2, 2, "#00FFAA"], [3, 2, 3, "#00FFAA"], [4, 2, 2, "#00FFAA"]]
base = []

sphere = []

slice = 36

for i in range(0, 360, slice):
    p = 0
    for x in range(0, 360, slice):  # 18 degrees
        x1 = 3 + math.sin((i + slice) * (math.pi / 180)) * math.cos(x * (math.pi / 180))
        y1 = 4 + math.cos((i + slice) * (math.pi / 180)) * math.cos(x * (math.pi / 180))
        z1 = 2 + math.sin(x * (math.pi / 180))

        x2 = 3 + math.sin(i * (math.pi / 180)) * math.cos(x * (math.pi / 180))
        y2 = 4 + math.cos(i * (math.pi / 180)) * math.cos(x * (math.pi / 180))
        z2 = 2 + math.sin(x * (math.pi / 180))

        x3 = 3 + math.sin(i * (math.pi / 180)) * math.cos((x + slice) * (math.pi / 180))
        y3 = 4 + math.cos(i * (math.pi / 180)) * math.cos((x + slice) * (math.pi / 180))
        z3 = 2 + math.sin((x + slice) * (math.pi / 180))
        # next line
        x4 = 3 + math.sin((i + slice)*(math.pi / 180))  * math.cos(x * (math.pi / 180))
        y4 = 4 + math.cos((i + slice)*(math.pi / 180))  * math.cos(x * (math.pi / 180))
        z4 = 2 + math.sin(x * (math.pi / 180))

        x5 = 3 + math.sin(i * (math.pi / 180)) * math.cos((x + slice) * (math.pi / 180))
        y5 = 4 + math.cos(i * (math.pi / 180)) * math.cos((x + slice) * (math.pi / 180))
        z5 = 2 + math.sin((x + slice) * (math.pi / 180))

        x6 = 3 + math.sin((i + slice) * (math.pi / 180)) * math.cos((x + slice) * (math.pi / 180))
        y6 = 4 + math.cos((i + slice) * (math.pi / 180)) * math.cos((x + slice) * (math.pi / 180))
        z6 = 2 + math.sin((x + slice) * (math.pi / 180))

        sphere.append([x1, y1, z1, "#FF1144"])
        sphere.append([x2, y2, z2, "#FF1144" ])
        sphere.append([x3, y3, z3, "#FF1144" ])
        sphere.append([x4, y4, z4, "#FF1144"])
        sphere.append([x5, y5, z5, "#FF1144"])
        sphere.append([x6, y6, z6, "#FF1144"])

world = sphere
win = GraphWin("you a sussy baka", 400, 400, autoflush=False)
win.setCoords(-200, -200, 200, 200)
main(world,win)

from math import *
"""from Classes.Vector3 import Vec3"""
""" from Utils.Offsets import *  """
class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def checkangles(x, y):
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else:
        return True

def nanchecker(first, second):
    if isnan(first) or isnan(second):
        return False
    else:
        return True
    
def normalizeAngles(angle: Vec3):
    """ normalize angles (A normalized angle maps the full range of angles (360 degrees) to the range zero to one.)
    No implementation yet."""
    pass

def CalcDistance(current: Vec3, new: Vec3):
    pass

def checkindex(pm, engine):
    pass


def GetBestTarget(pm, client, engine, localPlayer, spotted, baim, aimfov, random):
    """ search for best target, multiple factors are taken into consideration such as entity_hp , team, position """
    pass


def smoothing(t):
    pass
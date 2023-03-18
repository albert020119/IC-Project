""" here we enumerate the functionalities of the bot such as aimbot, wallhack, strafe, bunnyhop """
from csgoCheat.Offsets import *
import time
from MatFunctions.MathPy import *

def Bhop(pm, client, player):
    force_jump = client + dwForceJump
    on_ground = pm.read_uint(player + m_fFlags)
    if player and on_ground == 257 or on_ground == 263:
        pm.write_int(force_jump, 6)


def AutoStrafe(pm, client, player, y_angle, oldviewangle):
    on_ground = pm.read_uint(player + m_fFlags)

    if player and (on_ground == 256 or on_ground == 262):

        if y_angle > oldviewangle:
            pm.write_int(client + dwForceLeft, 6)

        elif y_angle < oldviewangle:
            pm.write_int(client + dwForceRight, 6)

    return y_angle



def SetEntityGlow(pm, entity_hp, entity_team_id, entity_dormant, localTeam, glow_manager, entity_glow, eteam, health, color):
   """ the SetEntityGlow function will make enemies glow and visible through walls """
   pass
""" some basic checks are made, entity_team_id in first place so that we see the enemies through the walls
and not the allies """

def GetEntityVars(pm, entity):
   pass
""" load Players info, used in main while looping through all the entities  """

def shootAtTarget(pm, client, engine, localpos, targetpos, player, engine_pointer, Silent, aimrcs, aimkey):
    """ calculations for target coordinates and writing the specific process """
    pass

def AimStep(pm, engine_pointer, smooth, CurrLocal, CurrTarget, LocalAngle, i, n):
   """ angle normalisation + distance calculations  """
   pass

def shootTrigger(pm, CrossID, client, lTeam, CTeam, triggerkey):
    """ if trigger key is pressed shoot at the pointing target """
    pass

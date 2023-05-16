from cmath import atan, pi, sqrt
import math
import pymem
import pymem.process
from threading import *
import utils.Offsets as Offsets
from win32api import GetAsyncKeyState

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
enginepointer = pm.read_int(engine + Offsets.dwClientState)
aimfov = int(input('Set Fov Value(1-26)'))

def calc_distance(current_x, current_y, new_x, new_y):
    distancex = new_x - current_x
    if distancex < -89:
        distancex += 360
    elif distancex > 89:
        distancex -= 360
    if distancex < 0.0:
        distancex = -distancex
 
    distancey = new_y - current_y
    if distancey < -180:
        distancey += 360
    elif distancey > 180:
        distancey -= 360
    if distancey < 0.0:
        distancey = -distancey
    return distancex, distancey
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
def normalizeAngles(viewAngleX, viewAngleY):
    if viewAngleX > 89:
        viewAngleX -= 360
    if viewAngleX < -89:
        viewAngleX += 360
    if viewAngleY > 180:
        viewAngleY -= 360
    if viewAngleY < -180:
        viewAngleY += 360
    return viewAngleX, viewAngleY
def Distance(src_x, src_y, src_z, dst_x, dst_y, dst_z):
    try:
        diff_x = src_x - dst_x
        diff_y = src_y - dst_y
        diff_z = src_z - dst_z
        return sqrt(diff_x * diff_x + diff_y * diff_y + diff_z * diff_z)
    except:
        pass
def calcangle(localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3):
    try:
        delta_x = localpos1 - enemypos1
        delta_y = localpos2 - enemypos2
        delta_z = localpos3 - enemypos3
        hyp = sqrt(delta_x * delta_x + delta_y * delta_y + delta_z * delta_z)
        x = atan(delta_z / hyp) * 180 / pi
        y = atan(delta_y / delta_x) * 180 / pi
        if delta_x >= 0.0:
            y += 180.0
        return x, y
    except:
        pass
def Aimbot():
    while True:
        try:
            olddistx = 111111111111
            olddisty = 111111111111
            target = None
            aimlocalplayer = pm.read_int(client + Offsets.dwLocalPlayer)
            if aimlocalplayer :
                global localplayer_team
                localplayer_team = pm.read_int(aimlocalplayer + Offsets.m_iTeamNum)
                for x in range(32):
                    if pm.read_int(client + Offsets.dwEntityList + x * 0x10):
                        entity = pm.read_int(client + Offsets.dwEntityList + x * 0x10)
                        entity_hp = pm.read_int(entity + Offsets.m_iHealth)
                        entity_team = pm.read_int(entity + Offsets.m_iTeamNum)
                        if localplayer_team != entity_team and entity_hp > 0:
                            entity_bones = pm.read_int(entity + Offsets.m_dwBoneMatrix)
                            localpos_x_angles = pm.read_float(enginepointer + Offsets.dwClientState_ViewAngles)
                            localpos_y_angles = pm.read_float(enginepointer + Offsets.dwClientState_ViewAngles + 0x4)
                            localpos1 = pm.read_float(aimlocalplayer + Offsets.m_vecOrigin)
                            localpos2 = pm.read_float(aimlocalplayer + Offsets.m_vecOrigin + 4)
                            localpos_z_angles = pm.read_float(aimlocalplayer + Offsets.m_vecViewOffset + 0x8)
                            localpos3 = pm.read_float(aimlocalplayer + Offsets.m_vecOrigin + 8) + localpos_z_angles
                            entitypos_x = pm.read_float(entity_bones + 0x30 * 8 + 0xC)
                            entitypos_y = pm.read_float(entity_bones + 0x30 * 8 + 0x1C)
                            entitypos_z = pm.read_float(entity_bones + 0x30 * 8 + 0x2C)
                            X, Y = calcangle(localpos1, localpos2, localpos3, entitypos_x, entitypos_y, entitypos_z)
                            newdist_x, newdist_y = calc_distance(localpos_x_angles, localpos_y_angles, X, Y)
                            if newdist_x < olddistx and newdist_y < olddisty and newdist_x <= aimfov and newdist_y <= aimfov:
                                olddistx, olddisty = newdist_x, newdist_y
                                target, target_hp = entity, entity_hp
                                target_x, target_y, target_z = entitypos_x, entitypos_y, entitypos_z
                if target and target_hp > 0 and GetAsyncKeyState(18) != 0:
                    x, y = calcangle(localpos1, localpos2, localpos3, target_x, target_y, target_z)
                    normalize_x, normalize_y = normalizeAngles(x, y)
                    silent(normalize_x, normalize_y)
        except:
            pass
def silent(x, y):
    pm.write_uchar(engine + Offsets.dwbSendPackets, 0)
    Commands = pm.read_int(client + Offsets.dwInput + 0xF4)
    VerifedCommands = pm.read_int(client + Offsets.dwInput + 0xF8)
    Desired = pm.read_int(enginepointer + Offsets.clientstate_last_outgoing_command) + 2
    OldUser = Commands + ((Desired - 1) % 150) * 100
    VerifedOldUser = VerifedCommands + ((Desired - 1) % 150) * 0x68
    m_buttons = pm.read_int(OldUser + 0x30)
    Net_Channel = pm.read_uint(enginepointer + Offsets.clientstate_net_channel)
    if pm.read_int(Net_Channel + 0x18) >= Desired:
        pm.write_float(OldUser + 0x0C, x)
        pm.write_float(OldUser + 0x10, y)
        pm.write_int(OldUser + 0x30, m_buttons | (1 << 0))
        pm.write_float(VerifedOldUser + 0x0C, x)
        pm.write_float(VerifedOldUser + 0x10, y)
        pm.write_int(VerifedOldUser + 0x30, m_buttons | (1 << 0))
        pm.write_uchar(engine + Offsets.dwbSendPackets, 1)


if __name__ == '__main__':
    main()
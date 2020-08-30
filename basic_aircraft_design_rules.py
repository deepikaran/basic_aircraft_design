
import math
b = 75 # cm
c = 16 # cm
l_h = 27.5
l_v = l_h - 5

V_h = 0.45 # dim less const.
V_v = 0.035 # dim less const.

S = b * c # sq. cm
#l_h = V_h * S * c / S_h
#l_v = V_v * S * b / S_v

S_v = V_v * S * b / l_v
print("S_v given l_v (and V_v=0.035) = ", S_v)

##capital B should be more than 5, no upper range. So vv lower is better
S_v_new = 0.02 * S * b / l_v
print("S_v given V_v=0.02 and b=75 is ", S_v_new)

S_v_new = 0.05 * S * b / l_v
print("S_v given V_v=0.05 and b=75 is ", S_v_new)


S_h = V_h * S * c / l_h 
print("S_h given l_h = ", S_h)


wing_area_sq_cm = b * c
wing_area_sq_ft = 0.0328084 * 0.0328084 * wing_area_sq_cm

D = pow(wing_area_sq_ft, 1.5)

wt = 300 #gm
wt_oz = wt * 0.035274

#WL = wt_oz / wing_area_sq_ft ##useless metric
WCL = wt_oz / D

# reference: http://www.ef-uk.net/data/wcl.htm

if WCL < 4:
    model = "glider"
elif WCL < 7:
    model = "trainer"
elif WCL < 10:
    model = "aerobatic"
else: 
    model = "you need a better design"  
print("l_h theo =", l_h, "l_v theo = ", l_v, "WCL=", WCL, "model falls under type=", model)              


lift_centre_wing = b / 3

## Once you have S_h, ARh is calculated by choosing dimensions of horizontal tail to meet the S_h 

AR = b/c
ARh = 22 / 15 ##measured from horizontal tail

N = 1 + 2/AR
D = 1 + 2/ARh
M = 4/(AR + 2)
xnp = (0.25 + (N * (1-M) * V_h)/D) * c

print("xnp = ", xnp)

SM = 0.1
xcg = xnp - (SM * c)
print("xcg for stability=", xcg)

#from airfoil tools.com clark Y airfoil
CL = 0.75 
B = 5
dihedral_angle = B * b *CL / l_v

V_v_min = 0.02
V_v_max = 0.05 
B_max = 0.2 / V_v_min
B_min = 0.2 / V_v_max
if B_min < 5:
    B_min = 5

dihedral_angle_max = B_max * b *CL / l_v
dihedral_angle_min = B_min * b *CL / l_v
print("dihedral_angle_range=", dihedral_angle_min, dihedral_angle_max, "for B_min, B_max", B_min, B_max)

#lv * dih_angle_actual / (b * CL) 




import time
from mathutils import Euler, Matrix
from math import radians


lastNewMoonRecord = 1595294380.7988243#in seconds
moonCycle = 29.53#in days


mc = moonCycle * 24 * 60 * 60


def cek(cont):
	thisTime = time.time()
	
	#debugging
	#thisTime = lastNewMoonRecord + (7.3825 * 24 * 60 * 60)#first quarter
	#thisTime = lastNewMoonRecord + (14.765 * 24 * 60 * 60)#full moon
	#thisTime = lastNewMoonRecord + (22.1475 * 24 * 60 * 60)#third quarter
	
	x = thisTime - lastNewMoonRecord

	moonPhase = (x%mc) / 60 / 60 / 24 / 29.53
	
	#cont.owner["pos"] = moonPhase
	#print(moonPhase)#for debugging
	
	own = cont.owner
	if "moon" in own:
		moon = own.scene.objects[own['moon']]
		
		#rot = 45
		rot = 360 * -moonPhase
		r = radians(rot)
		el = Euler((0, 0, r))
		#print(el)
		moon.worldOrientation = el.to_matrix()
		
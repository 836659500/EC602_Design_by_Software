import math
import sys
infinite = float("inf")

class sphere():
  def __init__(self,x = 0,y = 0,z = 0,v_x = 0,v_y = 0,v_z = 0,mass = 0,radius = 0,name = None):
    self.x = x
    self.y = y
    self.z = z
    self.m = mass
    self.r = radius
    self.vx = v_x
    self.vy = v_y
    self.vz = v_z
    self.name = name
    self.collision = {}

  def __repr__(self):
    return "({:g})".format([self.x,self.y,self.z,self.vx,self.vy,self.vz,self.name])

  def collision_with_sphere(a, b): #Calculate next collision time of sphere a and sphere b
    if a == b: 
      return infinite
    else:
      dx = a.x - b.x
      dy = a.y - b.y
      dz = a.z - b.z
      dvx = a.vx - b.vx
      dvy = a.vy - b.vy
      dvz = a.vz - b.vz
      dr = a.r + b.r
      delta = (2*(dx*dvx + dy*dvy + dz*dvz))**2 - 4*(dvx**2+dvy**2+dvz**2)*((dx**2+dy**2+dz**2)-dr**2)

      if delta >= 0 and dx*dvx + dy*dvy + dz*dvz< 0:
        root1 = ((-2*(dx*dvx + dy*dvy + dz*dvz))+math.sqrt(delta)) / (2*(dvx**2+dvy**2+dvz**2))
        root2 = ((-2*(dx*dvx + dy*dvy + dz*dvz))-math.sqrt(delta)) / (2*(dvx**2+dvy**2+dvz**2))
        t = judge(root1,root2,0)
      else:
        t = infinite

      if t in a.collision:
        a.collision[t].append(b)
      else:
        a.collision.update({t:[b]})
      return t

  def collision_with_universe(one, universe): #Calculate next collision time of sphere one and the universe
    reflect_spot = sphere()
    reflect_spot.x = universe.x
    reflect_spot.y = universe.y
    reflect_spot.z = universe.z
    reflect_spot.vx = universe.vx
    reflect_spot.vy = universe.vy
    reflect_spot.vz = universe.vz
    reflect_spot.m = universe.m
    reflect_spot.r = universe.r
    reflect_spot.name = universe.name
    dr = universe.r - one.r
    delta = (2*(one.vx*one.x+one.vy*one.y+one.vz*one.z))**2 - 4*(one.vx**2+one.vy**2+one.vz**2)*((one.x**2+one.y**2+one.z**2)-dr**2)
    
    if one.vx**2 + one.vy**2 + one.vz**2 != 0:
      root1 = ((-2*(one.vx*one.x+one.vy*one.y+one.vz*one.z))+math.sqrt(delta)) / (2*(one.vx**2+one.vy**2+one.vz**2))
      root2 = ((-2*(one.vx*one.x+one.vy*one.y+one.vz*one.z))-math.sqrt(delta)) / (2*(one.vx**2+one.vy**2+one.vz**2))
      if round(math.sqrt((one.x**2)+(one.y**2)+(one.z**2))+one.r, 8) == universe.r:
        t = judge(root1,root2,1)
      else:
        t = judge(root1,root2,2)
    else:
      t = infinite
    
    new_x = one.x + one.vx * t
    new_y = one.y + one.vy * t
    new_z = one.z + one.vz * t

    if new_x == 0 and new_y*new_z != 0:
      reflect_spot.x = 0
      reflect_spot.y = universe.r / square_rooting(new_z,new_y)
      reflect_spot.z = (reflect_spot.y * new_z) / new_y
    elif new_y == 0 and new_x*new_z != 0:
      reflect_spot.x = universe.r / square_rooting(new_z,new_x)
      reflect_spot.y = 0
      reflect_spot.z = (reflect_spot.x * new_z) / new_x
    elif new_z == 0 and new_x*new_y != 0:
      reflect_spot.x = universe.r / square_rooting(new_y,new_x)
      reflect_spot.y = (reflect_spot.x * new_y) / new_x
      reflect_spot.z = 0
    elif new_x == 0 and new_y == 0 and new_z != 0:
      reflect_spot.x = 0
      reflect_spot.y = 0
      reflect_spot.z = new_z + one.r
    elif new_x == 0 and new_z == 0 and new_y != 0:
      reflect_spot.x = 0
      reflect_spot.y = new_y + one.r
      reflect_spot.z = 0
    elif new_y == 0 and new_z == 0 and new_x != 0:
      reflect_spot.x = new_x + one.r
      reflect_spot.y = 0
      reflect_spot.z = 0
    else: 
      reflect_spot.x = universe.r / (math.sqrt(1 + (new_y / new_x)**2 + new_z / new_x)**2)
      reflect_spot.y = new_y * reflect_spot.x / new_x
      reflect_spot.z = new_z * reflect_spot.x / new_x
    
    if t in one.collision:        
      one.collision[t].append(reflect_spot)
    else:
      one.collision.update({t:[reflect_spot]})

    return t

  def new_position(a, t): #Calculate the new position of the sphere at the next collision
    a.x += a.vx * t
    a.y += a.vy * t
    a.z += a.vz * t

  def new_velocity(a, b, t): #Calculate the new velocity of the sphere at the next collision
    dx = a.x - b.x
    dy = a.y - b.y
    dz = a.z - b.z
    dvx = a.vx - b.vx
    dvy = a.vy - b.vy
    dvz = a.vz - b.vz
    
    for sphere in a.collision[t]:
      if sphere.m != infinite:
        collide_with_universe = False
      else:
        collide_with_universe = True

    if collide_with_universe == True and b.m == infinite:
      for sphere in a.collision[t]:
        if sphere.m == infinite:
          spot = sphere
      dx = a.x - spot.x
      dy = a.y - spot.y
      dz = a.z - spot.z
      dvx = a.vx - spot.vx
      dvy = a.vy - spot.vy
      dvz = a.vz - spot.vz
      a.vx -= 2*((dvx*dx+dvy*dy+dvz*dz)/(dx**2+dy**2+dz**2))*dx
      a.vy -= 2*((dvx*dx+dvy*dy+dvz*dz)/(dx**2+dy**2+dz**2))*dy
      a.vz -= 2*((dvx*dx+dvy*dy+dvz*dz)/(dx**2+dy**2+dz**2))*dz
      return 1
    elif b in a.collision[t] and (dx*dvx) + (dy*dvy) + (dz*dvz) < 0:
      dx = a.x - b.x
      dy = a.y - b.y
      dz = a.z - b.z
      dvx = a.vx - b.vx
      dvy = a.vy - b.vy
      dvz = a.vz - b.vz
      mass1 = a.m
      mass2 = b.m
      a.vx -= ((2*mass2 / (mass1+mass2))*((dvx*dx+dvy*dy+dvz*dz)/(dx**2+dy**2+dz**2))) * dx
      a.vy -= ((2*mass2 / (mass1+mass2))*((dvx*dx+dvy*dy+dvz*dz)/(dx**2+dy**2+dz**2))) * dy
      a.vz -= ((2*mass2 / (mass1+mass2))*((dvx*dx+dvy*dy+dvz*dz)/(dx**2+dy**2+dz**2))) * dz
      b.vx += ((2*mass1 / (mass1+mass2))*((dvx*dx+dvy*dy+dvz*dz)/(dx**2+dy**2+dz**2))) * dx
      b.vy += ((2*mass1 / (mass1+mass2))*((dvx*dx+dvy*dy+dvz*dz)/(dx**2+dy**2+dz**2))) * dy
      b.vz += ((2*mass1 / (mass1+mass2))*((dvx*dx+dvy*dy+dvz*dz)/(dx**2+dy**2+dz**2))) * dz
      return 1
    else:
      return 0

#Simplify the calculation
def judge(a,b,c):
  if c == 0:
    t=0
    if a >= 0 and b >= 0:
      if a > b:
        t = b 
      else:
        t = a
    elif a < 0 and b >= 0:
      t = b
    elif a >= 0 and b < 0:
      t = a
    else:
      t = infinite
  elif c == 1:
    if a > b:
      t = a
    else:
      t = b
  else:
    if a > 0 and b > 0: 
      if a <= b:
        t = a
      else:
        t = b
    elif a > 0 or b > 0:
      if b > 0:
        t = b
      else:
        t = a
    else:
        t = infinite
  return t

def square_rooting(x,y):
  return math.sqrt(1 + (x / y) ** 2)

def start_bouncing(spheres, universe): #Start bouncing between spheres with each other and the universe
  seconds = float(sys.argv[2])
  timenext = []
  timeflow = 0
  energy = 0
  for sphere in spheres:
    energy += sphere.m * (sphere.vx**2) / 2 + sphere.m * (sphere.vy**2) / 2 + sphere.m * (sphere.vz**2) / 2

  print("Here are the initial conditions.")
  print("universe radius", universe.r)
  print("end simulation", seconds)
  for sphere in spheres:
    print(sphere.name,"m={:g} r={:g} p=({:g},{:g},{:g}) v=({:g},{:g},{:g}) ".format(sphere.m, sphere.r,sphere.x,sphere.y,sphere.z,sphere.vx,sphere.vy,sphere.vz))
  print("energy: {:g}".format(energy))
  print("momentum: ({:g},{:g},{:g})".format(momentum(spheres)[0],momentum(spheres)[1],momentum(spheres)[2]))
  print()
  print("Here are the events.")
  print()

  sphere_amount=len(spheres)
  while (True): #Since we don't know where to stop unless we get the next collision time, sys.exit(0) is used to go out of the program
    for sphere in spheres:
      timenext.append(sphere.collision_with_universe(universe))

    for i in range(sphere_amount):
      for j in range(sphere_amount):
        timenext.append(spheres[i].collision_with_sphere(spheres[j]))

    timenext = sorted(timenext)

    if timeflow == 0:
      for t in timenext:
        if t == 0:
          timenext.remove(t)

    min_time=timenext[0]

    seconds -= min_time
    if seconds < 0:
      sys.exit(0) #When approaching the simulation ending time, the program will exit with return code 0

    timeflow += min_time
    for sphere in spheres:
      sphere.new_position(min_time)

    collision = []
    for sphere in spheres:
      if timenext[0] in sphere.collision:
        collision.append(sphere)

    collision_amount=len(collision)
    i=0
    while i < collision_amount:
      j=0
      while j < collision_amount:
        if j > i:
          if collision[i].new_velocity(collision[j], min_time): #Check whether sphere collides with another sphere
            print("time of events: {:g}".format(timeflow))
            print("colliding", collision[i].name,collision[j].name)
            for sphere in spheres:
              print(sphere.name,"m={:g} r={:g} p=({:g},{:g},{:g}) v=({:g},{:g},{:g})".format(sphere.m, sphere.r,sphere.x,sphere.y,sphere.z,sphere.vx,sphere.vy,sphere.vz))
            print("energy: {:g}".format(energy))
            print("momentum: ({:g},{:g},{:g})".format(momentum(spheres)[0],momentum(spheres)[1],momentum(spheres)[2]))
            print()
        j+=1

      if collision[i].new_velocity(universe, min_time): #Check whether sphere collides with the universe
        print("time of events: {:g}".format(timeflow))
        print("reflecting", collision[i].name)
        for sphere in spheres:
          print(sphere.name,"m={:g} r={:g} p=({:g},{:g},{:g}) v=({:g},{:g},{:g})".format(sphere.m, sphere.r,sphere.x,sphere.y,sphere.z,sphere.vx,sphere.vy,sphere.vz))
        print("energy: {:g}".format(energy))
        print("momentum: ({:g},{:g},{:g})".format(momentum(spheres)[0],momentum(spheres)[1],momentum(spheres)[2]))
        print()
      i+=1

    for sphere in spheres:
      sphere.collision.clear()

    timenext.clear()

def momentum(spheres): #Calculate the total momentum
  m_x = 0
  m_y = 0
  m_z = 0
  for sphere in spheres:
    m_x += sphere.m * sphere.vx
    m_y += sphere.m * sphere.vy
    m_z += sphere.m * sphere.vz
  momentum_sequence = [m_x, m_y, m_z]
  return momentum_sequence

def initialize(): #Initialize the universe
  print("Please enter the mass, radius, x/y/z position, x/y/z velocity")
  print("and name of each sphere")
  print("When complete, use EOF / Ctrl-D to stop entering")

  wuti = []
  timeleft = float(sys.argv[2])
  line = []
  spheres = []
  m=0
  n=0
  k=0
  sphere_input = [x.strip() for x in sys.stdin.readlines()]
  
  while m<len(sphere_input):
    wuti.append([x for x in sphere_input[m].split()])
    m += 1
  
  while n<len(wuti):
    line.append(wuti[n][-1])
    wuti[n].pop()
    n += 1
  
  while k<len(wuti):
    wuti[k] = [float(x) for x in wuti[k]]
    k += 1
  
  spheres=circle(wuti,line)
  return spheres

def circle(a,b): #Change the spheres sequence order to the order we build in the code
  c=[]
  for i in range(len(a)):
    a[i].append(b[i])
  for i in range(len(a)):
    n = sphere(a[i][2],a[i][3],a[i][4],a[i][5],a[i][6],a[i][7],a[i][0],a[i][1],a[i][8])
    c.append(n)
  return c

if __name__=="__main__":
  #Check whether too many (or too few) fields on one line
  if len(sys.argv) == 3:
    pass
  else:
    sys.exit(1)

  universe_radius=sys.argv[1]
  
  #Check whether universe radius input is a valid number
  try:
    float(universe_radius)
  except:
    sys.exit(1)

  #Check whether total time input is a valid number
  try:
    float(sys.argv[2])
  except:
    sys.exit(1)

  universe = sphere(0,0,0,0,0,0,infinite,float(universe_radius),"universe")
  spheres = []
  spheres = initialize()
  start_bouncing(spheres, universe)  

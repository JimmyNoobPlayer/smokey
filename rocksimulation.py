script dump from a Discord session discussing some programming and simulation concepts, 24june2020




Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> pos = 1000
>>> vel = 0
>>> acc = 0.
>>> def update(time):
	//update velocity
	
SyntaxError: invalid syntax
>>> 
>>> def update(time):
	#update velocity delta_v = accel*time
	#update position
	#"update acceleration"

	vel += acc*time
	pos += acc*time*time + vel*time
	acc = 0.0

	
>>> update(1.)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    update(1.)
  File "<pyshell#17>", line 6, in update
    vel += acc*time
UnboundLocalError: local variable 'vel' referenced before assignment
>>> class rock(object):
	__init__(self):
		
SyntaxError: invalid syntax
>>> class rock(object):
	def __init__(self):
		self.pos = 1000.0
		self.vel = 0.0
		self.acc = 0.0

		
>>> r = rock()
>>> r
<__main__.rock object at 0x00000000039345C0>
>>> r.pos
1000.0
>>> r.acc
0.0
>>> r.acc = -1
>>> r.acc
-1
>>> rock2 = rock()
>>> rock2.acc
0.0
>>> r.acc
-1
>>> r2 = rock()
>>> r2.acc
0.0
>>> r.acc
-1
>>> r.acc
-1
>>> r2.acc
0.0
>>> r.acc += -9.8
>>> r.acc
-10.8
>>> r.acc = -9.8
>>> r2.acc += -9.8
>>> r2.acc
-9.8
>>> r3.acc
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    r3.acc
NameError: name 'r3' is not defined
>>> r3 = rock()
\
>>> r3.pos
1000.0
>>> r3.pos = 900.0
>>> r3.pos
900.0
>>> r3 = rock(1.5)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    r3 = rock(1.5)
TypeError: __init__() takes 1 positional argument but 2 were given
>>> r3 = rock()
>>> r1
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    r1
NameError: name 'r1' is not defined
>>> r1 = rock()
>>> def update(rock, time)r1 = rock()
SyntaxError: invalid syntax
>>> 
>>> class betterRock(object):
	def __init__(self, pos):
		self.pos = pos
		self.vel = 0.0
		self.acc = 0.0

		
>>> r = betterRock()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    r = betterRock()
TypeError: __init__() missing 1 required positional argument: 'pos'
>>> r = betterRock(1000.)
>>> r
<__main__.betterRock object at 0x0000000003934FD0>
>>> r.pos
1000.0
>>> class betterRock(object):
	def __init__():
		self.pos = 100.0
		self.vel = 0.0
		self.acc = 0.0

		
>>> r = betterRock()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    r = betterRock()
TypeError: __init__() takes 0 positional arguments but 1 was given
>>> r = rock()
>>> r.
SyntaxError: invalid syntax
r.
>>> r.acc
0.0
>>> r.pos
1000.0
>>> def update(x, time):
	x.vel += time*x.acc
	x.pos += (time*time*x.acc + time*x.vel)
	x.acc = 0.0 #just blanking out the acceleration variable so we can use it again next second.

	
>>> def p(rock):
	output = str(p.pos)
	output += str(p.vel)
	output += str(p.acc)

	
>>> p(r)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    p(r)
  File "<pyshell#87>", line 2, in p
    output = str(p.pos)
AttributeError: 'function' object has no attribute 'pos'
>>> def p(rock):
	output = str(rock.pos)
	output += str(rock.vel)
	output += str(rock.acc)

	
>>> p(r)
>>> print(p(r))
None
>>> r
<__main__.rock object at 0x00000000039345C0>
>>> def p(rock):
	output = str(rock.pos)
	output += str(rock.vel)
	output += str(rock.acc)
	print(output)

	
>>> p(r)
1000.00.00.0
>>> str(r)
'<__main__.rock object at 0x00000000039345C0>'
>>> str(100)
'100'
>>> print(str(100))
100
>>> def p(rock):
	output = (str(rock.pos) + ' ')
	output += (str(rock.vel) + ' ')
	output += (str(rock.acc) + ' ')
	print(output)

	
>>> p(r)
1000.0 0.0 0.0 
>>> update(r, 100)
>>> p(r)
1000.0 0.0 0.0 
>>> r.acc = -9.8
>>> update(r, 1)
>>> p(r)
980.4 -9.8 0.0 
>>> 
>>> r.acc = -9.8
>>> update(r,t)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    update(r,t)
NameError: name 't' is not defined
>>> update(r,1)
>>> p(r)
951.0 -19.6 0.0 
>>> #set the acceleration
>>> #update the rock using update()
>>> for i in range(0,100):
	r.acc = -9.8
	update(r,1)

	
>>> p(r)
-51478.99999999997 -999.5999999999982 0.0 
>>> 

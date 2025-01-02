#Julia


##Index
[1.Environments](###Environments)
[2.Modular Arithmetic](##Modular Arithmetic)
[Logic](###Logic)
[Looping](###Looping)





###Environments
####Julia REPL
type julia in terminal
REPL modes: 
normal mode:type backspace to enter,  enter code
help mode: type ? to enter
		enter any function 
package mode: type ] to enter

####Pluto
intalling Pluto:
inside the Julia REPL in package mode, type add Pluto

opening Pluto:
in normal mode type:
using Pluto
Pluto.run()


## Modular Arithmetic

###Chains of Expression
; can be used to seperate expression
the last expression will be executed
if a variable is r = (1; 2; 5+3) it also has the value of the last expression (8 in this case)
if no value is assigned to a variable it has the default value of 1

###Logic
bool: true, false
logical AND: &&
logical OR: ||
logical operators are shortcircuiting: if an expression is already guaranteed to be true or false Julia won't evaluate the rest of the code

bitwise OR: &
bitwise AND: ||
bitwise operators are not shortcircuiting

comparisons:
==: compares two values regardless of type
	- 5==5.0 : True
===: compares whether two values are identical in all aspects
	- 5===5.0 : False
	- 5 is an integer, 5.0 is a float, they are different types


###Looping

####while Blocks
while condition
	code
end
bsp: 
j = 0
while j < 5
    println(j^2)
    j = j + 1
end

##if Blocks
operators:
if
elsif
else



def a_fun():
    global name
    name = 'raman' 
def b_fun():
    global name
    name = 'simar'
b_fun()
a_fun()
print (name)

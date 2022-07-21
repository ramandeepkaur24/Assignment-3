def f():
    x=42
    def g():
            global x
    x=43
    print("Before calling g: ",x)
    g()
    print("After calling g: ",x)
f()


##output:-
##Before calling g:  43
##After calling g:  43

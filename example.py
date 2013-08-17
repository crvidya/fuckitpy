import fuckit
#import broke
fuckit(fuckit('broke'))

@fuckit
def broken_function():
    non_existant_variable # Let's create a NameError
    return 'Function decorator works'

@fuckit
class BrokenClass(object):
    def f(self):
        self.black_hole = 1 / 0
        return 'Class decorator works'
    
var = 'Context manager'
def broken_context_manager_function():
    with fuckit:
        asd
        return var + ' works'
    
print broken_function()
print broken_context_manager_function()
print BrokenClass().f()
print broke.var



    

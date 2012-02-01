#!/usr/bin/env python2

'''
Adapter class to make a dynamic shell from the CoffeePot API.
'''
from cmd import Cmd
from api import CoffeePot as CP

class CoffeePotCmd(Cmd):
    """
    Adapt cmdline to coffeepot API
    """
    prompt = "Greg@BrewingMachine #> "
    # List of commands that should not be public.
    bad_commands = ['sendAndReceive']
    
    def __init__(self, *args, **kwargs):
        self.coffeepot_instance = CP(kwargs['device'])
        self.__injectCoffeePotMethods()
        Cmd.__init__(self)

    def __injectCoffeePotMethods(self):
        """
        Injects API methods in do_* style
        """
        api_methods = [method for method in dir(CP) if not (method.startswith('_') or method in self.bad_commands)]
        for m in api_methods:
            def f(coffeepot_instance, x):
                def g(self, arg=None, opts=None):
                    print repr(getattr(coffeepot_instance, x)())
                g.__doc__ = getattr(coffeepot_instance, x).__doc__
                return g
            self.__dict__[('do_%s' % (m))] = f(self.coffeepot_instance, m)
 
    def emptyline(self):
        """Does not repeat last command when receiving an empty line"""
        pass
    def get_names(self):
        """Default get_names function does a dir(self.__class__), and injected methods does not show up."""
        return dir(self)

if __name__ == '__main__':
    app = CoffeePotCmd(device='/dev/ttyACM0')
    app.cmdloop()

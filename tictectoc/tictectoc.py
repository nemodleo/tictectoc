from timeit import default_timer
from datetime import timedelta
from typing import Union, Optional


class TicTecToc:
    MSG = '[TTT:{}] Elapsed time is'
    Temp_MSG = '[TTT:{}] Temp Elapsed time is'
    _timestamps: dict = None

    def __init__(self, name: Union[str, int] = 'default'):
        self._timestamps = dict()
        self._name = name

    def tic(self, name: Optional[Union[str, int]] = None):
        '''Start.'''
        if name is None:
            name = self._name
        name = str(name)
        if name not in self._timestamps:
            self._timestamps[name] = {
                'start': default_timer(),
                'elapsed': 0.
            }
        else: 
            self._timestamps[name]['start'] = default_timer()

    def i(self,*args, **kwargs):
        self.tic(*args, **kwargs)

    def tec(self, name: Optional[Union[str, int]] = None, msg: str = None, tmp_msg: str = None, verbose: int = 0):
        '''End temp.'''
        if name is None:
            name = self._name
        name = str(name)
        if name not in self._timestamps:
            return None
        if self._timestamps[name] is None:
            return None
        if self._timestamps[name]['start'] is None:
            return None
        if msg is None:
            msg = TicTecToc.MSG
        if tmp_msg is None:
            tmp_msg = TicTecToc.Temp_MSG
            
        start = self._timestamps[name]['start']
        elapsed = self._timestamps[name]['elapsed']
        end = default_timer()
        temp_elapsed = end - start
        elapsed += temp_elapsed
        self._timestamps[name]['start'] = None
        self._timestamps[name]['elapsed'] = elapsed

        if verbose == 1: 
            print(msg.format(name), timedelta(seconds=elapsed), tmp_msg.format(name), timedelta(seconds=temp_elapsed))

        if verbose == 2: 
            print(msg.format+ timedelta(seconds=elapsed))

        if verbose == 3: 
            print(tmp_msg.format(name), timedelta(seconds=temp_elapsed))

        return temp_elapsed, elapsed
    
    def e(self,*args, **kwargs):
        return self.tec(*args, **kwargs)

    def toc(self, name: Optional[Union[str, int]] = None, msg: str = None, verbose: int = 1):
        '''End.'''
        if name is None:
            name = self._name
        name = str(name)
        if name not in self._timestamps:
            return None
        if self._timestamps[name]['start'] is not None:
            self.tec(name)
        if msg is None:
            msg = TicTecToc.MSG

        elapsed = self._timestamps[name]['elapsed']
        if verbose == 1:
            print(msg.format(name), timedelta(seconds=elapsed))

        del self._timestamps[name]

        return elapsed

    def o(self,*args, **kwargs):
        return self.toc(*args, **kwargs)

    def __enter__(self):
        """Start the timer when using TicToc in a context manager."""
        self.tic()
    
    def __exit__(self, *args):
        """On exit, pring time elapsed since entering context manager."""
        self.toc()

    
    # decorator
    def dec(self, argument):
        def decorator(func):
            def wrapper(*args, **kwargs):
                self.tic(argument)
                result = func(*args, **kwargs)
                self.toc(argument)
                return result
            return wrapper
        return decorator
    

# init
ttt = TicTecToc()


# global func with abbreviation
tic = i = ttt.tic
tec = e = ttt.tec
toc = o = ttt.toc

dec = ttt.dec



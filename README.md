# tictectoc
Tic Tec Toc timing for Python.


## How to install
```
pip install tictectoc
```

## TicTecToc
1. TicToc
```
import time
from tictectoc import TicTecToc
t = TicTecToc()
t.tic()
time.sleep(1)
t.toc() # print '[TTT:default] Elapsed time is 0:00:01'

t.tic()
time.sleep(2)
t.toc() # print '[TTT:default] Elapsed time is 0:00:02'
```


2. TicTecToc
```
import time
from tictectoc import TicTecToc
t = TicTecToc()
for i in range(10):
    t.tic()
    time.sleep(1)
    t.tec()
t.toc() # print '[TTT:default] Elapsed time is 0:00:10'
```


3. TicTecToc with more than 1 timers
```
import time
from tictectoc import TicTecToc
t = TicTecToc()
for i in range(10):
    t.tic('timer0')
    t.tic('timer1')
    t.tic(100)
    time.sleep(1)
    t.tec('timer0')
    t.tec('timer1')
    t.tec(100)
t.toc('timer0') # print '[TTT:timer0] Elapsed time is 0:00:10'
t.toc('timer1') # print '[TTT:timer1] Elapsed time is 0:00:10'
t.toc(100)      # print '[TTT:100] Elapsed time is 0:00:10'
```
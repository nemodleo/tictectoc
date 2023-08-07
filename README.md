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


3. (a) TicTecToc with more than 1 timers
```
import time
from tictectoc import TicTecToc
t = TicTecToc()
t2 = TicTecToc('timer2')
for i in range(10):
    t.tic('timer0')
    t.tic('timer1')
    t.tic(100)
    t2.tic()
    time.sleep(1)
    t.tec('timer0')
    t.tec('timer1')
    t.tec(100)
    t2.tec()
t.toc('timer0') # print '[TTT:timer0] Elapsed time is 0:00:10'
t.toc('timer1') # print '[TTT:timer1] Elapsed time is 0:00:10'
t.toc(100)      # print '[TTT:100] Elapsed time is 0:00:10'
t2.toc()        # print '[TTT:timer2] Elapsed time is 0:00:10'
```


4. global instance 'ttt'
```
import time
from tictectoc import ttt
for i in range(10):
    ttt.tic()
    time.sleep(1)
    ttt.tec()
ttt.toc() # print '[TTT:default] Elapsed time is 0:00:10'
```


5. global function 'tic, tec, toc'
```
import time
from tictectoc import tic, tec, toc
for i in range(10):
    tic()
    time.sleep(1)
    tec()
toc() # print '[TTT:default] Elapsed time is 0:00:10'
```


5. abbreviation
```
import time
from tictectoc import TicTecToc
t = TicTecToc()
for i in range(10):
    t.i()
    time.sleep(1)
    t.e()
t.o() # print '[TTT:default] Elapsed time is 0:00:10'
```
```
import time
from tictectoc import ttt
for i in range(10):
    ttt.i()
    time.sleep(1)
    ttt.e()
ttt.o() # print '[TTT:default] Elapsed time is 0:00:10'
```
```
import time
from tictectoc import i, e, o
for i in range(10):
    i()
    time.sleep(1)
    e()
o() # print '[TTT:default] Elapsed time is 0:00:10'
```


6. decorator
```
import time
from tictectoc import ttt
@ttt.dec('timer0')
def function(n=10):
    for i in range(n):
        time.sleep(1)
function() # print '[TTT:timer0] Elapsed time is 0:00:10'
```
```
import time
from tictectoc import dec
@dec('timer0')
def function(n=1):
    for i in range(n):
        time.sleep(1)
        
function() # print '[TTT:timer0] Elapsed time is 0:00:10'
```

7. (a) with statement

```
import time
from tictectoc import TicTecToc
with TicTecToc():
    for i in range(10):
        time.sleep(1)
# print '[TTT::default] Elapsed time is 0:00:10'
```

```
import time
from tictectoc import ttt
with ttt:
    for i in range(10):
        time.sleep(1)
# print '[TTT::default] Elapsed time is 0:00:10'
```

7. (b) double with 
```
import time
from tictectoc import TicTecToc
with TicTecToc('timer0'):
    with TicTecToc('timer1'):
        time.sleep(10)
    time.sleep(10)
# print '[TTT::timer1] Elapsed time is 0:00:10'
# print '[TTT::timer0] Elapsed time is 0:00:20'
```

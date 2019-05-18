# SuperConsole
A Python package for doing stuff in the console

# Simple Usage
Printing:
```py
from superconsole import Console

Console.Out.Print ('Hello, World!')
```

Printing without newline:
```py
from superconsole import Console

Console.Out.Put ('Hello,')
Console.Out.Put (' World!')
```

Colors:
```py
from superconsole import Console

Console.Out.Print (Console.Color.Red + 'Hello, World!')
```

Awaiting user input:
```py
from superconsole import Console

if Console.In.Get ('Hello'):
  Console.Out.Print (Console.Logger.Success ('Message entered!'))
```

Clearing the console
```py
from superconsole import Console

Console.Clear ()
```

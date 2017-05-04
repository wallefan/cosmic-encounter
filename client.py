"""A slightly smarter telnet client that, if available, supports readline."""

import telnetlib
from telnetlib import IAC, WILL, DO, WONT, DONT
try:
    import readline
    old_readline_callback=readline.get_completer()
except ImportError:
    readline=None

def telnet_callback(sock, cmd, option):
    if option==OPTION_READLINE:
        if cmd==DO:
            # Telnet: do not acknowledge a request to enter a requeat we are already in
            if readline is not None and readline.get_completer() is not completer:
                old_completer=readline.get_completer()
                readline.set_completer(completer)
            sock.sendall(IAC+WILL+OPTION_READLINE)
        else:
             sock.sendall(IAC+WONT+OPTION_READLINE)
      elif cmd==DONT:
          if readline is not None and readline.get_completer() is completer:
              readline.set_completer(old_completer)
              sock.sendall(IAC+WONT+OPTION_READLINE)
      
    elif cmd==SE:
      if mode is None
      
              
          
             
           

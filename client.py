"""A slightly smarter telnet client that, if available, supports readline."""

import telnetlib
from telnetlib import IAC, WILL, DO, WONT, DONT, SB, SE
from curses.ascii import NAK
try:
    import readline
    old_readline_callback=readline.get_completer()
except ImportError:
    readline=None

def telnet_callback(sock, cmd, option):
    global tn, old_completer, completion_result
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
        s = tn.read_sb_data()
        opt = s[:1]
        data = s[1:]
        if opt == PARSE_AND_BIND:
            if readline is not None:
                readline.parse_and_bind(data.decode('ascii'))
            else:
                sock.sendall(IAC+WONT+OPTION_READLINE)
        elif opt == COMPLETION_MATCHES:
            completion_result = [r.decode('ascii') for r in data.split(COMPLETION_MATCH_SEP)]
            result_ready.set()
        else:
            sock.sendall(IAC+NAK)
        
    elif cmd == NAK:
        sock.sendall(IAC+SB+last_data+IAC+SE) # resend the last SB ... SE sent
    
    
              
def completer(text, nth):
    return get_completions(text, readline.get_line_buffer(), readline.get_begidx(), readline.get_endidx())[nth]

@functools.lru_cache(200)
def get_completions(text, buffer, begidx, endidx):
    to_send=text.encode('ascii')+SEP+buffer.encode('ascii')+SEP+begidx.to_bytes(2, 'little')+endidx.to_bytes(2, 'little')
    tn.get_socket().sendall(IAC+SB+COMPLETE+to_send+IAC+SE)
    last_data=COMPLETE+data
             
           

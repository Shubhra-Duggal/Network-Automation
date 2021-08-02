# Python

Start the interactive python interpreter. Capture the startup message and give the user control over the session.
The [code](/Code/python.py):

## Shebang 
```python
#!/usr/bin/env python
```
If there are multiple versions of python installed, /usr/bin/env ensures that the interpreter uses the first one on you environment's $PATH.

## pexpect.spawn
```python
import pexpect
```

```python
c = pexpect.spawnu('/usr/bin/env python')
```

This is the main class interface for Pexpect. Use this class to start and control child applications.

### spawnu
For python3 compatibility reasons, we are using spawnu and importing unicode_literals (above). spawnu accepts Unicode input and unicode_literals makes all string literals in this script Unicode by default.

### \_\_init\_\_
__init__(command, args=[], timeout=30, maxread=2000, searchwindowsize=None, logfile=None, cwd=None, env=None, ignore_sighup=False, echo=True, preexec_fn=None, encoding=None, codec_errors='strict', dimensions=None, use_poll=False)

This is a constructor. 

#### maxread
It is used to set the read buffer size, which is the maximum number of bytes that will be read from TTY at once. 
Setting it to 1 turns the buffering off.
When the output from the child is large then the value should be set to a higher value.

#### searchwindowsize
Default is None. Full buffer is searched at each iteration of receiving data.
It can be optimised (reduced) to reduce cost and increase efficiency. When expect() returns, the full buffer attribute is equal to the size of maxread irrespective of value of searchwindowsize.

#### timeout
Default is 30. TIMEOUT is raised when the specified time has elapsed, in seconds. If the value is None, TIMEOUT will not be raised and expect() might be blocked indefinitely until match is found.

#### logfile
Default is None, which stops the logging. When it is set to sys.stdout to echo everything to standard output. All input and output will be copied to the given file object. The logfile is flushed after each write.
The logfile_read and logfile_send can be used to separately log the input from the child and output sent to the child. The input and output from the child can be separatley logged using logfile_read and logfile_send.


#### delaybeforesend
If the user expect() a 'Password:' and then calls a sendline() to send the password, then the password is echoed back to them which is not normal. Now, stdin echo is switched off after the 'Password:' prompt. If a human types in a password it is not a problem but if password is sent before stdin echo is turned off, then password is echoed back. A delay can be introduced just before sending password.

#### close()
Exit status is stored in self.exitstatus and signal is stored in self.signalstatus. For the exit status of the child, call the close() method. 
If the child exited normally then exitstatus will store the exit return code and signalstatus will be None. 
If the child was terminated abnormally with a signal, then signalstatus will store the signal value and exitstatus will be None.

#### echo
It may be set to False to disable echoing of input. 
As a pseudo-terminal, all input echoed by the “keyboard” (send() or sendline()) will be repeated to output. 
Many times it is not desirable to have echo enabled, and it can be disabled later using setecho(False), followed by waitnoecho().



The child application is ready to talk. This does not interpret shell meta characters like redirect, pipeline or wild cards. You have to run shell and then use these.



## expect()

```python
c.expect('>>>')
```
expect(pattern, timeout=-1, searchwindowsize=-1, async_=False, **kw)


Traversal through the stream till a pattern is found. 
The pattern can be a StringType, EOF, a compiled re, or a list of any of those types. If the pattern is not a list then it returns index 0 on a successful match. This might raise exceptions for EOF or TIMEOUT. 
EOF or TIMEOUT exceptions can be avoided by adding EOF or TIMEOUT to the pattern list. Then EOF or TIMEOUT will be matched instead of raising an exception.

If you pass a list of patterns and more than one matches, the first match in the stream is chosen. If more than one pattern matches at that point, the leftmost in the pattern list is chosen.


## interact()
```python
print(''.join(reversed((c.before))))
print('Output is reversed.')
print()
print(c.after, end=' ')
c.interact()

c.kill(1)
print('is alive:', c.isalive())
```
interact(escape_character='\x1d', input_filter=None, output_filter=None)[source]

Gives control of the child process to the interactive user (the human at the keyboard). Keystrokes are sent to the child process, and the stdout and stderr output of the child process is printed. 
This simply echos the child stdout and child stderr to the real stdout and it echos the real stdin to the child stdin.

If a logfile is specified, then the data sent and received from the child process in interact mode is duplicated to the given log.

#### Input and output filter functions
Interact will always pass input_filter and output_filter bytes. Functions need to be wraped to decode and encode to UTF-8.
The output_filter is passed on all the output from the child process and the  input_filter on the keyboard input. The input_filter is run BEFORE the check for the escape_character.


## kill()
This sends the given signal to the child application. In keeping with UNIX tradition it has a misleading name. It does not necessarily kill the child unless you send the right signal.

---

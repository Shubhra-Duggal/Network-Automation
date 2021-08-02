#!/usr/bin/env python

import pexpect

c = pexpect.spawnu('/usr/bin/env python')

c.expect('>>>')
print(''.join(reversed((c.before))))
print('Output is reversed.')
print()
print(c.after, end=' ')
c.interact()
c.kill(1)
print('is alive:', c.isalive())

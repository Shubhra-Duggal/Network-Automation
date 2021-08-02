#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pexpect

c = pexpect.spawnu('/usr/bin/env python')

c.expect('>>>')
print('And now for something completely different...')
print(''.join(reversed((c.before))))
print('Yes, it\'s python, but it\'s backwards.')
print()
print('Escape character is \'^]\'.')
print(c.after, end=' ')
c.interact()
c.kill(1)
print('is alive:', c.isalive())
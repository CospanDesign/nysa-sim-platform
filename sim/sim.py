# Copyright (c) 2013 Dave McCoy (dave.mccoy@cospandesign.com)

# This file is part of Nysa (wiki.cospandesign.com/index.php?title=Nysa).
#
# Nysa is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# Nysa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Nysa; If not, see <http://www.gnu.org/licenses/>.

""" dionysus

Concrete interface for Nysa on the Dionysus platform
"""

__author__ = 'dave.mccoy@cospandesign.com (Dave McCoy)'

""" Changelog:
10/18/2013
    -Pep8ing the module and some cleanup
09/21/2012
    -added core dump function to retrieve the state of the master when a crash
    occurs
08/30/2012
    -Initial Commit
"""
import sys
import os
import time
from array import array as Array

from nysa.ibuilder.lib.gen_scripts.gen_sdb import GenSDB
from nysa.cbuilder.sdb import SDBError
from nysa.host.nysa import Nysa

class FauxNysa(Nysa):

    def __init__(self, dev_dict, status = None):
        Nysa.__init__(self, status)
        self.dev_dict = dev_dict

    def read(self, address, length = 1, memory_device = False, disable_auto_inc = False):
        ra = Array('B')
        length *= 4
        address *= 4
        count = 0
        for count in range (0, length, 4):
            if address + count < len(self.rom):
                ra.extend(self.rom[address + count :address + count + 4])
            else:
                ra.extend(Array('B'), [0x00, 0x00, 0x00, 0x00])

        return ra

    def write(self, address, data, memory_device=False, disable_auto_inc = False):
        return

    def ping(self):
        return

    def reset(self):
        return

    def read_sdb(self):
        """read_sdb

        Read the contents of the DRT

        Args:
          Nothing

        Returns (Array of bytes):
          the raw DRT data, this can be ignored for normal operation

        Raises:
          Nothing
        """

        gd = GenSDB()
        self.rom = gd.gen_rom(self.dev_dict, debug = False)
        self.nsm.read_sdb(self)

    def get_sdb_base_address(self):
        return 0x00

    def is_interrupt_for_slave(self, dev_id):
        return True

    def wait_for_interrupts(self, wait_time = 1):
        time.sleep(0.1)
        return True

    def register_interrupt_callback(self, index, callback):
        pass

    def unregister_interrupt_callback(self, index, callback = None):
        pass

    def upload(self, filepath):
        return

    def program (self):
        return

    def ioctl(self, name, arg = None):
        return

    def list_ioctl(self):
        return

    def get_sdb_base_address(self):
        return 0x00



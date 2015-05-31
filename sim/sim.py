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

    def read(self, address, length = 1, disable_auto_inc = False):
        if self.s: self.s.Verbose("Reading: 0x%08X, Length (Words): %d, Disable auto increment: %s" %
                (address, length, disable_auto_inc))
        ra = Array('B')
        length *= 4
        address *= 4
        count = 0
        for count in range (0, length, 4):
            if address + count < len(self.rom):
                ra.extend(self.rom[address + count :address + count + 4])
            else:
                ra.extend(Array('B', [0x00, 0x00, 0x00, 0x00]))

        return ra

    def write(self, address, data, disable_auto_inc = False):
        verbose_data = data
        if len(verbose_data) > 8:
            verbose_data = verbose_data[:8]
        if self.s: self.s.Verbose("Write: 0x%08X, %s, Disable Auto Inc: %s" %
                                    (address,
                                    data,
                                    disable_auto_inc))

    def ping(self):
        if self.s: self.s.Verbose("entered")

    def reset(self):
        if self.s: self.s.Verbose("entered")

    def is_programmed(self):
        return True

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
        if self.s: self.s.Verbose("entered")
        gd = GenSDB()
        self.rom = gd.gen_rom(self.dev_dict, debug = False)
        return self.nsm.read_sdb(self)

    def get_sdb_base_address(self):
        if self.s: self.s.Verbose("entered")
        return 0x00

    def is_interrupt_for_slave(self, dev_id):
        if self.s: self.s.Verbose("entered")
        return True

    def wait_for_interrupts(self, wait_time = 1):
        if self.s: self.s.Verbose("entered")
        time.sleep(0.1)
        return True

    def register_interrupt_callback(self, index, callback):
        if self.s: self.s.Verbose("entered")

    def unregister_interrupt_callback(self, index, callback = None):
        if self.s: self.s.Verbose("entered")

    def get_board_name(self):
        if self.s: self.s.Verbose("entered")
        return "sim"

    def upload(self, filepath):
        if self.s: self.s.Verbose("entered")
        return

    def program (self):
        if self.s: self.s.Verbose("entered")
        return

    def ioctl(self, name, arg = None):
        if self.s: self.s.Verbose("entered")
        return

    def list_ioctl(self):
        if self.s: self.s.Verbose("entered")
        return

    def get_sdb_base_address(self):
        if self.s: self.s.Verbose("entered")
        return 0x00



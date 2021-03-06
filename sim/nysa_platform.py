#Distributed under the MIT licesnse.
#Copyright (c) 2014 Dave McCoy (dave.mccoy@cospandesign.com)

#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#of the Software, and to permit persons to whom the Software is furnished to do
#so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

"""
Dionysus Interface
"""
__author__ = 'dave.mccoy@cospandesign.com (Dave McCoy)'

import sys
import os
import glob
#import yaml
import json
import hashlib


from nysa.host.nysa_platform import Platform
from sim import FauxNysa


class SimPlatform(Platform):
    def __init__(self, status = None):
        super (SimPlatform, self).__init__(status)

    def get_type(self):
        if self.status: self.status.Verbose("Returnig 'sim' type")
        return "sim"

    '''
    def scan(self):
        if self.status: self.status.Verbose("Scanning...")
        configs = self.find_all_sims()
        if self.status: self.status.Verbose("scan: %s" % str(configs))
        sim_dict = {}
        for f in configs:
            d = yaml.load(open(f, "r"))
            unique = os.path.split(f)[-1]
            unique = os.path.splitext(unique)[0]
            fn = FauxNysa(d)
            if self.status: self.status.Debug("\tFound: %s" % unique)
            sim_dict[unique] = fn

        return sim_dict

    def find_all_sims(self):
        return glob.glob(os.path.join(os.path.dirname(__file__),
                                      "images",
                                      "*.yaml"))
    '''

    def scan(self):
        if self.status: self.status.Verbose("Scanning...")
        configs = self.find_all_sims()
        if self.status: self.status.Verbose("scan: %s" % str(configs))
        sim_dict = {}

        for f in configs:
            d = json.load(open(f, "r"))
            unique = os.path.split(f)[-1]
            unique = os.path.splitext(unique)[0]
            fn = FauxNysa(d, self.status)
            fn.read_sdb()
            if self.status: self.status.Debug("\tFound: %s" % unique)
            sim_dict[unique] = fn

        return sim_dict

    def find_all_sims(self):
        return glob.glob(os.path.join(os.path.dirname(__file__),
                                        "images",
                                        "*.json"))

    def test_build_tools(self):
        return True

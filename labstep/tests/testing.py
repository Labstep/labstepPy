#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
from .experiment import Experiment

user = LS.login('demo@labstep.com','demopassword')

exp = user.getExperiment(23436)


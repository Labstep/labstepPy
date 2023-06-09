#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env.test'
load_dotenv(dotenv_path=env_path)

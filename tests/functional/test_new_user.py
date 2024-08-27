#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from labstep.entities.user.model import User
from labstep.entities.user.repository import newUser

from .fixtures import fixtures, new_email


class TestNewUser:

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_new_user(self):
        email1 = new_email()

        fresh_user = newUser(
            first_name='Team',
            last_name='Labstep',
            email=email1,
            password='gehwuigGHEUWIG123478!@$%£^@')

        newWorkspace = fresh_user.newWorkspace('New Workspace')

        fresh_user.setWorkspace(newWorkspace.id)

        newExperiment = fresh_user.newExperiment('New Experiment')






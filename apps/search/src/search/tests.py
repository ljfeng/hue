#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from nose.tools import assert_true, assert_equal

from desktop.lib.django_test_util import make_logged_in_client
from desktop.lib.test_utils import grant_access


class TestSearchBase(object):

  def setUp(self):
    self.c = make_logged_in_client(username='test_search', is_superuser=False)
    grant_access('test_search', 'test_search', 'search')
    self.user = User.objects.get(username='test_search')

    # To mock/monkey patch Resource


class TestWithMockedSolr(TestSearchBase):

  def test_index(self):
    self.c.get(reverse('search:index'))

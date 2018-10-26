# coding: utf-8

"""
    SignRequest API

    API for SignRequest.com

    OpenAPI spec version: v1
    Contact: tech-support@signrequest.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import signrequest_python_client
from signrequest_python_client.api.events_api import EventsApi  # noqa: E501
from signrequest_python_client.rest import ApiException


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = signrequest_python_client.api.events_api.EventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_events_list(self):
        """Test case for events_list

        Retrieve a list of Events  # noqa: E501
        """
        pass

    def test_events_read(self):
        """Test case for events_read

        Retrieve an Event  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    SignRequest API

    API for SignRequest.com

    OpenAPI spec version: v1
    Contact: tech-support@signrequest.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InviteMember(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email': 'str',
        'is_admin': 'bool',
        'is_owner': 'bool'
    }

    attribute_map = {
        'email': 'email',
        'is_admin': 'is_admin',
        'is_owner': 'is_owner'
    }

    def __init__(self, email=None, is_admin=False, is_owner=False):  # noqa: E501
        """InviteMember - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._is_admin = None
        self._is_owner = None
        self.discriminator = None

        self.email = email
        if is_admin is not None:
            self.is_admin = is_admin
        if is_owner is not None:
            self.is_owner = is_owner

    @property
    def email(self):
        """Gets the email of this InviteMember.  # noqa: E501


        :return: The email of this InviteMember.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InviteMember.


        :param email: The email of this InviteMember.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) < 1:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def is_admin(self):
        """Gets the is_admin of this InviteMember.  # noqa: E501


        :return: The is_admin of this InviteMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this InviteMember.


        :param is_admin: The is_admin of this InviteMember.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def is_owner(self):
        """Gets the is_owner of this InviteMember.  # noqa: E501


        :return: The is_owner of this InviteMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_owner

    @is_owner.setter
    def is_owner(self, is_owner):
        """Sets the is_owner of this InviteMember.


        :param is_owner: The is_owner of this InviteMember.  # noqa: E501
        :type: bool
        """

        self._is_owner = is_owner

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InviteMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
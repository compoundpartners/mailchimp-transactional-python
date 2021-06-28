# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.28
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_transactional.api_client import ApiClient

class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_key='', api_client = None):
        self.api_key = api_key
        if api_client:
            self.api_client = api_client
        else:
            self.api_client = ApiClient()

    def info(self, body = {}, **kwargs):  # noqa: E501
        """Get user info  # noqa: E501

        Return the information about the API-connected user.  # noqa: E501
        """
        (data) = self.info_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def info_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get user info  # noqa: E501

        Return the information about the API-connected user.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method info" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/users/info', 'POST',
            body=body_params,
            response_type='InlineResponse20069') # noqa: E501

    def ping(self, body = {}, **kwargs):  # noqa: E501
        """Ping  # noqa: E501

        Validate an API key and respond to a ping.  # noqa: E501
        """
        (data) = self.ping_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def ping_with_http_info(self, body, **kwargs):  # noqa: E501
        """Ping  # noqa: E501

        Validate an API key and respond to a ping.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ping" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/users/ping', 'POST',
            body=body_params,
            response_type='str') # noqa: E501

    def ping2(self, body = {}, **kwargs):  # noqa: E501
        """Ping 2  # noqa: E501

        Validate an API key and respond to a ping (JSON parser version).  # noqa: E501
        """
        (data) = self.ping2_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def ping2_with_http_info(self, body, **kwargs):  # noqa: E501
        """Ping 2  # noqa: E501

        Validate an API key and respond to a ping (JSON parser version).  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ping2" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/users/ping2', 'POST',
            body=body_params,
            response_type='InlineResponse20070') # noqa: E501

    def senders(self, body = {}, **kwargs):  # noqa: E501
        """List account senders  # noqa: E501

        Return the senders that have tried to use this account, both verified and unverified.  # noqa: E501
        """
        (data) = self.senders_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def senders_with_http_info(self, body, **kwargs):  # noqa: E501
        """List account senders  # noqa: E501

        Return the senders that have tried to use this account, both verified and unverified.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method senders" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/users/senders', 'POST',
            body=body_params,
            response_type='list[InlineResponse20040]') # noqa: E501

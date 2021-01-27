# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.21
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_transactional.api_client import ApiClient

class SendersApi(object):
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

    def add_domain(self, body = {}, **kwargs):  # noqa: E501
        """Add sender domain  # noqa: E501

        Adds a sender domain to your account. Sender domains are added automatically as you send, but you can use this call to add them ahead of time.  # noqa: E501
        """
        (data) = self.add_domain_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def add_domain_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add sender domain  # noqa: E501

        Adds a sender domain to your account. Sender domains are added automatically as you send, but you can use this call to add them ahead of time.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/senders/add-domain', 'POST',
            body=body_params,
            response_type='InlineResponse20042') # noqa: E501

    def check_domain(self, body = {}, **kwargs):  # noqa: E501
        """Check domain settings  # noqa: E501

        Checks the SPF and DKIM settings for a domain. If you haven't already added this domain to your account, it will be added automatically.  # noqa: E501
        """
        (data) = self.check_domain_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def check_domain_with_http_info(self, body, **kwargs):  # noqa: E501
        """Check domain settings  # noqa: E501

        Checks the SPF and DKIM settings for a domain. If you haven't already added this domain to your account, it will be added automatically.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/senders/check-domain', 'POST',
            body=body_params,
            response_type='InlineResponse20043') # noqa: E501

    def domains(self, body = {}, **kwargs):  # noqa: E501
        """List sender domains  # noqa: E501

        Returns the sender domains that have been added to this account.  # noqa: E501
        """
        (data) = self.domains_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def domains_with_http_info(self, body, **kwargs):  # noqa: E501
        """List sender domains  # noqa: E501

        Returns the sender domains that have been added to this account.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domains" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/senders/domains', 'POST',
            body=body_params,
            response_type='list[InlineResponse20041]') # noqa: E501

    def info(self, body = {}, **kwargs):  # noqa: E501
        """Get sender info  # noqa: E501

        Return more detailed information about a single sender, including aggregates of recent stats.  # noqa: E501
        """
        (data) = self.info_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def info_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get sender info  # noqa: E501

        Return more detailed information about a single sender, including aggregates of recent stats.  # noqa: E501
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
            '/senders/info', 'POST',
            body=body_params,
            response_type='InlineResponse20045') # noqa: E501

    def list(self, body = {}, **kwargs):  # noqa: E501
        """List account senders  # noqa: E501

        Return the senders that have tried to use this account.  # noqa: E501
        """
        (data) = self.list_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_with_http_info(self, body, **kwargs):  # noqa: E501
        """List account senders  # noqa: E501

        Return the senders that have tried to use this account.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/senders/list', 'POST',
            body=body_params,
            response_type='list[InlineResponse20040]') # noqa: E501

    def time_series(self, body = {}, **kwargs):  # noqa: E501
        """View sender history  # noqa: E501

        Return the recent history (hourly stats for the last 30 days) for a sender.  # noqa: E501
        """
        (data) = self.time_series_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def time_series_with_http_info(self, body, **kwargs):  # noqa: E501
        """View sender history  # noqa: E501

        Return the recent history (hourly stats for the last 30 days) for a sender.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method time_series" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/senders/time-series', 'POST',
            body=body_params,
            response_type='list[InlineResponse20046]') # noqa: E501

    def verify_domain(self, body = {}, **kwargs):  # noqa: E501
        """Verify domain  # noqa: E501

        Sends a verification email in order to verify ownership of a domain. Domain verification is a required step to confirm ownership of a domain. Once a domain has been verified in a Transactional API account, other accounts may not have their messages signed by that domain unless they also verify the domain. This prevents other Transactional API accounts from sending mail signed by your domain.  # noqa: E501
        """
        (data) = self.verify_domain_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def verify_domain_with_http_info(self, body, **kwargs):  # noqa: E501
        """Verify domain  # noqa: E501

        Sends a verification email in order to verify ownership of a domain. Domain verification is a required step to confirm ownership of a domain. Once a domain has been verified in a Transactional API account, other accounts may not have their messages signed by that domain unless they also verify the domain. This prevents other Transactional API accounts from sending mail signed by your domain.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/senders/verify-domain', 'POST',
            body=body_params,
            response_type='InlineResponse20044') # noqa: E501

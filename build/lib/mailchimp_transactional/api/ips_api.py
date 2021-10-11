# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.46
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_transactional.api_client import ApiClient

class IpsApi(object):
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

    def cancel_warmup(self, body = {}, **kwargs):  # noqa: E501
        """Cancel ip warmup  # noqa: E501

        Cancels the warmup process for a dedicated IP.  # noqa: E501
        """
        (data) = self.cancel_warmup_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def cancel_warmup_with_http_info(self, body, **kwargs):  # noqa: E501
        """Cancel ip warmup  # noqa: E501

        Cancels the warmup process for a dedicated IP.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_warmup" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/ips/cancel-warmup', 'POST',
            body=body_params,
            response_type='InlineResponse20020') # noqa: E501

    def check_custom_dns(self, body = {}, **kwargs):  # noqa: E501
        """Test custom dns  # noqa: E501

        Tests whether a domain name is valid for use as the custom reverse DNS for a dedicated IP.  # noqa: E501
        """
        (data) = self.check_custom_dns_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def check_custom_dns_with_http_info(self, body, **kwargs):  # noqa: E501
        """Test custom dns  # noqa: E501

        Tests whether a domain name is valid for use as the custom reverse DNS for a dedicated IP.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_custom_dns" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/ips/check-custom-dns', 'POST',
            body=body_params,
            response_type='InlineResponse20026') # noqa: E501

    def create_pool(self, body = {}, **kwargs):  # noqa: E501
        """Add ip pool  # noqa: E501

        Creates a pool and returns it. If a pool already exists with this name, no action will be performed.  # noqa: E501
        """
        (data) = self.create_pool_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def create_pool_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add ip pool  # noqa: E501

        Creates a pool and returns it. If a pool already exists with this name, no action will be performed.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_pool" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/ips/create-pool', 'POST',
            body=body_params,
            response_type='InlineResponse20024') # noqa: E501

    def delete(self, body = {}, **kwargs):  # noqa: E501
        """Delete ip address  # noqa: E501

        Deletes a dedicated IP. This is permanent and cannot be undone.  # noqa: E501
        """
        (data) = self.delete_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def delete_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete ip address  # noqa: E501

        Deletes a dedicated IP. This is permanent and cannot be undone.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/ips/delete', 'POST',
            body=body_params,
            response_type='InlineResponse20022') # noqa: E501

    def delete_pool(self, body = {}, **kwargs):  # noqa: E501
        """Delete ip pool  # noqa: E501

        Deletes a pool. A pool must be empty before you can delete it, and you cannot delete your default pool.  # noqa: E501
        """
        (data) = self.delete_pool_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def delete_pool_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete ip pool  # noqa: E501

        Deletes a pool. A pool must be empty before you can delete it, and you cannot delete your default pool.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_pool" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/ips/delete-pool', 'POST',
            body=body_params,
            response_type='InlineResponse20025') # noqa: E501

    def info(self, body = {}, **kwargs):  # noqa: E501
        """Get ip info  # noqa: E501

        Retrieves information about a single dedicated IP.  # noqa: E501
        """
        (data) = self.info_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def info_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get ip info  # noqa: E501

        Retrieves information about a single dedicated IP.  # noqa: E501
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
            '/ips/info', 'POST',
            body=body_params,
            response_type='InlineResponse20018') # noqa: E501

    def list(self, body = {}, **kwargs):  # noqa: E501
        """List ip addresses  # noqa: E501

        Lists your dedicated IPs.  # noqa: E501
        """
        (data) = self.list_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_with_http_info(self, body, **kwargs):  # noqa: E501
        """List ip addresses  # noqa: E501

        Lists your dedicated IPs.  # noqa: E501
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
            '/ips/list', 'POST',
            body=body_params,
            response_type='list[InlineResponse20017]') # noqa: E501

    def list_pools(self, body = {}, **kwargs):  # noqa: E501
        """List ip pools  # noqa: E501

        Lists your dedicated IP pools.  # noqa: E501
        """
        (data) = self.list_pools_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_pools_with_http_info(self, body, **kwargs):  # noqa: E501
        """List ip pools  # noqa: E501

        Lists your dedicated IP pools.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_pools" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/ips/list-pools', 'POST',
            body=body_params,
            response_type='list[InlineResponse20023]') # noqa: E501

    def pool_info(self, body = {}, **kwargs):  # noqa: E501
        """Get ip pool info  # noqa: E501

        Describes a single dedicated IP pool.  # noqa: E501
        """
        (data) = self.pool_info_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def pool_info_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get ip pool info  # noqa: E501

        Describes a single dedicated IP pool.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pool_info" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/ips/pool-info', 'POST',
            body=body_params,
            response_type='InlineResponse20024') # noqa: E501

    def provision(self, body = {}, **kwargs):  # noqa: E501
        """Request additional ip  # noqa: E501

        Requests an additional dedicated IP for your account. Accounts may have one outstanding request at any time, and provisioning requests are processed within 24 hours.  # noqa: E501
        """
        (data) = self.provision_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def provision_with_http_info(self, body, **kwargs):  # noqa: E501
        """Request additional ip  # noqa: E501

        Requests an additional dedicated IP for your account. Accounts may have one outstanding request at any time, and provisioning requests are processed within 24 hours.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method provision" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/ips/provision', 'POST',
            body=body_params,
            response_type='InlineResponse20019') # noqa: E501

    def set_custom_dns(self, body = {}, **kwargs):  # noqa: E501
        """Set custom dns  # noqa: E501

        Configures the custom DNS name for a dedicated IP.  # noqa: E501
        """
        (data) = self.set_custom_dns_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def set_custom_dns_with_http_info(self, body, **kwargs):  # noqa: E501
        """Set custom dns  # noqa: E501

        Configures the custom DNS name for a dedicated IP.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_custom_dns" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/ips/set-custom-dns', 'POST',
            body=body_params,
            response_type='InlineResponse20027') # noqa: E501

    def set_pool(self, body = {}, **kwargs):  # noqa: E501
        """Move ip to different pool  # noqa: E501

        Moves a dedicated IP to a different pool.  # noqa: E501
        """
        (data) = self.set_pool_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def set_pool_with_http_info(self, body, **kwargs):  # noqa: E501
        """Move ip to different pool  # noqa: E501

        Moves a dedicated IP to a different pool.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_pool" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/ips/set-pool', 'POST',
            body=body_params,
            response_type='InlineResponse20021') # noqa: E501

    def start_warmup(self, body = {}, **kwargs):  # noqa: E501
        """Start ip warmup  # noqa: E501

        Begins the warmup process for a dedicated IP. During the warmup process, the Transactional API will gradually increase the percentage of your mail that is sent over the warming-up IP, over a period of roughly 30 days. The rest of your mail will be sent over shared IPs or other dedicated IPs in the same pool.  # noqa: E501
        """
        (data) = self.start_warmup_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def start_warmup_with_http_info(self, body, **kwargs):  # noqa: E501
        """Start ip warmup  # noqa: E501

        Begins the warmup process for a dedicated IP. During the warmup process, the Transactional API will gradually increase the percentage of your mail that is sent over the warming-up IP, over a period of roughly 30 days. The rest of your mail will be sent over shared IPs or other dedicated IPs in the same pool.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_warmup" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/ips/start-warmup', 'POST',
            body=body_params,
            response_type='InlineResponse20020') # noqa: E501

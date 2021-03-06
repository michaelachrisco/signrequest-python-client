# coding: utf-8

"""
    SignRequest API

    API for SignRequest.com

    OpenAPI spec version: v1
    Contact: tech-support@signrequest.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from signrequest_client.api_client import ApiClient


class SignrequestsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def signrequests_cancel_signrequest(self, uuid, **kwargs):  # noqa: E501
        """Cancel a SignRequest  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signrequests_cancel_signrequest(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.signrequests_cancel_signrequest_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.signrequests_cancel_signrequest_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def signrequests_cancel_signrequest_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Cancel a SignRequest  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signrequests_cancel_signrequest_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method signrequests_cancel_signrequest" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `signrequests_cancel_signrequest`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/signrequests/{uuid}/cancel_signrequest/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse201',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def signrequests_create(self, data, **kwargs):  # noqa: E501
        """Create a SignRequest  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signrequests_create(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SignRequest data: (required)
        :return: SignRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.signrequests_create_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.signrequests_create_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def signrequests_create_with_http_info(self, data, **kwargs):  # noqa: E501
        """Create a SignRequest  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signrequests_create_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SignRequest data: (required)
        :return: SignRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method signrequests_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `signrequests_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/signrequests/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SignRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def signrequests_list(self, **kwargs):  # noqa: E501
        """Retrieve a list of SignRequests  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signrequests_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str who: 
        :param str from_email: 
        :param int page: A page number within the paginated result set.
        :param int limit: Number of results to return per page.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.signrequests_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.signrequests_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def signrequests_list_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of SignRequests  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signrequests_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str who: 
        :param str from_email: 
        :param int page: A page number within the paginated result set.
        :param int limit: Number of results to return per page.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['who', 'from_email', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method signrequests_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'who' in params:
            query_params.append(('who', params['who']))  # noqa: E501
        if 'from_email' in params:
            query_params.append(('from_email', params['from_email']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/signrequests/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def signrequests_read(self, uuid, **kwargs):  # noqa: E501
        """Retrieve a SignRequest  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signrequests_read(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: SignRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.signrequests_read_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.signrequests_read_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def signrequests_read_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve a SignRequest  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signrequests_read_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: SignRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method signrequests_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `signrequests_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/signrequests/{uuid}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SignRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def signrequests_resend_signrequest_email(self, uuid, **kwargs):  # noqa: E501
        """Resend a SignRequest  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signrequests_resend_signrequest_email(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.signrequests_resend_signrequest_email_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.signrequests_resend_signrequest_email_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def signrequests_resend_signrequest_email_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Resend a SignRequest  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signrequests_resend_signrequest_email_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method signrequests_resend_signrequest_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `signrequests_resend_signrequest_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/signrequests/{uuid}/resend_signrequest_email/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

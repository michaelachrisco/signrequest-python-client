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


class ApiTokensApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_tokens_create(self, data, **kwargs):  # noqa: E501
        """Create an API token  # noqa: E501

        You can create an API token in the [team api settings page](/#/teams). It is also possible to get or create a token using the REST api with your login credentials.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_tokens_create(data, async=True)
        >>> result = thread.get()

        :param async bool
        :param AuthToken data: (required)
        :return: AuthToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_tokens_create_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.api_tokens_create_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def api_tokens_create_with_http_info(self, data, **kwargs):  # noqa: E501
        """Create an API token  # noqa: E501

        You can create an API token in the [team api settings page](/#/teams). It is also possible to get or create a token using the REST api with your login credentials.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_tokens_create_with_http_info(data, async=True)
        >>> result = thread.get()

        :param async bool
        :param AuthToken data: (required)
        :return: AuthToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_tokens_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `api_tokens_create`")  # noqa: E501

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
            '/api-tokens/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthToken',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_tokens_delete(self, key, **kwargs):  # noqa: E501
        """Delete an API token  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_tokens_delete(key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str key: A unique value identifying this api token. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_tokens_delete_with_http_info(key, **kwargs)  # noqa: E501
        else:
            (data) = self.api_tokens_delete_with_http_info(key, **kwargs)  # noqa: E501
            return data

    def api_tokens_delete_with_http_info(self, key, **kwargs):  # noqa: E501
        """Delete an API token  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_tokens_delete_with_http_info(key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str key: A unique value identifying this api token. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_tokens_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if ('key' not in params or
                params['key'] is None):
            raise ValueError("Missing the required parameter `key` when calling `api_tokens_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

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
            '/api-tokens/{key}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_tokens_list(self, **kwargs):  # noqa: E501
        """Retrieve a list of API tokens  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_tokens_list(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: A page number within the paginated result set.
        :param int limit: Number of results to return per page.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_tokens_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_tokens_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_tokens_list_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of API tokens  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_tokens_list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: A page number within the paginated result set.
        :param int limit: Number of results to return per page.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_tokens_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/api-tokens/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_tokens_read(self, key, **kwargs):  # noqa: E501
        """Retrieve an API token  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_tokens_read(key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str key: A unique value identifying this api token. (required)
        :return: AuthToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_tokens_read_with_http_info(key, **kwargs)  # noqa: E501
        else:
            (data) = self.api_tokens_read_with_http_info(key, **kwargs)  # noqa: E501
            return data

    def api_tokens_read_with_http_info(self, key, **kwargs):  # noqa: E501
        """Retrieve an API token  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_tokens_read_with_http_info(key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str key: A unique value identifying this api token. (required)
        :return: AuthToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_tokens_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if ('key' not in params or
                params['key'] is None):
            raise ValueError("Missing the required parameter `key` when calling `api_tokens_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

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
            '/api-tokens/{key}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthToken',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

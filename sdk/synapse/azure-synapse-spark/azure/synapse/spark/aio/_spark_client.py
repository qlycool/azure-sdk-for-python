# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.synapse.spark.core.rest import AsyncHttpResponse, HttpRequest, _AsyncStreamContextManager
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import SparkClientConfiguration
from .operations import SparkBatchOperations
from .operations import SparkSessionOperations
from .. import models


class SparkClient(object):
    """SparkClient.

    :ivar spark_batch: SparkBatchOperations operations
    :vartype spark_batch: azure.synapse.spark.aio.operations.SparkBatchOperations
    :ivar spark_session: SparkSessionOperations operations
    :vartype spark_session: azure.synapse.spark.aio.operations.SparkSessionOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param endpoint: The workspace development endpoint, for example https://myworkspace.dev.azuresynapse.net.
    :type endpoint: str
    :param spark_pool_name: Name of the spark pool.
    :type spark_pool_name: str
    :param livy_api_version: Valid api-version for the request.
    :type livy_api_version: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        endpoint: str,
        spark_pool_name: str,
        livy_api_version: str = "2019-11-01-preview",
        **kwargs: Any
    ) -> None:
        base_url = '{endpoint}'
        self._config = SparkClientConfiguration(credential, endpoint, spark_pool_name, livy_api_version, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.spark_batch = SparkBatchOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.spark_session = SparkSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def send_request(self, request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `azure.synapse.spark.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from azure.synapse.spark.rest import build_get_spark_batch_jobs_request
        >>> request = build_get_spark_batch_jobs_request(spark_pool_name, livy_api_version, from_parameter, size, detailed)
        <HttpRequest [GET], url: '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/batches'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        For advanced cases, you can also create your own :class:`~azure.synapse.spark.core.rest.HttpRequest`
        and pass it in.

        :param request: The network request you want to make. Required.
        :type request: ~azure.synapse.spark.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.synapse.spark.core.rest.AsyncHttpResponse
        """
        request_copy = deepcopy(request)
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        if kwargs.pop("stream", False):
            return _AsyncStreamContextManager(
                client=self._client._pipeline,
                request=request_copy,
            )
        pipeline_response = await self._client._pipeline.run(request_copy._internal_request, **kwargs)
        response = AsyncHttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=request_copy,
            _internal_response=pipeline_response.http_response
        )
        await response.read()
        return response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SparkClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
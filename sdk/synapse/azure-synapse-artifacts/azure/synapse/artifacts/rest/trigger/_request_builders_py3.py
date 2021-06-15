# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, IO, Optional

from azure.core.pipeline.transport._base import _format_url_section
from azure.synapse.artifacts.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_get_triggers_by_workspace_request(**kwargs: Any) -> HttpRequest:
    """Lists triggers.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str (optional)",
                "value": [
                    {
                        "etag": "str (optional)",
                        "id": "str (optional)",
                        "name": "str (optional)",
                        "properties": "properties",
                        "type": "str (optional)"
                    }
                ]
            }
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/triggers")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_create_or_update_trigger_request_initial(
    trigger_name: str, *, json: Any = None, content: Any = None, if_match: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    """Creates or updates a trigger.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param trigger_name: The trigger name.
    :type trigger_name: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Trigger resource definition.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Trigger resource definition.
    :paramtype content: Any
    :keyword if_match: ETag of the trigger entity.  Should only be specified for update, for which
     it should match existing entity or can be * for unconditional update.
    :paramtype if_match: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            properties = {
                "": {
                    "str": "object (optional)"
                },
                "annotations": [
                    "object (optional)"
                ],
                "description": "str (optional)",
                "pipelines": [
                    {
                        "parameters": {
                            "str": "object (optional)"
                        },
                        "pipelineReference": {
                            "name": "str (optional)",
                            "referenceName": "str",
                            "type": "str"
                        }
                    }
                ],
                "runtimeState": "str (optional)",
                "type": "MultiplePipelineTrigger"
            }
            # OR
            properties = {
                "": {
                    "str": "object (optional)"
                },
                "annotations": [
                    "object (optional)"
                ],
                "dependsOn": [
                    {
                        "name": "str (optional)",
                        "referenceName": "str",
                        "type": "str"
                    }
                ],
                "description": "str (optional)",
                "pipeline": {
                    "parameters": {
                        "str": "object (optional)"
                    },
                    "pipelineReference": {
                        "name": "str (optional)",
                        "referenceName": "str",
                        "type": "str"
                    }
                },
                "runDimension": "str",
                "runtimeState": "str (optional)",
                "type": "ChainingTrigger"
            }
            # OR
            properties = {
                "": {
                    "str": "object (optional)"
                },
                "annotations": [
                    "object (optional)"
                ],
                "description": "str (optional)",
                "parentTrigger": "object",
                "requestedEndTime": "datetime",
                "requestedStartTime": "datetime",
                "rerunConcurrency": "int",
                "runtimeState": "str (optional)",
                "type": "RerunTumblingWindowTrigger"
            }
            # OR
            properties = {
                "": {
                    "str": "object (optional)"
                },
                "annotations": [
                    "object (optional)"
                ],
                "delay": "object (optional)",
                "dependsOn": [
                    {
                        "type": "TumblingWindowTrigger"
                    }
                ],
                "description": "str (optional)",
                "endTime": "datetime (optional)",
                "frequency": "str",
                "interval": "int",
                "maxConcurrency": "int",
                "pipeline": {
                    "parameters": {
                        "str": "object (optional)"
                    },
                    "pipelineReference": {
                        "name": "str (optional)",
                        "referenceName": "str",
                        "type": "str"
                    }
                },
                "retryPolicy": {
                    "count": "object (optional)",
                    "intervalInSeconds": "int (optional)"
                },
                "runtimeState": "str (optional)",
                "startTime": "datetime",
                "type": "TumblingWindowTrigger"
            }

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "etag": "str (optional)",
                "id": "str (optional)",
                "name": "str (optional)",
                "properties": "properties",
                "type": "str (optional)"
            }

            # response body for status code(s): 200
            response.json() == {
                "etag": "str (optional)",
                "id": "str (optional)",
                "name": "str (optional)",
                "properties": "properties",
                "type": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/triggers/{triggerName}")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url(
            "trigger_name",
            trigger_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_match is not None:
        header_parameters["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="PUT", url=url, params=query_parameters, headers=header_parameters, json=json, content=content, **kwargs
    )


def build_get_trigger_request(trigger_name: str, *, if_none_match: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    """Gets a trigger.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param trigger_name: The trigger name.
    :type trigger_name: str
    :keyword if_none_match: ETag of the trigger entity. Should only be specified for get. If the
     ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    :paramtype if_none_match: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "etag": "str (optional)",
                "id": "str (optional)",
                "name": "str (optional)",
                "properties": "properties",
                "type": "str (optional)"
            }
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/triggers/{triggerName}")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url(
            "trigger_name",
            trigger_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_none_match is not None:
        header_parameters["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_delete_trigger_request_initial(trigger_name: str, **kwargs: Any) -> HttpRequest:
    """Deletes a trigger.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param trigger_name: The trigger name.
    :type trigger_name: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/triggers/{triggerName}")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url(
            "trigger_name",
            trigger_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_subscribe_trigger_to_events_request_initial(trigger_name: str, **kwargs: Any) -> HttpRequest:
    """Subscribe event trigger to events.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param trigger_name: The trigger name.
    :type trigger_name: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "status": "str (optional)",
                "triggerName": "str (optional)"
            }
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/triggers/{triggerName}/subscribeToEvents")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url(
            "trigger_name",
            trigger_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_get_event_subscription_status_request(trigger_name: str, **kwargs: Any) -> HttpRequest:
    """Get a trigger's event subscription status.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param trigger_name: The trigger name.
    :type trigger_name: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "status": "str (optional)",
                "triggerName": "str (optional)"
            }
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/triggers/{triggerName}/getEventSubscriptionStatus")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url(
            "trigger_name",
            trigger_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_unsubscribe_trigger_from_events_request_initial(trigger_name: str, **kwargs: Any) -> HttpRequest:
    """Unsubscribe event trigger from events.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param trigger_name: The trigger name.
    :type trigger_name: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "status": "str (optional)",
                "triggerName": "str (optional)"
            }
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/triggers/{triggerName}/unsubscribeFromEvents")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url(
            "trigger_name",
            trigger_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_start_trigger_request_initial(trigger_name: str, **kwargs: Any) -> HttpRequest:
    """Starts a trigger.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param trigger_name: The trigger name.
    :type trigger_name: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/triggers/{triggerName}/start")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url(
            "trigger_name",
            trigger_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_stop_trigger_request_initial(trigger_name: str, **kwargs: Any) -> HttpRequest:
    """Stops a trigger.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param trigger_name: The trigger name.
    :type trigger_name: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/triggers/{triggerName}/stop")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url(
            "trigger_name",
            trigger_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)
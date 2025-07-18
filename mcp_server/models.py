# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T10:56:09+00:00

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import AnyUrl, BaseModel, Field, constr


class ContentV1Content(BaseModel):
    account_sid: Optional[
        constr(pattern=r'^AC[0-9a-fA-F]{32}$', min_length=34, max_length=34)
    ] = Field(
        None,
        description='The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource.',
    )
    date_created: Optional[datetime] = Field(
        None,
        description='The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.',
    )
    date_updated: Optional[datetime] = Field(
        None,
        description='The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.',
    )
    friendly_name: Optional[str] = Field(
        None,
        description='A string name used to describe the Content resource. Not visible to the end recipient.',
    )
    language: Optional[str] = Field(
        None,
        description='Two-letter (ISO 639-1) language code (e.g., en) identifying the language the Content resource is in.',
    )
    links: Optional[Dict[str, Any]] = Field(
        None,
        description='A list of links related to the Content resource, such as approval_fetch and approval_create',
    )
    sid: Optional[
        constr(pattern=r'^HX[0-9a-fA-F]{32}$', min_length=34, max_length=34)
    ] = Field(
        None,
        description='The unique string that that we created to identify the Content resource.',
    )
    types: Optional[Any] = Field(
        None,
        description='The [Content types](https://www.twilio.com/docs/content-api/content-types-overview) (e.g. twilio/text) for this Content resource.',
    )
    url: Optional[AnyUrl] = Field(
        None,
        description='The URL of the resource, relative to `https://content.twilio.com`.',
    )
    variables: Optional[Any] = Field(
        None,
        description='Defines the default placeholder values for variables included in the Content resource. e.g. {"1": "Customer_Name"}.',
    )


class ContentV1ContentApprovalFetch(BaseModel):
    account_sid: Optional[
        constr(pattern=r'^AC[0-9a-fA-F]{32}$', min_length=34, max_length=34)
    ] = Field(
        None,
        description='The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource.',
    )
    sid: Optional[
        constr(pattern=r'^HX[0-9a-fA-F]{32}$', min_length=34, max_length=34)
    ] = Field(
        None,
        description='The unique string that that we created to identify the Content resource.',
    )
    url: Optional[AnyUrl] = Field(
        None,
        description='The URL of the resource, relative to `https://content.twilio.com`.',
    )
    whatsapp: Optional[Any] = Field(
        None,
        description='Contains the whatsapp approval information for the Content resource, with fields such as approval status, rejection reason, and category, amongst others.',
    )


class ContentV1ContentAndApprovals(BaseModel):
    account_sid: Optional[
        constr(pattern=r'^AC[0-9a-fA-F]{32}$', min_length=34, max_length=34)
    ] = Field(
        None,
        description='The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource.',
    )
    approval_requests: Optional[Any] = Field(
        None,
        description='The submitted information and approval request status of the Content resource.',
    )
    date_created: Optional[datetime] = Field(
        None,
        description='The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.',
    )
    date_updated: Optional[datetime] = Field(
        None,
        description='The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.',
    )
    friendly_name: Optional[str] = Field(
        None,
        description='A string name used to describe the Content resource. Not visible to the end recipient.',
    )
    language: Optional[str] = Field(
        None,
        description='Two-letter (ISO 639-1) language code (e.g., en) identifying the language the Content resource is in.',
    )
    sid: Optional[
        constr(pattern=r'^HX[0-9a-fA-F]{32}$', min_length=34, max_length=34)
    ] = Field(
        None,
        description='The unique string that that we created to identify the Content resource.',
    )
    types: Optional[Any] = Field(
        None,
        description='The [Content types](https://www.twilio.com/docs/content-api/content-types-overview) (e.g. twilio/text) for this Content resource.',
    )
    variables: Optional[Any] = Field(
        None,
        description='Defines the default placeholder values for variables included in the Content resource. e.g. {"1": "Customer_Name"}.',
    )


class ContentV1LegacyContent(BaseModel):
    account_sid: Optional[
        constr(pattern=r'^AC[0-9a-fA-F]{32}$', min_length=34, max_length=34)
    ] = Field(
        None,
        description='The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource.',
    )
    date_created: Optional[datetime] = Field(
        None,
        description='The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.',
    )
    date_updated: Optional[datetime] = Field(
        None,
        description='The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.',
    )
    friendly_name: Optional[str] = Field(
        None,
        description='A string name used to describe the Content resource. Not visible to the end recipient.',
    )
    language: Optional[str] = Field(
        None,
        description='Two-letter (ISO 639-1) language code (e.g., en) identifying the language the Content resource is in.',
    )
    legacy_body: Optional[str] = Field(
        None,
        description='The string body field of the legacy content template associated with this Content resource',
    )
    legacy_template_name: Optional[str] = Field(
        None,
        description='The string name of the legacy content template associated with this Content resource, unique across all template names for its account.  Only lowercase letters, numbers and underscores are allowed',
    )
    sid: Optional[
        constr(pattern=r'^HX[0-9a-fA-F]{32}$', min_length=34, max_length=34)
    ] = Field(
        None,
        description='The unique string that that we created to identify the Content resource.',
    )
    types: Optional[Any] = Field(
        None,
        description='The [Content types](https://www.twilio.com/docs/content-api/content-types-overview) (e.g. twilio/text) for this Content resource.',
    )
    url: Optional[AnyUrl] = Field(
        None,
        description='The URL of the resource, relative to `https://content.twilio.com`.',
    )
    variables: Optional[Any] = Field(
        None,
        description='Defines the default placeholder values for variables included in the Content resource. e.g. {"1": "Customer_Name"}.',
    )


class Meta(BaseModel):
    first_page_url: Optional[AnyUrl] = None
    key: Optional[str] = None
    next_page_url: Optional[AnyUrl] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
    previous_page_url: Optional[AnyUrl] = None
    url: Optional[AnyUrl] = None


class V1ContentGetResponse(BaseModel):
    contents: Optional[List[ContentV1Content]] = None
    meta: Optional[Meta] = None


class V1ContentAndApprovalsGetResponse(BaseModel):
    contents: Optional[List[ContentV1ContentAndApprovals]] = None
    meta: Optional[Meta] = None


class V1LegacyContentGetResponse(BaseModel):
    contents: Optional[List[ContentV1LegacyContent]] = None
    meta: Optional[Meta] = None

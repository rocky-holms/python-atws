from pytz import timezone
USE_REQUEST_TRANSPORT_TYPE = True
REQUEST_TRANSPORT_TRANSIENT_ERROR_RETRIES = 5
REQUEST_TRANSPORT_TIMEOUT_CONNECT_WAIT = 4
REQUEST_TRANSPORT_TIMEOUT_RESPONSE_WAIT = 27
DISABLE_SSL_WARNINGS = True
SUPPORTED_SUDS_VERSION = 0.7
LOCAL_TZ='Europe/London'
AUTOTASK_API_TZ = 'US/Eastern'
LOCAL_TIMEZONE = timezone(LOCAL_TZ)

MONKEY_PATCHING_ENABLED = True

AUTOTASK_API_TIMEZONE = timezone(AUTOTASK_API_TZ)
AUTOTASK_API_BASE_URL = 'https://webservices.autotask.net/atservices/1.5/atws.wsdl'
AUTOTASK_API_QUERY_RESULT_LIMIT = 500
AUTOTASK_API_QUERY_ID_LIMIT = 200
AUTOTASK_API_QUERY_DATEFORMAT = "%Y-%m-%d %H:%M:%S"
AUTOTASK_API_ENTITY_SEND_LIMIT = 200

AUTOTASK_QUERY_XML_SPACING = 3

WRAPPER_DISABLE_CLEAN_ENTITIES = False
WRAPPER_BULK_UPDATE_ENABLED = True
WRAPPER_DEFAULT_GET_ALL_ENTITIES = True
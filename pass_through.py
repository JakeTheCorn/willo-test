import copy

PRIVACY_SETTINGS = {
  'private': {
    'fields': {
      'allow': ['user_id']
    }
  },
  'partial': {
    'fields': {
      'allow': ['user_id', 'first_name', 'last_name']
    }
  },
  'not-private': {
    'fields': {
      'allow': ['user_id', 'first_name', 'last_name', 'email']
    }
  }
}

def pass_through(*, privacy_setting: str, body: dict):
  if not isinstance(body, dict):
    return None, TypeError('body must be type dict')
  if not isinstance(privacy_setting, str):
    return None, TypeError('privacy_setting must be type string')
  if privacy_setting not in PRIVACY_SETTINGS:
    return None, ValueError('privacy_setting must be one of %s' % PRIVACY_SETTINGS.keys())
  if privacy_setting == 'not-private':
    return __delete_unallowed_fields(
      privacy_setting=privacy_setting,
      body=body
    )
  if privacy_setting == 'private':
    return __delete_unallowed_fields(
      privacy_setting=privacy_setting,
      body=body
    )
  if privacy_setting == 'partial':
    return __delete_unallowed_fields(
      privacy_setting=privacy_setting,
      body=body,
    )

def __delete_unallowed_fields(*, body: dict, privacy_setting: str):
  body_keys = body.keys()
  allowed_fields = PRIVACY_SETTINGS[privacy_setting]['fields'].get('allow')
  _copy = copy.copy(body)
  warn_msg = ''

  if not isinstance(allowed_fields, list):
    return None, Exception(f'Could not find config for privacy setting {privacy_setting}' )

  for body_key in body_keys:
    if body_key in allowed_fields:
      continue
    warn_msg += f'Field not allowed: {body_key}. removing... \n'
    if body_key not in _copy:
      continue
    del _copy[body_key]

  return _copy, None if len(warn_msg) == 0 else Warning(warn_msg)

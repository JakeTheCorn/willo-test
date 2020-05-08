from typing import Any
import json

VALID_OUTPUT_FORMATS = ['json', 'flat']

def format_data(*, output_format: str, data: dict):
  if not isinstance(output_format, str) or output_format not in VALID_OUTPUT_FORMATS:
    return None, ValueError('output_format must be one of: json, flat. received %s' % output_format)
  if not isinstance(data, dict):
    return None, TypeError(f'data must be type dict. received {data.__class__.__name__}')
  if output_format == 'json':
    return safe_json_dumps(data)
  if output_format == 'flat':
    return flat_parse(data)
  return None, Exception('Unexpected error occured in format_data')

def safe_json_dumps(v: Any):
  try:
    return json.dumps(v), None
  except Exception as err:
    return None, err

def flat_parse(v: Any):
  if not isinstance(v, dict):
    return None, TypeError('flat_parse expected type dict')
  res = ''
  for key in v:
    val = v.get(key)
    if isinstance(val, (list, dict)):
      row_data, err = safe_json_dumps(val)
      if err:
        return None, err
    res += f'{key}={str(val)}\n'
  return res, None

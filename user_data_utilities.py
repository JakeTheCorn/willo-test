import json

def write_json_file(*, data: str, user_id):
  try:
    with open(f'data/users.{user_id}.json', 'w') as outfile:
      json.dump(json.loads(data), outfile)
    return None
  except Exception as err:
    return err

def write_flat_file(*, data: str, user_id):
  try:
    with open(f'data/users.{user_id}.flat', 'w') as outfile:
      lines = data.split('\n')
      num_lines = len(lines)
      for idx, line in enumerate(lines):
        if (idx + 1) == num_lines:
          outfile.write(line)
        else:
          outfile.write(line + '\n')
    return None
  except Exception as err:
    return err


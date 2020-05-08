import json
from flask import Flask, request

from pass_through import pass_through
from format_data import format_data
from user_data_utilities import write_flat_file, write_json_file
from Responder import Responder

app = Flask(__name__)

@app.route('/ping')
def ping():
  return 'pong'

@app.route('/provision', methods=['POST'])
def provision():
  responder = Responder()

  request_data = request.get_json()
  pass_through_data, err = pass_through(
    privacy_setting=request_data.get('privacy_setting'),
    body=request_data.get('body')
  )

  if err:
    if not isinstance(err, Warning):
      msg = 'Error parsing user data'
      print(msg, err)
      return responder.error(msg)
    responder.append_warning(err)

  user_id = pass_through_data.get('user_id')

  if user_id is None:
    return responder.error('No user_id found. Cannot write user data')

  output_format = request_data.get('output_format')

  writable_data, err = format_data(
    output_format=output_format,
    data=pass_through_data
  )

  if err:
    msg = 'Error formating user data'
    print(msg, err)
    return responder.error(msg)

  if output_format == 'json':
    err = write_json_file(
      data=writable_data,
      user_id=user_id
    )
    if err:
      msg = 'Error writing user json file'
      print(msg, err)
      return responder.error(msg)
    return responder.create_success()

  err = write_flat_file(
    data=writable_data,
    user_id=user_id
  )

  if err:
    msg = 'Error writing flat file'
    print(msg, err)
    return responder.error(msg)
  return responder.create_success()

if __name__ == '__main__':
  app.run()

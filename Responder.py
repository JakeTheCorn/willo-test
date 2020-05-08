HttpStatus = {
  'Created': 201,
  'Error': 500
}

class Responder(object):
  def __init__(self):
    self.__warnings = []

  def append_warning(warning):
    self.__warnings.append(warning)

  def create_success(self, msg = 'Success'):
    return {
      'status': HttpStatus['Created'],
      'message': msg,
      'warnings': self.__warnings
    }

  def error(self, msg):
    return {
      'status': HttpStatus['Error'],
      'message': msg,
      'warnings': self.__warnings
    }

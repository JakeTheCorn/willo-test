import unittest
import json
from format_data import format_data

class FormatDataTest(unittest.TestCase):
  def test_valid_output_format(self):
    _data, err = format_data(
      output_format=None,
      data={},
    )
    self.assertRegex(str(err), r'output_format must be one of: json, flat. received ')
    _data, err = format_data(
      output_format='csv',
      data={},
    )
    self.assertRegex(str(err), r'output_format must be one of: json, flat. received csv')

  def test_valid_data_type(self):
    _data, err = format_data(
      output_format='json',
      data=1,
    )
    self.assertRegex(str(err), r'data must be type dict. received ')

  def test_format_json(self):
    data = {
      'name': 'bill'
    }
    result, _err = format_data(
      output_format='json',
      data=data
    )
    expectation = json.dumps(data)
    self.assertEqual(result, expectation)

  def test_format_flat(self):
    data = {
      'name': 'bill',
      'age': 45
    }
    result, _err = format_data(
      output_format='flat',
      data=data
    )
    expectation = 'name=bill\nage=45\n'
    self.assertEqual(result, expectation)

if __name__ == '__main__':
  unittest.main()

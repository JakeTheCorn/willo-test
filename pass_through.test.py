import unittest
from pass_through import pass_through

class Test(unittest.TestCase):
  def test_body_type(self):
    _data, err = pass_through(
      privacy_setting='private',
      body=None
    )
    self.assertRegex(str(err), 'body must be type dict')

  def test_privacy_setting_type(self):
    _data, err = pass_through(
      privacy_setting=None,
      body={}
    )
    self.assertRegex(str(err), r'privacy_setting must be type string')

  def test_privacy_setting_value(self):
    _data, err = pass_through(
      privacy_setting='a',
      body={}
    )
    self.assertRegex(str(err), r'privacy_setting must be one of ')

  def test_private(self):
    data, err = pass_through(
      privacy_setting='private',
      body={
        'email': 'a@a.com',
        'first_name': 'bill',
        'last_name': 'bob',
        'user_id': 1
      }
    )
    self.assertEqual(data, {'user_id': 1})
    self.assertIsInstance(err, Warning)

  def test_partial(self):
    data, err = pass_through(
      privacy_setting='partial',
      body={
        'email': 'a@a.com',
        'first_name': 'bill',
        'last_name': 'bob',
        'user_id': 1
      }
    )
    self.assertEqual(data, {
      'user_id': 1,
      'first_name': 'bill',
      'last_name': 'bob',
    })
    self.assertIsInstance(err, Warning)

  def test_not_private(self):
    body = {
      'email': 'a@a.com',
      'first_name': 'bill',
      'last_name': 'bob',
      'user_id': 1,
      'extraneous_key': True
    }
    data, err = pass_through(
      privacy_setting='not-private',
      body=body
    )
    del body['extraneous_key']
    self.assertEqual(data, body)
    self.assertIsInstance(err, Warning)


unittest.main()

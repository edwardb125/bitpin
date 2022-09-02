# Usage:
# python -m unittest discover

from unittest import TestCase, mock, result
import unittest
import utils


mock_collection = {}
updated = False


class Content:
    def find(self):
        return [
            {
                'title': 'Crypto',
            },
            {
                'title': 'Bitcoin',
            }    
        ]

    
    def find_one(self, title):
        return {
                'title': 'Crypto',
                'vote': 1000,
                'score': 4.5
            }


    def update_one(self, title, object):
        global updated
        updated = True


class Form():
    def get(self, key):
        return 2


class Request():
    form = Form()


class TestApi(TestCase):
    def setUp(self):
        global mock_collection
        mock_collection = Content()

    def test_init(self):
        result = utils.init(mock_collection)
        self.assertEqual(result, {'Crypto': -1, 'Bitcoin': -1})


    def test_list_function(self):
        result = utils.list_function(mock_collection)
        self.assertEqual(result[0][0]['title'], 'Crypto')

    
    def test_update_vote(self):
        utils.update_vote(mock_collection, 'Crypto', 4)
        self.assertEqual(updated, True)

    @mock.patch('utils.update_vote')
    def test_add_vote_function(self, mock_update_vote):
        request = Request()
        mock_update_vote.return_value = True
        result = utils.add_vote_function(mock_collection, request)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
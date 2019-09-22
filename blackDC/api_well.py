from rest_framework.response import Response
from rest_framework.status import \
    HTTP_400_BAD_REQUEST, \
    HTTP_404_NOT_FOUND


import os
import json

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'one_example.json')
one_example = open(file_path)
data = json.load(one_example)


def get_one(request):
    """
    Get one well
    :return: Json of well
    """
    global data
    return data




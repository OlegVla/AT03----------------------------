import pytest
import requests
from requests.models import Response
from unittest.mock import Mock

from main1 import get_cat_image_by_breed  # Замените 'your_module' на имя вашего модуля


def test_get_cat_image_by_breed_404(mocker):
    # Mock the requests.get method
    mock_get = mocker.patch('requests.get')

    # Create a mock response object with status code 404
    mock_response = Mock(spec=Response)
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    breed_id = "abys"  # Example breed ID
    result = get_cat_image_by_breed(breed_id)

    # Assert that the result is None when the status code is 404
    assert result is None


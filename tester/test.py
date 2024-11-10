# tester/test.py
import requests
import time
import sys

def wait_for_nginx():
    """Wait for Nginx to become available."""
    max_retries = 30
    retries = 0
    while retries < max_retries:
        try:
            requests.get('http://nginx:80')
            return True
        except requests.exceptions.ConnectionError:
            print("Waiting for Nginx to start...")
            time.sleep(1)
            retries += 1
    return False

def test_servers():
    """Test both Nginx servers."""
    # Wait for Nginx to start
    if not wait_for_nginx():
        print("Nginx failed to start")
        sys.exit(1)

    try:
        # Test server 1 (port 80)
        response = requests.get('http://nginx:80')
        assert response.status_code == 200, f"Server 1 returned {response.status_code}, expected 200"
        assert "Welcome to Server 1" in response.text, "Server 1 content not found"
        print("✅ Server 1 test passed")

        # Test server 2 (port 8080)
        response = requests.get('http://nginx:8080')
        assert response.status_code == 404, f"Server 2 returned {response.status_code}, expected 404"
        print("✅ Server 2 test passed")

        print("All tests passed! 🎉")
        return True

    except AssertionError as e:
        print(f"❌ Test failed: {str(e)}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_servers()
    sys.exit(0 if success else 1)



# import requests
# import sys
# import time
# import logging
# from typing import Tuple, Dict
#
# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger(__name__)
#
#
# def check_server_response(url: str, expected_code: int, expected_content: str = None) -> Tuple[bool, Dict]:
#     """
#     Test a single server endpoint
#
#     Args:
#         url: The URL to test
#         expected_code: Expected HTTP status code
#         expected_content: Expected content in response (optional)
#
#     Returns:
#         Tuple of (success: bool, result: dict)
#     """
#     try:
#         response = requests.get(url, timeout=5)
#         success = response.status_code == expected_code
#
#         if expected_content:
#             success = success and expected_content in response.text
#
#         result = {
#             'status_code': response.status_code,
#             'content': response.text[:100],  # First 100 chars
#             'expected_code': expected_code,
#             'url': url
#         }
#
#         return success, result
#
#     except requests.exceptions.RequestException as e:
#         logger.error(f"Error testing {url}: {str(e)}")
#         return False, {'error': str(e), 'url': url}
#
#
# def test_nginx_servers() -> bool:
#     """
#     Test both Nginx server configurations
#
#     Returns:
#         bool: True if all tests pass, False otherwise
#     """
#     # Wait for nginx to start
#     logger.info("Waiting for Nginx servers to start...")
#     time.sleep(5)
#
#     tests = [
#         {
#             'name': 'Site 1',
#             'url': 'http://nginx:8080',
#             'expected_code': 200,
#             'expected_content': 'Welcome to Site 1'
#         },
#         {
#             'name': 'Site 2',
#             'url': 'http://nginx:8081',
#             'expected_code': 503,
#             'expected_content': None
#         }
#     ]
#
#     all_passed = True
#
#     for test in tests:
#         logger.info(f"Testing {test['name']}...")
#         success, result = check_server_response(
#             test['url'],
#             test['expected_code'],
#             test['expected_content']
#         )
#
#         if success:
#             logger.info(f"{test['name']} test passed!")
#         else:
#             logger.error(f"{test['name']} test failed!")
#             logger.error(f"Expected status code: {test['expected_code']}")
#             logger.error(f"Actual result: {result}")
#             all_passed = False
#
#     return all_passed
#
#
# if __name__ == "__main__":
#     logger.info("Starting Nginx server tests...")
#     success = test_nginx_servers()
#
#     if success:
#         logger.info("All tests passed successfully!")
#         sys.exit(0)
#     else:
#         logger.error("Some tests failed!")
#         sys.exit(1)
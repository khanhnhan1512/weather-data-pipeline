#!/usr/bin/env python3
"""
Script test để kiểm tra việc import hàm từ api-request folder
"""
import sys
import os

# Thêm đường dẫn đến api-request folder
current_dir = os.path.dirname(os.path.abspath(__file__))
api_request_path = os.path.join(current_dir, 'api-request')
sys.path.append(api_request_path)

try:
    from insert_records import main
    print("✓ Import thành công!")
    print(f"Function main: {main}")
    
    # Test call function (comment out để tránh actual execution)
    # result = main()
    # print(f"Result: {result}")
    
except ImportError as e:
    print(f"✗ Import failed: {e}")
except Exception as e:
    print(f"✗ Error: {e}")
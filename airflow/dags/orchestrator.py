import sys
import os
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

# Thêm đường dẫn đến thư mục api-request
api_request_path = '/opt/airflow/api-request'
if api_request_path not in sys.path:
    sys.path.append(api_request_path)

def safe_main_callable():
    try:
        from insert_records import main
        return main()
    except ImportError as e:
        print(f"Import error: {e}")
        # Fallback cho môi trường local development
        local_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'api-request')
        if local_path not in sys.path:
            sys.path.append(local_path)
        from insert_records import main
        return main()

# Định nghĩa DAG

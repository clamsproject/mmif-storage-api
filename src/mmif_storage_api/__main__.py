"""
"""

import os
import sys
import json
from dotenv import load_dotenv

from mmif_storage import config, storage, analytics


load_dotenv()
config.MMIF_STORAGE_DIR = os.environ.get('MMIF_STORAGE_DIR')


def print_json(json_obj):
    print(json.dumps(json_obj, indent=2))


if len(sys.argv) > 1:

    if sys.argv[1] == 'peek':
        workflow = {"swt-detection/v8.6": {}}
        workflow_item = storage.WorkflowItem(
            app="swt-detection", version="v8.6", properties={})
        print_json(storage.peek([workflow_item]))

    elif sys.argv[1] == 'analytics':
        print_json(analytics.storage_analytics())

    elif sys.argv[1] == 'paths':
        stats = analytics.storage_analytics()
        print_json([wf["path"] for wf in stats["workflows"]])

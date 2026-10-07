# mmif-storage-api

Starting repository for api code separated out from mmif-storage.

To work with this first install the mmif storage archive in the packages directory and then do a local editable install of this repo:

```bash
pip install packages/mmif_storage_mv-0.2.0rc5.tar.gz
pip install -e .[dev]
```


<!--

Notes to self. 

The other README file in the top directory has the old full README from mmif-storage.

To make the tests run at some point some changes were made to `mmif_storage.create_storage_example()`. The distribution package is now updated, but for development consider doing a local editable install of the package: `pip install -e ../mmif_storage`.

-->
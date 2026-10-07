clean:
	rm -rf build
	rm -rf src/mmif_storage_api__mv.egg-info
	rm -rf storage-response*
	rm -rf tests/tmp-storage
	rm -rf tests/__pycache__
	rm -rf src/mmif_storage_api/__pycache__

build:
	python -m build

test:
	pytest --disable-warnings --tb=line

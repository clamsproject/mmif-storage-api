clean:
	rm -rf build
	rm -rf src/*.egg-info
	rm -rf storage-response*
	rm -rf tests/tmp-storage
	rm -rf tests/__pycache__
	rm -rf src/mmif_storage_api/__pycache__

build:
	make clean
	python -m build

test:
	pytest --disable-warnings --tb=line

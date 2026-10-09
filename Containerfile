FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir mmif-storage==0.2.0 python-dotenv==1.*
RUN pip install --no-cache-dir fastapi[standard]==0.141.* flask==3.1.* gunicorn==26.*

COPY pyproject.toml /app/pyproject.toml
COPY src /app/src

WORKDIR /app

RUN pip install .

# In the near future, after mmif-storage-api is available on PyPI, replace all
# pip installs above with:
#
# RUN pip install mmif-storage-api==0.1.0

CMD ["start_api", "--dir", "/data"]

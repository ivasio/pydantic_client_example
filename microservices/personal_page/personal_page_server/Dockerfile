FROM python:3.7 AS builder

WORKDIR /usr/src/app

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip

COPY common common
RUN pip install ./common
COPY microservices/petstore/client-python-httpx/petstore_httpx_client ./petstore_httpx_client
RUN pip install ./petstore_httpx_client

COPY microservices/personal_page/personal_page_server .
RUN pip install --no-cache-dir .


FROM python:3.7 AS service
WORKDIR /root/app/site-packages
COPY --from=builder /venv /venv
ENV PATH=/venv/bin:$PATH

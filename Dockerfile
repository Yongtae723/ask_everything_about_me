FROM python:3.9.3-slim
WORKDIR /workspace
RUN apt-get update -y --fix-missing && \
    apt-get -y install \
    make \
    git \
    curl \
    file \
    build-essential \
    libffi-dev


COPY poetry.lock pyproject.toml ./
RUN pip install poetry
COPY . .
RUN poetry config virtualenvs.create false \
    && poetry install --without dev

CMD streamlit run app.py\
    --browser.serverAddress="0.0.0.0" \
    --server.port="8080"

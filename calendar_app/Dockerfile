FROM python:3.10


COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8001
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
FROM python:3.8.6

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./app.py
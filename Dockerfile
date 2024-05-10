FROM python:3.12
WORKDIR /app
COPY /diplomProject/storeproject/ /app/sporthub
ENTRYPOINT ["python", "manage.py"]
RUN pip install -r requirements.txt
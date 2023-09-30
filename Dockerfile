FROM python:latest

COPY . /opt/app
WORKDIR /opt/app
RUN python -m pip install -r requirements.txt
# ENV DATABASE_URL="postgresql://postgres:19960801@postgres:5432/remarkables"

CMD ["python", "app.py"]
FROM python:3
COPY . .
CMD ["python", "./compute.py"]
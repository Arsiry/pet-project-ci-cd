FROM python:3.10

WORKDIR /app-sum-two-numbers
COPY ./main.py /app-sum-two-numbers/main.py
CMD ["/app-sum-two-numbers/main.py"]

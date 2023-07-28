FROM python:3.8
RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip install -r requirements.txt
ENV PARAMS ""

CMD ["bash", "-c", "python", "/app/main.py $PARAMS"]
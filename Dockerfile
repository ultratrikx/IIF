FROM python:3.12.4
WORKDIR "/home"
ADD app.zip .
RUN unzip app.zip
RUN pip install spacy flask nltk flask-sqlalchemy flask-login
RUN python -m spacy download en_core_web_sm
EXPOSE 42069
CMD ["python", "IIF/app.py"]

FROM continuumio/anaconda3
EXPOSE 5000
WORKDIR /app/
COPY ./FlaskDemo /app
RUN pip install -r requirements.txt 
CMD [ "python", "flask_predict_api.py" ] 
from flask import Flask, render_template, request
from flask import *
import pandas as pd
from model import all_data_representation, sqlQueries
from configuration_file import app, db, configure_app
from sqlalchemy import create_engine
from decouple import config


@app.route('/')
def hello_world():
    """
    rendering index3.html page for uploading csv file to process and save to DB
    :return: homepage
    """
    return render_template('index3.html')


@app.route('/products', methods=["POST"])
def upload_file():
    """
    rendering after all reading file data to show in datatable using jinja2
    :return: index3.html
    """
    raw_file = request.files['csv_uploader_file']
    raw_file.save('temporary_data/{}'.format(raw_file.filename))
    data = pd.read_csv('temporary_data//{}'.format(raw_file.filename))

    # Cleaning all duplicate data in 'sku' column
    filter_data = data.drop_duplicates(subset="sku", keep=False, inplace=True)
    clean_data = data

    return render_template('index3.html', data=clean_data)


if __name__ == '__main__':
    app.run(debug=True)

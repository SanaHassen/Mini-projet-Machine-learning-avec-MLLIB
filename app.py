import findspark
findspark.init()

import json

import pyspark
from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel


spark = SparkSession.builder.appName('prediction-api').getOrCreate()

#charger le modele a partir de dosser de serialisation (resultat de serialisation de phase de training )
model = PipelineModel.load("lrModelPipeline")

#developper l'api
# Create a Flask app
app = Flask(__name__)

# Define a route for the API
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.get_json()

    # Convert the input data into a Spark DataFrame
    input_df = spark.createDataFrame([input_data])

    # Evaluate and predict the output using the loaded Spark model
    output_df = model.transform(input_df).select('prediction')
    output = output_df.collect()[0]['prediction']

    # Return the result as a JSON object
    return jsonify({'prediction': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
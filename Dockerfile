FROM jupyter/pyspark-notebook

 # Set the working directory
WORKDIR /app
# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the training script and data files
COPY ./app.py  .
COPY . /app/ 
# Expose port for API
EXPOSE 8080

# Start Flask API
CMD ["python", "app.py"]
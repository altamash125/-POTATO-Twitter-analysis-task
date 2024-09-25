# FROM python:3.9
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# CMD ["streamlit", "run", "app.py"]
# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local files to the container
COPY . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the Streamlit default port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]

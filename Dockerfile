# 1. Base image with python installed
FROM python:3.10-slim

# 2. set working dir inside the container
WORKDIR /rate-limiter

# 3. Copy requirements first
COPY requirements.txt .

# 4. Install Python Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the entire project into container
COPY . .

# 6. Expose the port where Flask will run on
EXPOSE 5000

# 7. Command to run the Flask app
CMD [ "python", "app.py" ]

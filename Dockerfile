FROM python:3

# Server port and mongo port.
EXPOSE 3000
EXPOSE 27017

# Our project directory.
WORKDIR /usr/src/student_management

COPY requirements.txt ./

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run the server.
CMD [ "python", "./student_management.py" ]

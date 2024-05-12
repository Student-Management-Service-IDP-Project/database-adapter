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

ENV FLASK_APP="student_management.py"
# Run the server.
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=3000"]


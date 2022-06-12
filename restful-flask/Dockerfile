FROM python:3.10-alpine

# Install package
RUN apk update
RUN pip install --no-cache-dir virtualenv

# Define working directory
WORKDIR /usr/src/app
COPY requirement.txt bootstrap.sh ./
COPY cashman ./cashman

# Install API dependencies
RUN virtualenv venv
RUN venv/Scripts/activate
RUN pip install -r requirement.txt

# Start app
EXPOSE 5000
ENTRYPOINT [ "/usr/src/app/bootstrap.sh" ]
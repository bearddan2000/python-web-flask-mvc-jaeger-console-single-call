# python-web-flask-mvc-jaeger-console-single-call

## Description
Three spans are called in a single
call. Creates a simple web page with
a single button. When the button is
clicked spans are created and opentracing
output is sent to the console.

## Tech stack
- python
  - flask
  - opentracing-api
  - opentracing-sdk

## Docker stack
- python:latest

## To run
`sudo ./install.sh -u`
- Available http://localhost

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
[ Code concept ] (https://www.splunk.com/en_us/blog/devops/getting-started-with-opentelemetry-python-v1-0-0.html)

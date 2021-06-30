from flask import Flask, render_template, request
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)

tracer = trace.get_tracer(__name__)

def sendTrace():
    with tracer.start_as_current_span("foo"):
        with tracer.start_as_current_span("bar"):
            with tracer.start_as_current_span("baz"):
                print("Hello Splunk")
                return "Trace complete"

# Create Flask's `app` object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

@app.route('/', methods=['GET'])
def getIndex():
    trace = sendTrace()
    return render_template("index.html", msg=trace)

@app.route('/', methods=['POST'])
def postIndex():
    return sendTrace()

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)

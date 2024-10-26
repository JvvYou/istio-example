from opentelemetry import trace
from opentelemetry.propagate import set_global_textmap
from opentelemetry.propagators.b3 import B3MultiFormat
from opentelemetry.sdk.trace import TracerProvider

propagator = B3MultiFormat()
set_global_textmap(B3MultiFormat())
provider = TracerProvider()
# Sets the global default tracer provider
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)


def getForwardHeaders(request):
    headers = {}

    # x-b3-*** headers can be populated using the OpenTelemetry span
    ctx = propagator.extract(carrier={k.lower(): v for k, v in request.headers.items()})
    propagator.inject(headers, ctx)

    # We handle other (non x-b3-***) headers manually
    # if 'user' in session:
    #     headers['end-user'] = session['user']

    # Keep this in sync with the headers in details and reviews.
    incoming_headers = [
        # All applications should propagate x-request-id. This header is
        # included in access log statements and is used for consistent trace
        # sampling and log sampling decisions in Istio.
        'x-request-id',

        # Lightstep tracing header. Propagate this if you use lightstep tracing
        # in Istio (see
        # https://istio.io/latest/docs/tasks/observability/distributed-tracing/lightstep/)
        # Note: this should probably be changed to use B3 or W3C TRACE_CONTEXT.
        # Lightstep recommends using B3 or TRACE_CONTEXT and most application
        # libraries from lightstep do not support x-ot-span-context.
        'x-ot-span-context',

        # Datadog tracing header. Propagate these headers if you use Datadog
        # tracing.
        'x-datadog-trace-id',
        'x-datadog-parent-id',
        'x-datadog-sampling-priority',

        # W3C Trace Context. Compatible with OpenCensusAgent and Stackdriver Istio
        # configurations.
        'traceparent',
        'tracestate',

        # Cloud trace context. Compatible with OpenCensusAgent and Stackdriver Istio
        # configurations.
        'x-cloud-trace-context',

        # Grpc binary trace context. Compatible with OpenCensusAgent nad
        # Stackdriver Istio configurations.
        'grpc-trace-bin',

        # b3 trace headers. Compatible with Zipkin, OpenCensusAgent, and
        # Stackdriver Istio configurations.
        # This is handled by opentelemetry above
        # 'x-b3-traceid',
        # 'x-b3-spanid',
        # 'x-b3-parentspanid',
        # 'x-b3-sampled',
        # 'x-b3-flags',

        # SkyWalking trace headers.
        'sw8',

        # Application-specific headers to forward.
        'user-agent',

        # Context and session specific headers
        'cookie',
        'authorization',
        'jwt',
    ]
    # For Zipkin, always propagate b3 headers.
    # For Lightstep, always propagate the x-ot-span-context header.
    # For Datadog, propagate the corresponding datadog headers.
    # For OpenCensusAgent and Stackdriver configurations, you can choose any
    # set of compatible headers to propagate within your application. For
    # example, you can propagate b3 headers or W3C trace context headers with
    # the same result. This can also allow you to translate between context
    # propagation mechanisms between different applications.

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val

    return headers

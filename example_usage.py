from client import W3CTraceContext

def main():
    print("=== Testing W3C Trace Context Propagator ===")
    w3c = W3CTraceContext()
    tp = w3c.create_traceparent(trace_id="4bf92f3577b34da6a3ce929d0e0e4736", span_id="00f067aa0ba902b7", sampled=True)
    print("Generated traceparent:", tp)
    assert tp == "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01"

    parsed = w3c.parse_traceparent(tp)
    print("Parsed context:", parsed)
    assert parsed["trace_id"] == "4bf92f3577b34da6a3ce929d0e0e4736"
    assert parsed["sampled"] is True
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()

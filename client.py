import secrets

class W3CTraceContext:
    """
    W3C Trace Context Specification Propagator.
    Generates and parses traceparent headers.
    """
    def create_traceparent(self, trace_id=None, span_id=None, sampled=True):
        tid = trace_id or secrets.token_hex(16)
        sid = span_id or secrets.token_hex(8)
        flags = "01" if sampled else "00"
        return f"00-{tid}-{sid}-{flags}"

    def parse_traceparent(self, header):
        parts = header.split("-")
        if len(parts) != 4 or parts[0] != "00":
            return None
        return {
            "version": parts[0],
            "trace_id": parts[1],
            "parent_span_id": parts[2],
            "sampled": parts[3] == "01"
        }

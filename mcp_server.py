import sys
import json
from client import W3CTraceContext

def main():
    w3c = W3CTraceContext()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "create":
            tp = w3c.create_traceparent(params.get("trace_id"), params.get("span_id"), params.get("sampled", True))
            res = {"traceparent": tp}
        elif method == "parse":
            res = {"context": w3c.parse_traceparent(params.get("header", ""))}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()

# genpark-w3c-trace-context-span-propagator-skill

[![CI](https://github.com/alphaparkinc/genpark-w3c-trace-context-span-propagator-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/alphaparkinc/genpark-w3c-trace-context-span-propagator-skill/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> W3C Trace Context propagator implementing 128-bit TraceID, 64-bit SpanID, sampled flags, and cross-service distributed trace header parsing.

## Architecture

```mermaid
flowchart TD
    Client[AI Agent / Telemetry Source] -->|Trace Context / Span / Metric| Engine[genpark-w3c-trace-context-span-propagator-skill]
    Engine --> ObservabilityCore[Tracing Propagator & Histogram Aggregator]
    ObservabilityCore --> Collector[(OpenTelemetry Collector / Dashboard)]
```

## Features
- Pure standard library Python implementation with strictly zero pip dependencies.
- Production-grade telemetry principles (W3C traceparent, HdrHistogram, t-Digest, Dapper sampling).
- Native Model Context Protocol (MCP) server support for AI agent observability.

## Installation

```bash
git clone https://github.com/alphaparkinc/genpark-w3c-trace-context-span-propagator-skill.git
cd genpark-w3c-trace-context-span-propagator-skill
```

## Quickstart

```bash
python example_usage.py
```

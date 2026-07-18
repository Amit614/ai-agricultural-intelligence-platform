from benchmarks.model_latency import benchmark_latency
def test_latency():
    assert benchmark_latency()["avg_latency_ms"] > 0

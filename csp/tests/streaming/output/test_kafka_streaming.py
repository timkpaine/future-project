import csp.streaming as ts
import pytest
import time


class TestKafka:
    def setup(self):
        time.sleep(0.5)

    @pytest.mark.skipif("int(os.environ.get('csp_SKIP_DOCKER_TESTS', '1'))")
    def test_kafka(self):
        """Test streaming with Kafka"""

        def func():
            yield "a"
            yield "b"
            yield "c"

        out = ts.KafkaSink(ts.Func(func), servers="localhost:9092", topic="csp")
        assert ts.run(out) == ["a", "b", "c"]

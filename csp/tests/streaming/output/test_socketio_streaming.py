import csp.streaming as ts
import pytest
import time


class TestSocketIO:
    def setup(self):
        time.sleep(0.5)

    @pytest.mark.skipif("int(os.environ.get('csp_SKIP_DOCKER_TESTS', '1'))")
    def test_socketio(self):
        """Test socketio streaming"""

        def func():
            yield "a"
            yield "b"
            yield "c"

        out = ts.SocketIOSink(ts.Func(func), url="http://localhost:8069")
        assert ts.run(out) == ["a", "b", "c"]

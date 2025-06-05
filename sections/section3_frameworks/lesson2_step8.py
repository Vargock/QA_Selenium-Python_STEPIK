inputs = [(8, 11), (11, 11), (11, 15)]


def test_input_text(expected_result, actual_result):
    assert (
        expected_result == actual_result
    ), f"expected {expected_result}, got {actual_result}"


for a, b in inputs:
    test_input_text(a, b)

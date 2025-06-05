inputs = [(1, 1), ("some_text", "some")]


def test_substring(full_string, substring):
    assert str(substring) in str(
        full_string
    ), f"expected '{substring}' to be substring of '{full_string}'"


for a, b in inputs:
    test_substring(a, b)

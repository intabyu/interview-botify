from src.func import f


def test_f():
    # GIVEN
    cases = [
        ("abcde", True),
        ("}", False),
        ("{}", True),
        ("{[]}", True),
        ("{{)}", False),
        ("{a[b]c}d", True),
        ("a{b{c)d}e", False),
        ("", True),
    ]

    # WHEN
    for case in cases:
        input_, expected = case
        result = f(input_)
        # THEN
        assert result == expected

from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    result = split_integer(value, 3)

    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(32, 8)
    assert result == [4, 4, 4, 4, 4, 4, 4, 4]

    result = split_integer(32, 4)
    assert result == [8, 8, 8, 8]

    result = split_integer(6, 2)
    assert result == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)

    assert result == [8]
    assert len(result) == 1


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result)

    result = split_integer(17, 4)
    assert result == sorted(result)


def test_difference_between_max_and_min_should_be_no_more_than_one() -> None:
    result = split_integer(32, 6)
    assert max(result) - min(result) <= 1

    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 6)

    assert result == [0, 0, 0, 1, 1, 1]
    assert len(result) == 6
    assert sum(result) == 3
    assert max(result) - min(result) <= 1
    assert result == sorted(result)


def test_should_return_exact_number_of_parts() -> None:
    result = split_integer(15, 4)
    assert len(result) == 4

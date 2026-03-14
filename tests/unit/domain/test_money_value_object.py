from core.domain.value_objects.money import Money


def test_money_addition():
    m1 = Money(100, "USD")
    m2 = Money(50, "USD")

    result = m1 + m2

    assert result.amount == 150
    assert result.currency == "USD"


def test_money_currency_mismatch():
    m1 = Money(100, "USD")
    m2 = Money(50, "EUR")

    try:
        m1 + m2
        assert False
    except ValueError:
        assert True
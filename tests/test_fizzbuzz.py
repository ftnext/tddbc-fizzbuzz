from fizzbuzz import FizzBuzz


class TestFizzBuzz:
    def test_1を渡すと文字列1を返す(self):
        fizzbuzz = FizzBuzz()
        actual = fizzbuzz.convert(1)
        assert "1" == actual

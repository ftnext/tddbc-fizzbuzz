from fizzbuzz import FizzBuzz


class TestFizzBuzz:
    def test_1を渡すと文字列1を返す(self):
        fizzbuzz = FizzBuzz()
        assert "1" == fizzbuzz.convert(1)
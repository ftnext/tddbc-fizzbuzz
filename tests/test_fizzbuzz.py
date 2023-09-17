from fizzbuzz import FizzBuzz


class TestFizzBuzz:
    def test_1を渡すと文字列1を返す(self):
        fizzbuzz = FizzBuzz()
        assert "1" == fizzbuzz.convert(1)

    def test_2を渡すと文字列2を返す(self):
        fizzBuzz = FizzBuzz()
        assert "2" == fizzBuzz.convert(2)

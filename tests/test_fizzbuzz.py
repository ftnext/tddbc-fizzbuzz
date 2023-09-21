from fizzbuzz import FizzBuzz


class TestFizzBuzz:
    def setup_method(self):
        self.fizzBuzz = FizzBuzz()

    def test_1を渡すと文字列1を返す(self):
        assert "1" == self.fizzBuzz.convert(1)

    def test_2を渡すと文字列2を返す(self):
        assert "2" == self.fizzBuzz.convert(2)

    class Test_3の倍数のときは数の代わりにFizzに変換する:
        def test_3を渡すと文字列Fizzを返す(self):
            fizzBuzz = FizzBuzz()
            assert "Fizz" == fizzBuzz.convert(3)

    def test_5を渡すと文字列Buzzを返す(self):
        assert "Buzz" == self.fizzBuzz.convert(5)

from fizzbuzz import FizzBuzz


class Test_FizzBuzz数列と変換規則を扱うFizzBuzzクラス:
    class Test_convertメソッドは数を文字列に変換する:
        class Test_3の倍数のときは数の代わりにFizzに変換する:
            def test_3を渡すと文字列Fizzを返す(self):
                fizzBuzz = FizzBuzz()
                assert "Fizz" == fizzBuzz.convert(3)

        class Test_5の倍数のときは数の代わりにBuzzに変換する:
            def test_5を渡すと文字列Buzzを返す(self):
                fizzBuzz = FizzBuzz()
                assert "Buzz" == fizzBuzz.convert(5)

        class Test_その他の数のときはそのまま文字列に変換する:
            def setup_method(self):
                self.fizzBuzz = FizzBuzz()

            def test_1を渡すと文字列1を返す(self):
                assert "1" == self.fizzBuzz.convert(1)

            def test_2を渡すと文字列2を返す(self):
                assert "2" == self.fizzBuzz.convert(2)

from AQA_Alokhin.lesson_09.homework import sred_aref, perimetr, page_counter
import unittest

class Test_sred_aref(unittest.TestCase):
    def test_numbers(self):
        '''
        Positive case with integer
        :return:
        '''
        test_list = [0, 5, 7, 8]
        result = sred_aref(test_list)
        self.assertEquals(result,5)

    def test_float_numbers(self):
        '''
        positive case with float
        :return:
        '''
        test_list = [0.5, 1.3, 2.7, 3.3]
        result = sred_aref(test_list)
        self.assertEquals(result,1.95)

    def test_zero_devision(self):
        '''
        Negative case. Empty list
        :return:
        '''
        test_list = []
        with self.assertRaises(ZeroDivisionError):
            result = sred_aref(test_list)

    def test_type_error(self):
        '''
        Negative case with sting
        :return:
        '''
        test_list = [5, 'qwerty', 1, 'test']
        with self.assertRaises(TypeError):
            result = sred_aref(test_list)


class Test_perimetr(unittest.TestCase):
    def test_numbers(self):
        '''
        Positive case
        :return:
        '''
        self.assertEquals(perimetr(2,3), 10)

    def test_negative_numbers(self):
        self.assertEquals(perimetr(-4, -5), None)


    def test_type_error(self):
        '''
        Negative case with sting
        :return:
        '''
        with self.assertRaises(TypeError):
            result = perimetr('qwerty',4)

class Test_page_counter(unittest.TestCase):

    def test_golden_pass(self):
        result = page_counter(36, 4)
        self.assertEquals(result, 9)

    def test_golden_pass_plusOne(self):
        result = page_counter(60, 8)
        self.assertEquals(result, 8)

    def test_zero_photos(self):
        result = page_counter(0, 8)
        self.assertEquals(result, 0)

    def test_zero_photo_per_list(self):
        with self.assertRaises(ZeroDivisionError):
                result = page_counter(50, 0)


if __name__=='__main__':
    unittest.main()
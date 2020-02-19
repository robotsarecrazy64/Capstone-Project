import unittest
import data_processing

class MyTest(unittest.TestCase):
    # Tests the creation of the alarm hex master set
    def test_make_alarm_hex_master_set(self):
        result = data_processing.make_alarm_hex_master_set() # function call
        self.assertEqual(len(result), 74) # the resulting list should have a length of 74
        self.assertFalse(result == 1583) # the resulting length should not be equal to the input length (1583 tickets)

        test_list1 = ['0x10009', '0x10703', '0x10F69', '0x47E016B', '0x47E0228', '0x47E02FE', '0x47E0310', '0x47E0319', '0x47E0320', '0x47E0323', '0x47E0324', '0x47E0326', '0x47E0329', 
                      '0x47E0330', '0x47E0339', '0x47E0349', '0x47E035D', '0x47E035F', '0x47E0360', '0x47E0361', '0x47E042D', '0x47E048C', '0x47E0560', '0x47E05FD', '0x47E05FF', '0x47E060D',
                      '0x47E0616', '0x47E0690', '0x47E06C6', '0x47E06CB', '0x47E06D9', '0x47E06DB', '0x47E06DE', '0x47E06E0', '0x47E06E1', '0x47E06E2', '0x47E07B9', '0x47E07C6', '0x47E07CF', 
                      '0x47E07DC', '0x47E07DD', '0x47E07E1', '0x47E07E6', '0x47E07E9', '0x47E07EA', '0x47E07F2', '0x47E07F5', '0x47E07FA', '0x47E0812', '0x47E0822', '0x47E0854', '0x47E0857', 
                      '0x47E0859', '0x47E1006', '0x47E1007', '0x47E1008', '0x47E100C', '0x47E100D', '0x47E100E', '0x47E1013', '0x47E1014', '0x47E102D', '0x47E102E', '0x47E102F', '0x47E1030', 
                      '0x47E1045', '0x47E1046', '0x47E1047', '0x47E1049', '0x47E104E', '0x47E1052', '0x47E1058', '0x47E105A', '0x47E15FB' ] # master test array
        test_list1.sort() # sort the master test array
        self.assertEqual(result, test_list1) # the resulting list should contain 74 unique hex codes
        test_list2 = [] # empty array
        self.assertFalse(result == test_list2) # the resulting list should not be empty

if __name__ == '__main__':
    unittest.main()
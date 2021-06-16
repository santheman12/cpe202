# Name:         San Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VI
# Term:         Winter 2021

import unittest

import pset6
from pset6 import Entry  # only allowed use of from ... import


class TestHashKey(unittest.TestCase):

    def test_hash_key_1(self):
        self.assertEqual(pset6.hash_key(3, 3), 0)

    def test_hash_key_2(self):
        self.assertEqual(pset6.hash_key(6, 5), 1)

    def test_hash_key_3(self):
        self.assertEqual(pset6.hash_key(10, 7), 3)

    def test_hash_key_4(self):
        self.assertEqual(pset6.hash_key(0, 1), 0)

    def test_hash_key_5(self):
        with self.assertRaises(ZeroDivisionError):
            pset6.hash_key(1, 0)




class TestGetLoadFactor(unittest.TestCase):

    def test_get_load_factor_1(self):
        table = [None, Entry(1, "A", Entry(5, "B", None)), None, None]
        self.assertEqual(pset6.get_load_factor(table), 0.5)

    def test_get_load_factor_2(self):
        table = [Entry(0, "A", None), Entry(5, "B", None), None, None, None]
        self.assertEqual(pset6.get_load_factor(table), 0.4)

    def test_get_load_factor_3(self):
        table = [Entry(0, "C", None), Entry(5, "B", None), None, None, None]
        self.assertEqual(pset6.get_load_factor(table), 0.4)

    def test_get_load_factor_4(self):
        table = [Entry(0, "D", None), Entry(5, "B", None), None, None, None]
        self.assertEqual(pset6.get_load_factor(table), 0.4)

    def test_get_load_factor_5(self):
        table = [Entry(0, "E", None), Entry(5, "B", None), None, None, None]
        self.assertEqual(pset6.get_load_factor(table), 0.4)



class TestResize(unittest.TestCase):

    def test_resize_1(self):
        table = [Entry(0, "A", Entry(3, "B", Entry(6, "C", None))),
                 Entry(7, "D", Entry(1, "E", None)), None]
        resized = [Entry(7, "D", Entry(0, "A", None)), Entry(1, "E", None),
                   None, Entry(3, "B", None), None, None, Entry(6, "C", None)]
        self.assertEqual(pset6.resize(table, "chain"), resized)

    def test_resize_2(self):
        table = [Entry(0, "A", None), Entry(3, "B", None), Entry(8, "C", None)]
        resized = [Entry(0, "A", None), Entry(8, "C", None), None,
                   Entry(3, "B", None), None, None, None]
        self.assertEqual(pset6.resize(table, "probe"), resized)

    def test_resize_3(self):
        table = [Entry(0, "B", None), Entry(3, "C", None), Entry(8, "D", None)]
        resized = [Entry(0, "B", None), Entry(8, "D", None), None,
                   Entry(3, "C", None), None, None, None]
        self.assertEqual(pset6.resize(table, "probe"), resized)

    def test_resize_4(self):
        table = [Entry(0, "C", None), Entry(3, "D", None), Entry(8, "E", None)]
        resized = [Entry(0, "C", None), Entry(8, "E", None), None,
                   Entry(3, "D", None), None, None, None]
        self.assertEqual(pset6.resize(table, "probe"), resized)

    def test_resize_5(self):
        table = [Entry(0, "D", None), Entry(3, "E", None), Entry(8, "F", None)]
        resized = [Entry(0, "D", None), Entry(8, "F", None), None,
                   Entry(3, "E", None), None, None, None]
        self.assertEqual(pset6.resize(table, "probe"), resized)


class TestChainGet(unittest.TestCase):

    def test_chain_get_1(self):
        table = [Entry(3, "B", Entry(0, "A", None)), None, None]
        self.assertEqual(pset6.chain_get(table, 0), "A")

    def test_chain_get_2(self):
        table = [Entry(3, "B", Entry(0, "V", None)), None, None]
        self.assertEqual(pset6.chain_get(table, 0), "V")

    def test_chain_get_3(self):
        table = [Entry(3, "B", Entry(0, "N", None)), None, None]
        self.assertEqual(pset6.chain_get(table, 0), "N")

    def test_chain_get_4(self):
        table = [Entry(3, "B", Entry(0, "M", None)), None, None]
        self.assertEqual(pset6.chain_get(table, 0), "M")

    def test_chain_get_5(self):
        table = [Entry(3, "B", Entry(0, "O", None)), None, None]
        self.assertEqual(pset6.chain_get(table, 0), "O")




class TestChainInsert(unittest.TestCase):

    def test_chain_insert_1(self):
        table = [Entry(3, "C", Entry(0, "A", None)), 
                 Entry(4, "D", Entry(1, "B", None)), None]
        inserted = [Entry(0, "A", None), Entry(8, "E", Entry(1, "B", None)),
                    None, Entry(3, "C", None), Entry(4, "D", None), None, None]
        self.assertEqual(pset6.chain_insert(table, 8, "E"), inserted)

    def test_chain_insert_2(self):
        table = [Entry(3, "C", Entry(0, "A", None)),
                 Entry(4, "D", Entry(1, "B", None)), None]
        inserted = [Entry(0, "A", None), Entry(8, "F", Entry(1, "B", None)),
                    None, Entry(3, "C", None), Entry(4, "D", None), None, None]
        self.assertEqual(pset6.chain_insert(table, 8, "F"), inserted)

    def test_chain_insert_3(self):
        table = [Entry(3, "C", Entry(0, "A", None)),
                 Entry(4, "D", Entry(1, "B", None)), None]
        inserted = [Entry(0, "A", None), Entry(8, "G", Entry(1, "B", None)),
                    None, Entry(3, "C", None), Entry(4, "D", None), None, None]
        self.assertEqual(pset6.chain_insert(table, 8, "G"), inserted)

    def test_chain_insert_4(self):
        table = [Entry(3, "C", Entry(0, "A", None)),
                 Entry(4, "D", Entry(1, "B", None)), None]
        inserted = [Entry(0, "A", None), Entry(8, "H", Entry(1, "B", None)),
                    None, Entry(3, "C", None), Entry(4, "D", None), None, None]
        self.assertEqual(pset6.chain_insert(table, 8, "H"), inserted)

    def test_chain_insert_5(self):
        table = [Entry(3, "C", Entry(0, "A", None)),
                 Entry(4, "D", Entry(1, "B", None)), None]
        inserted = [Entry(0, "A", None), Entry(8, "I", Entry(1, "B", None)),
                    None, Entry(3, "C", None), Entry(4, "D", None), None, None]
        self.assertEqual(pset6.chain_insert(table, 8, "I"), inserted)


class TestChainRemove(unittest.TestCase):

    def test_chain_remove_1(self):
        table = [Entry(6, "C", Entry(3, "B", Entry(0, "A", None))), None, None]
        self.assertEqual(pset6.chain_remove(table, 3),
                         [Entry(6, "C", Entry(0, "A", None)), None, None])

    def test_chain_remove_2(self):
        table = [Entry(6, "C", Entry(3, "B", Entry(0, "D", None))), None, None]
        self.assertEqual(pset6.chain_remove(table, 3),
                         [Entry(6, "C", Entry(0, "D", None)), None, None])

    def test_chain_remove_3(self):
        table = [Entry(6, "C", Entry(3, "B", Entry(0, "E", None))), None, None]
        self.assertEqual(pset6.chain_remove(table, 3),
                         [Entry(6, "C", Entry(0, "E", None)), None, None])

    def test_chain_remove_4(self):
        table = [Entry(6, "C", Entry(3, "B", Entry(0, "P", None))), None, None]
        self.assertEqual(pset6.chain_remove(table, 3),
                         [Entry(6, "C", Entry(0, "P", None)), None, None])

    def test_chain_remove_5(self):
        table = [Entry(6, "C", Entry(3, "B", Entry(0, "X", None))), None, None]
        self.assertEqual(pset6.chain_remove(table, 3),
                         [Entry(6, "C", Entry(0, "X", None)), None, None])


class TestProbeGet(unittest.TestCase):

    def test_probe_get_1(self):
        table = [Entry(0, "A", None), Entry(3, "B", None), None]
        self.assertEqual(pset6.probe_get(table, 3), "B")

    def test_probe_get_2(self):
        table = [Entry(0, "A", None), Entry(3, "C", None), None]
        self.assertEqual(pset6.probe_get(table, 3), "C")

    def test_probe_get_3(self):
        table = [Entry(0, "A", None), Entry(3, "D", None), None]
        self.assertEqual(pset6.probe_get(table, 3), "D")

    def test_probe_get_4(self):
        table = [Entry(0, "A", None), Entry(3, "E", None), None]
        self.assertEqual(pset6.probe_get(table, 3), "E")

    def test_probe_get_5(self):
        table = [Entry(0, "A", None), Entry(3, "Q", None), None]
        self.assertEqual(pset6.probe_get(table, 3), "Q")


class TestProbeInsert(unittest.TestCase):

    def test_probe_insert_1(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), None]
        inserted = [Entry(0, "A", None), Entry(1, "B", None),
                    Entry(2, "C", None), None, None, None, None]
        self.assertEqual(pset6.probe_insert(table, 2, "C"), inserted)

    def test_probe_insert_2(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), None]
        inserted = [Entry(0, "A", None), Entry(1, "B", None),
                    Entry(2, "D", None), None, None, None, None]
        self.assertEqual(pset6.probe_insert(table, 2, "D"), inserted)

    def test_probe_insert_3(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), None]
        inserted = [Entry(0, "A", None), Entry(1, "B", None),
                    Entry(2, "E", None), None, None, None, None]
        self.assertEqual(pset6.probe_insert(table, 2, "E"), inserted)

    def test_probe_insert_4(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), None]
        inserted = [Entry(0, "A", None), Entry(1, "B", None),
                    Entry(2, "F", None), None, None, None, None]
        self.assertEqual(pset6.probe_insert(table, 2, "F"), inserted)

    def test_probe_insert_5(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), None]
        inserted = [Entry(0, "A", None), Entry(1, "B", None),
                    Entry(2, "G", None), None, None, None, None]
        self.assertEqual(pset6.probe_insert(table, 2, "G"), inserted)


class TestProbeRemove(unittest.TestCase):

    def test_probe_remove_1(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), None]
        self.assertEqual(pset6.probe_remove(table, 0),
                         [Entry(None, None, None), Entry(1, "B", None), None])

    def test_probe_remove_2(self):
        table = [Entry(0, "A", None), Entry(1, "E", None), None]
        self.assertEqual(pset6.probe_remove(table, 0),
                         [Entry(None, None, None), Entry(1, "E", None), None])

    def test_probe_remove_3(self):
        table = [Entry(0, "A", None), Entry(1, "X", None), None]
        self.assertEqual(pset6.probe_remove(table, 0),
                         [Entry(None, None, None), Entry(1, "X", None), None])

    def test_probe_remove_4(self):
        table = [Entry(0, "A", None), Entry(1, "P", None), None]
        self.assertEqual(pset6.probe_remove(table, 0),
                         [Entry(None, None, None), Entry(1, "P", None), None])

    def test_probe_remove_5(self):
        table = [Entry(0, "A", None), Entry(1, "W", None), None]
        self.assertEqual(pset6.probe_remove(table, 0),
                         [Entry(None, None, None), Entry(1, "W", None), None])


if __name__ == "__main__":
    unittest.main()

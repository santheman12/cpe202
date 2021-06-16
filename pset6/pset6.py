# Name:         San Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VI
# Term:         Winter 2021

from typing import List, Optional


class Entry:

    def __init__(self, key: Optional[int], val: Optional[str],
                 ref: Optional["Entry"]) -> None:
        self.key: Optional[int] = key
        self.val: Optional[str] = val
        self.ref = ref

    def __eq__(self, other: Optional["Entry"]) -> bool:
        if other is None:
            return False
        return (self.key == other.key and self.val == other.val
                and self.ref == other.ref)

    def __repr__(self) -> str:
        s = f"{self.key}:{self.val}"
        return s if self.ref is None else s + " " + str(self.ref)

    def __len__(self) -> int:
        """
        Return the number of entries chained together.

        >>> len(Entry(1, "A", Entry(2, "B", Entry(3, "C", None))))
        3
        """
        return 1 if self.ref is None else 1 + len(self.ref)

    def nullify(self) -> None:
        """
        Set the key and value of this object to None. A nullified object serves
        as a placeholder for a removed entry in a hash table.

        >>> e = Entry(1, "A", None)
        >>> e.nullify()
        >>> assert e.key == None
        >>> assert e.val == None
        """
        self.key = None
        self.val = None




def hash_key(key: int, size: int) -> int:
    """
    Return an integer for the given key to be used as an index to a table of
    the given size.

    >>> hash_key(10, 7)
    3
    """
    return key % size




def get_load_factor(table: List[Optional[Entry]]) -> float:
    """
    Return the load factor of the given table. Entries of None should count
    as empty slots when computing the load factor.

    >>> table = [None, Entry(1, "A", Entry(5, "B", None)), None, None]
    >>> get_load_factor(table)
    0.5

    >>> table = [Entry(0, "A", None), Entry(5, "B", None), None, None, None]
    >>> get_load_factor(table)
    0.4
    """

    count = 0
    load = 0
    if len(table) == 0:
        return 0
    while count < len(table):
        if table[count] is not None:
            load += 1
            if table[count].ref is not None:
                temp = table[count]
                while temp.ref is not None:
                    load += 1
                    temp = temp.ref
        count += 1
    return load / len(table)



def resize(table: List[Optional[Entry]], mode: str) -> List[Optional[Entry]]:
    """
    Resize and return the given table to twice its length plus one and rehash
    all integer keys from the original table into the resized table using the
    given collision resolution mode, which will be either "chain" or "probe".
    Rehash lower-indexed keys first; for separate chaining only, rehash keys at
    the head of the chain first.

    >>> table = [Entry(0, "A", Entry(3, "B", Entry(6, "C", None))), \
                 Entry(7, "D", Entry(1, "E", None)), None]
    >>> resize(table, "chain")
    [Entry(7, "D", Entry(0, "A", None)), Entry(1, "E", None), None, \
     Entry(3, "B", None), None, None, Entry(6, "C", None)]

    >>> table = [Entry(0, "A", None), Entry(3, "B", None), Entry(8, "C", None)]
    >>> resize(table, "probe")
    [Entry(0, "A", None), Entry(8, "C", None), None, Entry(3, "B", None), None,\
     None, None]
    """

    temp_table: List[Optional[Entry]] = []
    while (len(table) * 2 + 1) > len(temp_table):
        temp_table.append(None)

    if mode == 'chain':
        for i in table:
            if i is not None:
                while i is not None:
                    hashkey = hash_key(i.key, len(temp_table))
                    if temp_table[hashkey] is not None:
                        temp = temp_table[hashkey]
                        temp_table[hashkey] = Entry(i.key, i.val, temp)
                    else:
                        temp_table[hashkey] = Entry(i.key, i.val, None)
                    i = i.ref

    if mode == 'probe':
        for i in table:
            if i is not None:
                hashkey = hash_key(i.key, len(temp_table))
                if temp_table[hashkey] is None:
                    temp_table[hashkey] = i
                else:
                    while temp_table[hashkey] is not None:
                        if hashkey + 1 > len(temp_table)-1:
                            hashkey = 0
                        else:
                            hashkey += 1
                    temp_table[hashkey] = i

    return temp_table

def chain_get(table: List[Optional[Entry]], key: int) -> str:
    """
    Return the value corresponding to the given key in the table, following
    separate chaining collision resolution. If the key does not exist in the
    table, raise a KeyError.

    >>> table = [Entry(3, "B", Entry(0, "A", None)), None, None]
    >>> chain_get(table, 0)
    "A"
    """

    index = hash_key(key, len(table))

    while table[index] is not None:
        if table[index].key == key:
            return table[index].val
        table[index] = table[index].ref

    raise KeyError





def chain_insert(table: List[Optional[Entry]], key: int,
                 val: str) -> List[Optional[Entry]]:
    """
    Add the given key-value pair (as a Entry object) to the table and return
    this updated table, following separate chaining collision resolution.

    If performing this update results in the load factor reaching 1.5, resize
    the table to be one more than twice the original length and rehash the
    entire table before returning it.

    >>> table = [Entry(3, "C", Entry(0, "A", None)), \
                 Entry(4, "D", Entry(1, "B", None)), None]
    >>> chain_insert(table, 8, "E")
    [Entry(0, "A", None), Entry(8, "E", Entry(1, "B", None)), None, \
     Entry(3, "C", None), Entry(4, "D", None), None, None]
    """

    hashkey = hash_key(key, len(table))

    if table[hashkey] is None:
        table[hashkey] = Entry(key, val, None)
    else:
        table[hashkey] = Entry(key, val, table[hashkey])

    if get_load_factor(table) >= 1.5:
        table = resize(table, 'chain')

    return table




def chain_remove(table: List[Optional[Entry]],
                 key: int) -> List[Optional[Entry]]:
    """
    Remove the Entry object containing the given key and return this updated
    table. If such an entry does not exist, raise a KeyError.

    >>> table = [Entry(6, "C", Entry(3, "B", Entry(0, "A", None))), None, None]
    >>> chain_remove(table, 3)
    [Entry(6, "C", Entry(0, "A", None)), None, None]
    """

    index = hash_key(key, len(table))
    temp = table[index]
    while temp is not None:
        if temp.key == key:
            table[index] = temp.ref
            return table
        if temp.ref is not None:
            node = table[hash_key(key, len(table))]
            while node.ref.key != key:
                node = node.ref
                if node.ref is None:
                    raise KeyError
            node.ref = node.ref.ref
            return table
    raise KeyError



def probe_get(table: List[Optional[Entry]], key: int) -> str:
    """
    Return the value corresponding to the given key in the table, following
    linear probing collision resolution and terminating early if an empty slot
    (but not a nullified entry) is encountered. If the key does not exist in
    the table, raise a KeyError.

    >>> table = [Entry(0, "A", None), Entry(3, "B", None), None]
    >>> probe_get(table, 3)
    "B"
    """

    index = hash_key(key, len(table))

    while table[index] is not None:
        if table[index].key == key:
            return table[index].val
        index += 1

    raise KeyError






def probe_insert(table: List[Optional[Entry]], key: int,
                 val: str) -> List[Optional[Entry]]:
    """
    Add the given key-value pair (as a Entry object) to the table and return
    this updated table, following linear probing collision resolution by
    replacing either an empty slot or a nullified entry with the new entry.

    If performing this update results in the load factor reaching 0.75, resize
    the table to be one more than twice the original length and rehash the
    entire table before returning it.

    >>> table = [Entry(0, "A", None), Entry(1, "B", None), None]
    >>> probe_insert(table, 2, "C")
    [Entry(0, "A", None), Entry(1, "B", None), Entry(2, "C", None), None, \
     None, None, None]
    """

    hashkey = hash_key(key, len(table))

    if get_load_factor(table) == 1:
        table = resize(table, 'probe')

    while table[hashkey] is not None:
        hashkey += 1

    table[hashkey] = Entry(key, val, None)

    if get_load_factor(table) >= 0.75:
        table = resize(table, 'probe')

    return table



def probe_remove(table: List[Optional[Entry]],
                 key: int) -> List[Optional[Entry]]:
    """
    Call the nullify method on the Entry object containing the given key and
    return this updated table. If such an entry does not exist, raise a
    KeyError.

    >>> table = [Entry(0, "A", None), Entry(1, "B", None), None]
    >>> probe_remove(table, 0)
    [Entry(None, None, None), Entry(1, "B", None), None]
    """

    index = hash_key(key, len(table))

    while table[index] is not None:
        if table[index].key == key:
            table[index].nullify()
            return table
        index += 1

    raise KeyError


import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        person = BookLover('Alice', 'alice@email.com', 'fantasy')
        person.add_book('The Hobbit', 5)
        self.assertTrue(person.has_read('The Hobbit'))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        person = BookLover('Bob', 'bob@email.com', 'sci-fi')
        person.add_book('Dune', 4)
        person.add_book('Dune', 4)
        self.assertEqual(person.num_books_read(), 1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        person = BookLover('Charlie', 'charlie@email.com', 'mystery')
        person.add_book('Harry Potter', 4)
        self.assertTrue(person.has_read('Harry Potter'))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        person = BookLover('Dave', 'dave@email.com', 'horror')
        self.assertFalse(person.has_read('Dracula'))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        person = BookLover('Eve', 'eve@email.com', 'romance')
        person.add_book('Pride and Prejudice', 5)
        person.add_book('Emma', 4)
        self.assertEqual(person.num_books_read(), 2)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating > 3
        person = BookLover('Frank', 'frank@email.com', 'adventure')
        person.add_book('The Three Musketeers', 4)
        person.add_book('Treasure Island', 3)
        fav_books = person.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)

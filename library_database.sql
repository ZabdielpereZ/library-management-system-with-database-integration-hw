-- Library Database

-- Creating database 
CREATE DATABASE library;

-- using this scipt 
USE library; 

-- books table
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- authors table
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

-- customers table 
CREATE TABLE customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    email CHAR(25),
    phone CHAR(16),
    library_id VARCHAR(10) NOT NULL UNIQUE
    );

-- borrowed books table 
CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

-- Creating an index for (library_id)
ALTER TABLE customer MODIFY library_id VARCHAR(10);
CREATE INDEX idx_library_id ON customer(library_id);

-- Adding customers to our database
INSERT INTO customer (customer_name, email, phone, library_id)
VALUES ('Mozinni', 'poptart@mail.milk', '1594563586', 'KJHW4EF2LK'),
('Zab', 'look@menow.mail', '6524857545', 'PLKUH5TD7B'), ('Ruppee', 'meow@meow.meow', '3621520145', 'POP00PI320'), 
('Lisa J Simpson', 'rules@rule.wow', '5036295864' , 'LOGHJ5VSD1'),
('Bart J Simpson', 'yousmell@aye.cramba', '5035625414', 'FDSZXC2QA5');

-- Verifying the Author Exists / Adding authors
SELECT * FROM authors WHERE id = 1;

INSERT INTO authors (id, name, biography) VALUES ('1', 'George Orwell', 'George Orwell (1903–1950) was an English novelist, essayist, and critic12. His real name was Eric Arthur Blair. He is best known for his novels Animal Farm (1945) and Nineteen Eighty-Four (1949)'), 
('2', 'JK Rowling', 'J.K. Rowling, born on July 31, 1965, is a British author. She is best known for creating the popular Harry Potter series, which was adapted into blockbuster films'), 
('3', 'Simon Hanselmann', 'Simon Hanselmann is an Australian-born cartoonist best known for his Megg, Mogg, and Owl series. Hanselmann has been nominated four times for an Ignatz Award, four times for an Eisner Award (winning twice), twice for the Harvey Award and won Best Series at Angouleme 2018.'),
('4', 'J.R.R. Tolkien', 'J.R.R. Tolkien was an English writer and scholar. He achieved fame with his book The Hobbit and his epic fantasy The Lord of the Rings.'),
('5', 'Jeff Kenney', 'Jeff Kinney (born February 19, 1971, Fort Washington, Maryland, U.S.) is an American children’s author and website developer best known for writing the Diary of a Wimpy Kid series of books. The books became extremely popular with middle-school students, especially boys, who were easily able to identify with characters in the books.');


-- DROPING TABLE 
DROP TABLE customer; 
DROP TABLE borrowed_books;
DROP TABLE authors;
DROP TABLE books;

-- View contents
DESCRIBE books;
SELECT * FROM books;
SELECT * FROM authors;
SELECT * FROM customer;
SELECT * FROM borrowed_books;
CREATE TABLE ballygunnerleaders
(
    id INT NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address VARCHAR(60) NOT NULL,
    contact CHAR(10) NOT NULL,
    email VARCHAR(40) NOT NULL,
    garda_vetted DATE NOT NULL,
    training_level VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO ballygunnerleaders (firstname, surname, gender, address, contact, email, garda_vetted, training_level)
VALUES
    ('Louis', 'Sullivan', 'male', 'Bothar Bui, Ballygunner, Waterford', '0848371234', 'louissullivan@gmail.com', '2019-01-19', 'Gilwell Woggle'),
    ('Mark', 'Schnieders', 'male', 'Fairview, Ballygunner, Waterford', '0812371234', 'marks@gmail.com', '2019-01-21', 'Gilwell Woggle'),
    ('Mark', 'Hayes', 'male', 'Riverhill, Ballygunner, Waterford', '089886544', 'hayesmark@gmail.com', '2018-09-08', 'Wood Badge Beads'),
    ('Conor', 'Phelan', 'male', ' 12 Dunmore Road, Ballygunner, Waterford', '0862341111', 'cphelan12@gmail.com', '2019-01-18', 'Gilwell Woggle'),
    ('Katie', 'Paul', 'female', '22 Finns Park, Ballygunner, Waterford', '0877888224', 'kpaul12@gmail.com', '2018-09-08', 'Wood Badge Pin')
;

DROP TABLE IF EXISTS ballygunnerskills

CREATE TABLE ballygunnerskills
(
    id INT NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    birth DATE NOT NULL,
    camping CHAR(1) NOT NULL,
    backwoods CHAR(1) NOT NULL,
    hillwalking CHAR(1) NOT NULL,
    pioneering CHAR(1) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO ballygunnerscouts (firstname, surname, birth, camping, backwoods, hillwalking, pioneering)
VALUES
('Jim', 'Fox', '2015-02-02', '1', '2', '2', '1'),
('Todd', 'McDonald', '2014-04-11', '3', '2', '1', '3'),
('Conor', 'McCarthy', '2012-05-16', '2', '3', '3', '1'),
('Ella', 'O''Brien', '2012-04-20', '3', '3', '3', '3'),
('Clara', 'Keeney', '2013-08-28', '3', '2', '2', '1'),
('Roisin', 'Prizeman', '2012-01-12', '4', '3', '2', '4'),
('Sean', 'Cronin', '2010-03-24','3', '4', '4', '3'),
('Ben', 'Luby', '2008-04-22', '4', '3', '2', '2'),
('Cian', 'Kiely', '2009-11-15', '5', '5', '2', '4'),
('Dan', 'Buckley', '2010-08-01', '3', '4', '4', '4'),
('Aoife', 'Cahill', '2007-02-19', '5', '5', '6', '5'),
('Ruth', 'Power', '2005-04-18', '6', '5', '7', '4'),
('Sophie', 'Bradley', '2006-12-22', '7', '5', '5', '5'),
('Alex', 'Delaney', '2007-04-29', '4', '6', '6', '7'),
('Shane', 'Crowdle', '2005-05-19', '5', '4', '4', '6'),
('Heather', 'O''Keefe', '2004-12-23', '5', '6', '6', '5'),
('John', 'Curtain', '2002-04-26', '8', '7', '7', '7'),
('Eoin', 'Kelly', '2003-12-12', '6', '7', '7', '5'),
('Lorna', 'O''Dwyer', '2002-08-07', '7', '6', '6', '6'),
('Mark', 'Morrison', '2004-11-16', '7', '7', '7', '8')

;

DROP TABLE IF EXISTS ballygunnerscouts

CREATE TABLE ballygunnerscouts
(
    id INT NOT NULL AUTO_INCREMENT,
    scout_section VARCHAR(10),
    firstname VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    birth DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address VARCHAR(60) NOT NULL,
    guardian_fname VARCHAR(20) NOT NULL,
    guardian_sname VARCHAR(20) NOT NULL,
    guardian_number CHAR(10) NOT NULL,
    guardian_email VARCHAR(40) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO ballygunnerscouts (scout_section, firstname, surname, birth, gender, address, guardian_fname, guardian_sname, guardian_number, guardian_email)
VALUES
    ('Beavers', 'Jim', 'Fox', '2015-02-02', 'male', '2nd Floor, 7 Adelphi Quay, Ballygunner, Waterford', 'Mary', 'Fox', '0848379866', 'foxmary@gmail.com'),
    ('Beavers', 'Todd', 'McDonald', '2014-04-11', 'male', 'Rantavan Hse, Ballygunner, Waterford', 'Orla', 'McDonald', '086892211', 'orlamcdonald@gmail.com'),
    ('Beavers', 'Conor', 'McCarthy', '2012-05-16', 'male', 'Colman West, Ballygunner, Waterford', 'Jerry', 'McCarthy', '0860022917', 'mccarthyjerry@gmail.com'),
    ('Beavers', 'Ella', 'O''Brien', '2012-04-20', 'female', '103 Castleforbes, Ballygunner, Waterford', 'Claire', 'O''Brien', '0843358524', 'claireob@gmail.com'),
    ('Beavers', 'Clara', 'Keeney', '2013-08-28', 'female', 'The Parade, Ballygunner, Waterford', 'George', 'Keeney', '0843739773', 'georgekeeney@gmail.com'),
    ('Cubs', 'Roisin', 'Prizeman', '2012-01-12', 'female', '7 Sharman Drive, Ballygunner, Waterford', 'Kevin', 'Prizeman', '0859945344', 'kevprizeman@gmail.com'),
    ('Cubs', 'Sean', 'Cronin', '2010-03-24', 'male', '13 Clifton Grange, Tramore, Waterford', 'Daisy', 'Cronin', '0830792184', 'cronindaisy@gmail.com'),
    ('Cubs', 'Ben', 'Luby', '2008-04-22', 'male', 'Portnahully, Coppercoast, Waterford', 'Catherine', 'Luby', '0837280313', 'catluby@gmail.com'),
    ('Cubs', 'Cian', 'Kiely', '2009-11-15', 'male', '86 Erne Dale Heights, Barrack St, Waterford', 'Jason', 'Kiely', '0860705043', 'jkiely@gmail.com'),
    ('Cubs', 'Dan', 'Buckley', '2010-08-01', 'male', '1 Charlemount Heights, Ballygunner, Waterford', 'Beth', 'Buckley', '0875927327', 'bethbuckley@gmail.com'),
    ('Scouts', 'Aoife', 'Cahill', '2007-02-19', 'female', 'Castledonovan, Drimoleague, Waterford', 'Ludwig', 'Cahill', '0858381714', 'ludcahill@gmail.com'),
    ('Scouts', 'Ruth', 'Power', '2005-04-18', 'female', '16 Rathfriland St, Waterford', 'Kate', 'Power', '0863417995', 'powerkate@gmail.com'),
    ('Scouts', 'Sophie', 'Bradley', '2006-12-22', 'female', '136 Morehampton rd, Waterford', 'Lisa', 'Bradley', '0858220656', 'lisab@gmail.com'),
    ('Scouts', 'Alex', 'Delaney', '2007-04-29', 'male', 'Canal Banks, Ballygunner, Waterford', 'Eimear', 'Delaney', '0851483953', 'eimeardelaney@gmail.com'),
    ('Scouts', 'Shane', 'Crowdle', '2005-05-19', 'male', 'Lanesboro st, Fairview, Waterford', 'Michael', 'Crowdle', '0859406307', 'michaelcrowdle@gmail.com'),
    ('Ventures', 'Heather', 'O''Keefe', '2004-12-23', 'female', '69 Kingsgrove, Tramore, Waterford', 'Carol', 'O''Keefe', '0870753974', 'carolok@gmail.com'),
    ('Ventures', 'John', 'Curtain', '2002-04-26', 'male',  '3 Hillview, Ballygunner, Waterford', 'Kieran', 'Curtain', '0833596145', 'curtainkieran@gmail.com'),
    ('Ventures', 'Eoin', 'Kelly', '2003-12-12', 'male', 'Main Street, Urlingford, Waterford', 'Niall', 'Kelly', '0854635063', 'niallkelly@gmail.com'),
    ('Ventures', 'Lorna', 'O''Dwyer', '2002-08-07', 'female', '21B Western Rd, Waterford City', 'Aisling', 'O''Dwyer', '0833747996', 'aislingodwyer@gmail.com'),
    ('Ventures', 'Mark', 'Morrison', '2004-11-16', 'male', 'Loughbown, Ballygunner, Waterford', 'Noah', 'Morrison', '0863033697', 'morrisonniall@gmail.com')

;

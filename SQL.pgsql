DELETE FROM advisors
WHERE name = 'Doctor Strange'
-- WHERE id BETWEEN 4 AND 6 ; 

DELETE FROM users WHERE id BETWEEN 23 AND 24 ; 


SELECT * from admin;
SELECT * from advisors;
SELECT * from bookings;
SELECT * from users;

INSERT INTO admin(name, image_url)
VALUES
('Nick Fury','https://i.ibb.co/gwfjT9z/Nick-Fury.jpg');

DELETE FROM admin;

DELETE FROM users WHERE id = 1 or id > 2 ;

DROP TABLE alembic_version ;

UPDATE advisors
SET status = Not status
where id = 1;
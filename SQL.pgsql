DELETE FROM advisors
WHERE name = 'Doctor Strange'
-- WHERE id BETWEEN 4 AND 6 ; 

DELETE FROM users
WHERE id BETWEEN 23 AND 24 ; 

select * from advisors;
select * from admin;
select * from users;

INSERT INTO admin(name, image_url)
VALUES
('Nick Fury','https://i.ibb.co/gwfjT9z/Nick-Fury.jpg');

DELETE FROM admin;

DELETE FROM users
where id = 1 or id >2;

drop table alembic_version;
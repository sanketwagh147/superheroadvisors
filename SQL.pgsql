DELETE FROM advisors
WHERE id BETWEEN 21 AND 23 ; 



select * from advisors;
select * from admin;
select * from users;

INSERT INTO admin(name, image_url)
VALUES
('Nick Fury','https://i.ibb.co/gwfjT9z/Nick-Fury.jpg');

DELETE FROM admin;

DELETE FROM users;

drop table alembic_version;
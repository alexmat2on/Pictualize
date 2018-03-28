DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `createUser`(
  IN firstname VARCHAR(20),
  IN lastname VARCHAR(20),
  IN e_mail VARCHAR(20),
  IN user_id varchar(25)
)
BEGIN
if ( select exists (select 1 from Users where userID = user_id) ) THEN

select 'Username Exists !!';

ELSE

insert into Users
  (
    first_name,
    last_name,
    email,
    userID
  )
  values
  (
    firstname,
    lastname,
    e_mail,
    user_id
  );

  END IF;
  END$$
  DELIMITER ;

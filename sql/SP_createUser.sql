DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `createUser` (
  IN firstname VARCHAR(20),
  IN lastname VARCHAR(20),
  IN e_mail VARCHAR(20),
  IN user_id varchar(25)
)

BEGIN
IF ( SELECT EXISTS (SELECT 1 from Users where userID = user_id) ) THEN

SELECT 'Username Exists';

ELSE

INSERT INTO Users
  (
    first_name,
    last_name,
    email,
    userID
  )

  VALUES
  (
    firstname,
    lastname,
    e_mail,
    user_id
  );

END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `setAvatar` (
  IN arg_imageID VARCHAR(40),
  IN arg_userID VARCHAR(25)
)

BEGIN
INSERT INTO Profiles
  (
    userID,
    avatarID
  )

  VALUES
  (
    arg_userID,
    arg_imageID
  );

END$$
DELIMITER ;

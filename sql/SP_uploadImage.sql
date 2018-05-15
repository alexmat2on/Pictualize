DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `uploadImage` (
  IN arg_imageID VARCHAR(40),
  IN arg_img_type VARCHAR(5),
  IN arg_userID VARCHAR(25)
)

BEGIN
INSERT INTO Images
  (
    imageID,
    img_type
  )

  VALUES
  (
    arg_imageID,
    arg_img_type
  );

INSERT INTO SavedImages
  (userID, saved_imageID)
VALUES
  (arg_userID, arg_imageID);

END$$
DELIMITER ;

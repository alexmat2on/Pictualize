DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `makePost` (
  IN arg_userID VARCHAR(25),
  IN arg_postImage VARCHAR(40),
  IN arg_tempImage VARCHAR(40),
  IN arg_textTop VARCHAR (20),
  IN arg_textBot VARCHAR (20)
)

BEGIN
INSERT INTO Posts
  (
    userID,
    post_image,
    template_image,
    post_ts,
    text_top,
    text_bot
  )

  VALUES
  (
    arg_userID,
    arg_postImage,
    arg_tempImage,
    NOW(),
    arg_textTop,
    arg_textBot
  );

END$$
DELIMITER ;

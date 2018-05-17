DELIMITER $$
CREATE DEFINER=`root`@`localhost`
TRIGGER `addDefaultTemplates`
AFTER INSERT ON Users
FOR EACH ROW
BEGIN
DECLARE n INT DEFAULT 0;
DECLARE i INT DEFAULT 0;
SELECT COUNT(*) FROM DefaultTemplates INTO n;
SET i=0;

WHILE i<n DO
  SET @img := (SELECT imageID FROM DefaultTemplates LIMIT i,1);
  
  INSERT INTO SavedImages (userID, saved_imageID)
  VALUES (
    NEW.userID,
    @img
  );
  SET i = i + 1;
END WHILE;
END$$
DELIMITER ;

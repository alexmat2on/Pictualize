-- MySQL dump 10.16  Distrib 10.1.31-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: Pictualize
-- ------------------------------------------------------
-- Server version	10.1.31-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Follows`
--

DROP TABLE IF EXISTS `Follows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Follows` (
  `userID` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `followed_userID` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Follows`
--

LOCK TABLES `Follows` WRITE;
/*!40000 ALTER TABLE `Follows` DISABLE KEYS */;
/*!40000 ALTER TABLE `Follows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ImageTags`
--

DROP TABLE IF EXISTS `ImageTags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ImageTags` (
  `imageID` int(11) DEFAULT NULL,
  `tag` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ImageTags`
--

LOCK TABLES `ImageTags` WRITE;
/*!40000 ALTER TABLE `ImageTags` DISABLE KEYS */;
/*!40000 ALTER TABLE `ImageTags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Images`
--

DROP TABLE IF EXISTS `Images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Images` (
  `imageID` int(11) NOT NULL,
  `img_size` int(11) DEFAULT NULL,
  `img_type` varchar(5) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `text_top` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `text_bot` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`imageID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Images`
--

LOCK TABLES `Images` WRITE;
/*!40000 ALTER TABLE `Images` DISABLE KEYS */;
/*!40000 ALTER TABLE `Images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Posts`
--

DROP TABLE IF EXISTS `Posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Posts` (
  `postID` int(11) NOT NULL,
  `userID` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `post_imageID` int(11) DEFAULT NULL,
  `post_ts` datetime DEFAULT NULL,
  PRIMARY KEY (`postID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Posts`
--

LOCK TABLES `Posts` WRITE;
/*!40000 ALTER TABLE `Posts` DISABLE KEYS */;
/*!40000 ALTER TABLE `Posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Profiles`
--

DROP TABLE IF EXISTS `Profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Profiles` (
  `userID` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `avatarID` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Profiles`
--

LOCK TABLES `Profiles` WRITE;
/*!40000 ALTER TABLE `Profiles` DISABLE KEYS */;
INSERT INTO `Profiles` VALUES ('Raven_Bergnaum39','https://s3.amazonaws.com/uifaces/faces/twitter/_williamguerra/128.jpg'),('Maybell12','https://s3.amazonaws.com/uifaces/faces/twitter/wearesavas/128.jpg'),('Aidan.Marks','https://s3.amazonaws.com/uifaces/faces/twitter/allthingssmitty/128.jpg'),('Marguerite99','https://s3.amazonaws.com/uifaces/faces/twitter/jagan123/128.jpg'),('Donavon72','https://s3.amazonaws.com/uifaces/faces/twitter/rawdiggie/128.jpg'),('Bryce_Cole16','https://s3.amazonaws.com/uifaces/faces/twitter/sydlawrence/128.jpg'),('Selina68','https://s3.amazonaws.com/uifaces/faces/twitter/souperphly/128.jpg'),('Ricardo_Will','https://s3.amazonaws.com/uifaces/faces/twitter/evandrix/128.jpg'),('Britney_Dickinson6','https://s3.amazonaws.com/uifaces/faces/twitter/maz/128.jpg'),('Vena17','https://s3.amazonaws.com/uifaces/faces/twitter/agromov/128.jpg'),('Roscoe76','https://s3.amazonaws.com/uifaces/faces/twitter/RussellBishop/128.jpg'),('Melvina.Konopelski85','https://s3.amazonaws.com/uifaces/faces/twitter/flexrs/128.jpg'),('Evie_Doyle66','https://s3.amazonaws.com/uifaces/faces/twitter/andyisonline/128.jpg'),('Dolores.Corwin21','https://s3.amazonaws.com/uifaces/faces/twitter/spedwig/128.jpg'),('Maximillian57','https://s3.amazonaws.com/uifaces/faces/twitter/mattlat/128.jpg'),('Shanny.Pacocha','https://s3.amazonaws.com/uifaces/faces/twitter/martinansty/128.jpg'),('Camren16','https://s3.amazonaws.com/uifaces/faces/twitter/peachananr/128.jpg'),('Clementina.Ledner','https://s3.amazonaws.com/uifaces/faces/twitter/_vojto/128.jpg'),('Sonny.Kirlin','https://s3.amazonaws.com/uifaces/faces/twitter/martip07/128.jpg'),('Mohamed42','https://s3.amazonaws.com/uifaces/faces/twitter/nomidesigns/128.jpg'),('Zack19','https://s3.amazonaws.com/uifaces/faces/twitter/tumski/128.jpg'),('Julianne_Oberbrunner','https://s3.amazonaws.com/uifaces/faces/twitter/weglov/128.jpg'),('Clair69','https://s3.amazonaws.com/uifaces/faces/twitter/syropian/128.jpg'),('Amely_Corwin','https://s3.amazonaws.com/uifaces/faces/twitter/johnriordan/128.jpg'),('Ronaldo81','https://s3.amazonaws.com/uifaces/faces/twitter/jitachi/128.jpg'),('Garry_Schneider','https://s3.amazonaws.com/uifaces/faces/twitter/vj_demien/128.jpg'),('Angeline1','https://s3.amazonaws.com/uifaces/faces/twitter/nyancecom/128.jpg'),('Claude.Shanahan2','https://s3.amazonaws.com/uifaces/faces/twitter/incubo82/128.jpg'),('Beulah_Reinger15','https://s3.amazonaws.com/uifaces/faces/twitter/iamglimy/128.jpg'),('Christa.Schulist','https://s3.amazonaws.com/uifaces/faces/twitter/ernestsemerda/128.jpg'),('Enos_Gislason70','https://s3.amazonaws.com/uifaces/faces/twitter/tweetubhai/128.jpg'),('Ben70','https://s3.amazonaws.com/uifaces/faces/twitter/spedwig/128.jpg'),('Dillan_Hauck56','https://s3.amazonaws.com/uifaces/faces/twitter/_pedropinho/128.jpg'),('Dejah26','https://s3.amazonaws.com/uifaces/faces/twitter/tweetubhai/128.jpg'),('Jonas_Mante97','https://s3.amazonaws.com/uifaces/faces/twitter/mr_shiznit/128.jpg'),('Mabelle.Davis96','https://s3.amazonaws.com/uifaces/faces/twitter/tur8le/128.jpg'),('Judy18','https://s3.amazonaws.com/uifaces/faces/twitter/wesleytrankin/128.jpg'),('Remington_Bechtelar12','https://s3.amazonaws.com/uifaces/faces/twitter/vivekprvr/128.jpg'),('Olin_Willms','https://s3.amazonaws.com/uifaces/faces/twitter/jarjan/128.jpg'),('Alisha_Schumm6','https://s3.amazonaws.com/uifaces/faces/twitter/ryanjohnson_me/128.jpg'),('Lulu_Zemlak','https://s3.amazonaws.com/uifaces/faces/twitter/xripunov/128.jpg'),('Kaelyn66','https://s3.amazonaws.com/uifaces/faces/twitter/brunodesign1206/128.jpg'),('Reymundo_Flatley96','https://s3.amazonaws.com/uifaces/faces/twitter/ashernatali/128.jpg'),('Emanuel_Green','https://s3.amazonaws.com/uifaces/faces/twitter/ratbus/128.jpg'),('Manuela93','https://s3.amazonaws.com/uifaces/faces/twitter/borantula/128.jpg'),('Casper71','https://s3.amazonaws.com/uifaces/faces/twitter/agromov/128.jpg'),('Leonie_Wunsch16','https://s3.amazonaws.com/uifaces/faces/twitter/thierrykoblentz/128.jpg'),('Brock41','https://s3.amazonaws.com/uifaces/faces/twitter/marciotoledo/128.jpg'),('Mathias84','https://s3.amazonaws.com/uifaces/faces/twitter/dss49/128.jpg'),('Audra.Will8','https://s3.amazonaws.com/uifaces/faces/twitter/thehacker/128.jpg');
/*!40000 ALTER TABLE `Profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Replies`
--

DROP TABLE IF EXISTS `Replies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Replies` (
  `postID` int(11) DEFAULT NULL,
  `posterID` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `reply_imageID` int(11) DEFAULT NULL,
  `reply_ts` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Replies`
--

LOCK TABLES `Replies` WRITE;
/*!40000 ALTER TABLE `Replies` DISABLE KEYS */;
/*!40000 ALTER TABLE `Replies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SavedImages`
--

DROP TABLE IF EXISTS `SavedImages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SavedImages` (
  `userID` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `saved_imageID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SavedImages`
--

LOCK TABLES `SavedImages` WRITE;
/*!40000 ALTER TABLE `SavedImages` DISABLE KEYS */;
/*!40000 ALTER TABLE `SavedImages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `userID` varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_name` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES ('Aidan.Marks','Corrine','Bechtelar','Hailee.Pouros@yahoo.'),('Alisha_Schumm6','Tyree','Marquardt','Kayley.Smith84@gmail'),('Amely_Corwin','Maximus','McKenzie','Kavon_Beier@gmail.co'),('Angeline1','Krystal','Adams','Sanford45@yahoo.com'),('Audra.Will8','Jerrod','Ruecker','Carol19@hotmail.com'),('Ben70','Agnes','Heaney','Laron_Wisoky@gmail.c'),('Beulah_Reinger15','Geovanny','Veum','Lila.Kling21@yahoo.c'),('Britney_Dickinson6','Breanna','Vandervort','Zackary23@yahoo.com'),('Brock41','Eunice','Rau','Kim.Schiller@yahoo.c'),('Bryce_Cole16','Mathilde','Herzog','Jevon20@gmail.com'),('Camren16','Cathryn','Terry','Henri88@yahoo.com'),('Casper71','Jaquan','Feeney','Jewel_Cartwright24@g'),('Christa.Schulist','Muhammad','Rempel','Joany.Ernser31@gmail'),('Clair69','Lavada','Purdy','Jamaal.Bailey@yahoo.'),('Claude.Shanahan2','Cassandre','Abbott','Anita.Eichmann87@yah'),('Clementina.Ledner','Leonor','Stracke','Alexane.Botsford@hot'),('Dejah26','Turner','Pagac','Doris.Anderson@hotma'),('Dillan_Hauck56','Raina','Kris','Letitia_Mills83@hotm'),('Dolores.Corwin21','Shea','Barton','Ibrahim_Baumbach@hot'),('Donavon72','Nya','Mueller','Emmie79@hotmail.com'),('Emanuel_Green','Buford','Boyer','Carmela91@gmail.com'),('Enos_Gislason70','Rey','Zieme','Roel.Robel@gmail.com'),('Evie_Doyle66','Pierce','Terry','Joannie_Schamberger@'),('four','one','two','3'),('foursfsf','r','two','3'),('Garry_Schneider','Reta','Little','Jake69@hotmail.com'),('Jonas_Mante97','Bobbie','Thiel','Reginald_Hintz14@hot'),('Judy18','Sanford','McDermott','Connie.Simonis@gmail'),('Julianne_Oberbrunner','Anjali','Kreiger','Madaline87@yahoo.com'),('Kaelyn66','Dane','Ankunding','Zackery59@gmail.com'),('Leonie_Wunsch16','Melba','Turcotte','Curt75@yahoo.com'),('Lulu_Zemlak','Cyrus','Stark','Antonio_Hayes26@gmai'),('Mabelle.Davis96','Cullen','Schultz','June23@hotmail.com'),('Manuela93','Emerson','Metz','Daron_Parisian@gmail'),('Marguerite99','Madelyn','Block','Amie50@yahoo.com'),('Mathias84','Marvin','Daniel','Emelia.Daugherty@yah'),('Maximillian57','Mitchell','Cremin','Bradly70@gmail.com'),('Maybell12','Cassandra','McDermott','Hyman_Reichert99@hot'),('Melvina.Konopelski85','Meda','Grimes','Myron.Quigley21@gmai'),('Mohamed42','Cynthia','MacGyver','Adele.Parisian65@hot'),('Olin_Willms','Edmond','Jast','Maxine47@gmail.com'),('Raven_Bergnaum39','Dameon','Baumbach','Douglas.Dooley7@gmai'),('Remington_Bechtelar12','Lillian','Mosciski','Tristian48@yahoo.com'),('Reymundo_Flatley96','Victor','Ziemann','Mina.Feest@hotmail.c'),('Ricardo_Will','Rick','Farrell','Tyshawn.Flatley61@ya'),('Ronaldo81','Sister','Mitchell','Frank.Swift@yahoo.co'),('Roscoe76','Kavon','Cassin','Holly_Kub78@hotmail.'),('Selina68','Imani','Larkin','Agnes_Ratke@gmail.co'),('Shanny.Pacocha','Tyrell','Wilkinson','Jasper8@gmail.com'),('Sonny.Kirlin','Meghan','Tillman','Marcella_Rath@hotmai'),('Vena17','Kurt','Padberg','Jacky_Jaskolski@yaho'),('Zack19','Kraig','Lynch','Ferne_Littel91@yahoo');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-29 21:17:21

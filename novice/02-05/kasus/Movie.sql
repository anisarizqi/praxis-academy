-- MySQL dump 10.17  Distrib 10.3.17-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: Movie
-- ------------------------------------------------------
-- Server version	10.3.17-MariaDB-1:10.3.17+maria~xenial-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Member`
--

DROP TABLE IF EXISTS `Member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Member` (
  `id_member` int(11) NOT NULL AUTO_INCREMENT,
  `f_name` char(250) DEFAULT NULL,
  `p_address` varchar(250) DEFAULT NULL,
  `id_salute` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_member`),
  KEY `fk_member_salute` (`id_salute`),
  CONSTRAINT `fk_member_salute` FOREIGN KEY (`id_salute`) REFERENCES `Salutation` (`id_salute`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Member`
--

LOCK TABLES `Member` WRITE;
/*!40000 ALTER TABLE `Member` DISABLE KEYS */;
INSERT INTO `Member` VALUES (1,'Janet Jones','First Street Plot No. 4',2),(2,'Robert Phil','3rd Street 34',1),(3,'Robert Phil','5th Street 34',1);
/*!40000 ALTER TABLE `Member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Movie`
--

DROP TABLE IF EXISTS `Movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Movie` (
  `id_member` int(11) DEFAULT NULL,
  `n_movie` varchar(250) DEFAULT NULL,
  KEY `fk_movie_member` (`id_member`),
  CONSTRAINT `fk_movie_member` FOREIGN KEY (`id_member`) REFERENCES `Member` (`id_member`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movie`
--

LOCK TABLES `Movie` WRITE;
/*!40000 ALTER TABLE `Movie` DISABLE KEYS */;
INSERT INTO `Movie` VALUES (1,'Pirates of the Caribbean'),(1,'Clash of the Titan'),(2,'Forgetting Sarah Marshal'),(2,'Daddy\'s Little Girls'),(3,'Clash of the Titans');
/*!40000 ALTER TABLE `Movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Salutation`
--

DROP TABLE IF EXISTS `Salutation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Salutation` (
  `id_salute` int(11) NOT NULL AUTO_INCREMENT,
  `salute` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_salute`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Salutation`
--

LOCK TABLES `Salutation` WRITE;
/*!40000 ALTER TABLE `Salutation` DISABLE KEYS */;
INSERT INTO `Salutation` VALUES (1,'Mr.'),(2,'Ms.'),(3,'Mrs.'),(4,'Dr.');
/*!40000 ALTER TABLE `Salutation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-04 13:30:48

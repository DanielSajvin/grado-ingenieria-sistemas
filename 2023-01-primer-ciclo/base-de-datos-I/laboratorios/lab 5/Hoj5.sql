-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comercio`
--

DROP TABLE IF EXISTS `comercio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comercio` (
  `Id` int NOT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comercio`
--

LOCK TABLES `comercio` WRITE;
/*!40000 ALTER TABLE `comercio` DISABLE KEYS */;
INSERT INTO `comercio` VALUES (1,'Amazon'),(2,'Netflix'),(3,'Disney'),(4,'Spotify'),(5,'Lol'),(6,'Valorant'),(7,'Xbox'),(8,'Play Station'),(9,'Nintendo'),(10,'FIFA');
/*!40000 ALTER TABLE `comercio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comercio_has_venta`
--

DROP TABLE IF EXISTS `comercio_has_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comercio_has_venta` (
  `Comercio_Id` int NOT NULL,
  `Venta_Id` int NOT NULL,
  PRIMARY KEY (`Comercio_Id`,`Venta_Id`),
  KEY `fk_Comercio_has_Venta_Venta1_idx` (`Venta_Id`),
  KEY `fk_Comercio_has_Venta_Comercio1_idx` (`Comercio_Id`),
  CONSTRAINT `fk_Comercio_has_Venta_Comercio1` FOREIGN KEY (`Comercio_Id`) REFERENCES `comercio` (`Id`),
  CONSTRAINT `fk_Comercio_has_Venta_Venta1` FOREIGN KEY (`Venta_Id`) REFERENCES `venta` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comercio_has_venta`
--

LOCK TABLES `comercio_has_venta` WRITE;
/*!40000 ALTER TABLE `comercio_has_venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `comercio_has_venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fallo`
--

DROP TABLE IF EXISTS `fallo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fallo` (
  `Codigo` int NOT NULL,
  `Descripcion_fallo` varchar(45) DEFAULT NULL,
  `Productos` varchar(45) DEFAULT NULL,
  `Cantidad` int DEFAULT NULL,
  `Total` float DEFAULT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fallo`
--

LOCK TABLES `fallo` WRITE;
/*!40000 ALTER TABLE `fallo` DISABLE KEYS */;
/*!40000 ALTER TABLE `fallo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `Id` int NOT NULL,
  `Descripción` varchar(45) DEFAULT NULL,
  `Precio_unitario` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Tarjeta Spotify','100.00'),(2,'Tarjeta Netflix','120.00'),(3,'Tarjeta Amazon','245.00'),(4,'Tarjeta Valorant','300.00'),(5,'Tarjeta Lol','250.00');
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_has_venta`
--

DROP TABLE IF EXISTS `producto_has_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto_has_venta` (
  `Producto_Id` int NOT NULL,
  `Venta_Id` int NOT NULL,
  PRIMARY KEY (`Producto_Id`,`Venta_Id`),
  KEY `fk_Producto_has_Venta_Venta1_idx` (`Venta_Id`),
  KEY `fk_Producto_has_Venta_Producto1_idx` (`Producto_Id`),
  CONSTRAINT `fk_Producto_has_Venta_Producto1` FOREIGN KEY (`Producto_Id`) REFERENCES `producto` (`Id`),
  CONSTRAINT `fk_Producto_has_Venta_Venta1` FOREIGN KEY (`Venta_Id`) REFERENCES `venta` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_has_venta`
--

LOCK TABLES `producto_has_venta` WRITE;
/*!40000 ALTER TABLE `producto_has_venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `producto_has_venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarjeta`
--

DROP TABLE IF EXISTS `tarjeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarjeta` (
  `Id` int NOT NULL,
  `Número` varchar(45) DEFAULT NULL,
  `Fecha_vencimiento` date DEFAULT NULL,
  `Nombre_tarjeta` varchar(45) DEFAULT NULL,
  `Marca` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarjeta`
--

LOCK TABLES `tarjeta` WRITE;
/*!40000 ALTER TABLE `tarjeta` DISABLE KEYS */;
/*!40000 ALTER TABLE `tarjeta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_usuario`
--

DROP TABLE IF EXISTS `tipo_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_usuario` (
  `Id` int NOT NULL,
  `Preferencial` tinyint DEFAULT NULL,
  `Normal` tinyint DEFAULT NULL,
  `Oro` tinyint DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_usuario`
--

LOCK TABLES `tipo_usuario` WRITE;
/*!40000 ALTER TABLE `tipo_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `Id` int NOT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  `Dirección` varchar(45) DEFAULT NULL,
  `Correo_electronico` varchar(45) DEFAULT NULL,
  `País_residente` varchar(45) DEFAULT NULL,
  `Tipo_usuario_Id` int NOT NULL,
  `Tarjeta_Id` int NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_Usuario_Tipo_usuario_idx` (`Tipo_usuario_Id`),
  KEY `fk_Usuario_Tarjeta1_idx` (`Tarjeta_Id`),
  CONSTRAINT `fk_Usuario_Tarjeta1` FOREIGN KEY (`Tarjeta_Id`) REFERENCES `tarjeta` (`Id`),
  CONSTRAINT `fk_Usuario_Tipo_usuario` FOREIGN KEY (`Tipo_usuario_Id`) REFERENCES `tipo_usuario` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `Id` int NOT NULL,
  `Cantidad` int DEFAULT NULL,
  `Descripccion` varchar(45) DEFAULT NULL,
  `Sub_total` float DEFAULT NULL,
  `Codigo_para_usar` varchar(45) DEFAULT NULL,
  `Comercio` varchar(45) DEFAULT NULL,
  `Total` float DEFAULT NULL,
  `Usuario_Id` int NOT NULL,
  `Fallo_Codigo` int NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_Venta_Usuario1_idx` (`Usuario_Id`),
  KEY `fk_Venta_Fallo1_idx` (`Fallo_Codigo`),
  CONSTRAINT `fk_Venta_Fallo1` FOREIGN KEY (`Fallo_Codigo`) REFERENCES `fallo` (`Codigo`),
  CONSTRAINT `fk_Venta_Usuario1` FOREIGN KEY (`Usuario_Id`) REFERENCES `usuario` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-04 23:53:16

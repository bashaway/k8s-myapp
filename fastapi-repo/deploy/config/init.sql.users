SET FOREIGN_KEY_CHECKS=0;

-- -- -- -- -- -- -- -- -- -- -- --
-- SCHEMA : hero
-- -- -- -- -- -- -- -- -- -- -- --

DROP TABLE IF EXISTS `heroes`;
CREATE TABLE `heroes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `secret_name` varchar(200) NOT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


-- -- -- -- -- -- -- -- -- -- -- --
-- SCHEMA : users / groups
-- -- -- -- -- -- -- -- -- -- -- --

DROP TABLE IF EXISTS `groups`;
CREATE TABLE `groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `email` varchar(32) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  KEY `group_id` (`group_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


SET FOREIGN_KEY_CHECKS=1;


-- -- -- -- -- -- -- -- -- -- -- --
-- DATA : heroes
-- -- -- -- -- -- -- -- -- -- -- --
INSERT INTO `heroes` VALUES (1,'No.01','aho',10);
INSERT INTO `heroes` VALUES (2,'No.02','baka',20);
INSERT INTO `heroes` VALUES (3,'No.03','manuke', DEFAULT);
INSERT INTO `heroes` VALUES (4,'No.04','secname_04',24);

-- -- -- -- -- -- -- -- -- -- -- --
-- DATA : groups
-- -- -- -- -- -- -- -- -- -- -- --
INSERT INTO `groups` VALUES (1,'firstgroup','最初のグループ');
INSERT INTO `groups` VALUES (2,'secondgroup','二番目のグループ');
INSERT INTO `groups` VALUES (3,'thirdgroup','さんばんめのグループ');

-- -- -- -- -- -- -- -- -- -- -- --
-- DATA : users
-- -- -- -- -- -- -- -- -- -- -- --
INSERT INTO `users` VALUES (1,'Alice','Alice@example.com',1);
INSERT INTO `users` VALUES (2,'Bob','Bob@example.com',2);
INSERT INTO `users` VALUES (3,'Carol','Carol@example.com',3);
INSERT INTO `users` VALUES (4,'Dave','Dave@example.com',1);
INSERT INTO `users` VALUES (5,'Eve','Eve@example.com',2);
INSERT INTO `users` VALUES (6,'Faythe','Faythe@example.com',3);
INSERT INTO `users` VALUES (7,'Frank','Frank@example.com',1);
INSERT INTO `users` VALUES (8,'Grace','Grace@example.com',2);
INSERT INTO `users` VALUES (9,'Heidi','Heidi@example.com',3);
INSERT INTO `users` VALUES (10,'Ivan','Ivan@example.com',1);
INSERT INTO `users` VALUES (11,'Judy','Judy@example.com',2);
INSERT INTO `users` VALUES (12,'Mallory','Mallory@example.com',3);
INSERT INTO `users` VALUES (13,'Michael','Michael@example.com',1);
INSERT INTO `users` VALUES (14,'Niaj','Niaj@example.com',2);
INSERT INTO `users` VALUES (15,'Olivia','Olivia@example.com',3);
INSERT INTO `users` VALUES (16,'Oscar','Oscar@example.com',1);
INSERT INTO `users` VALUES (17,'Peggy','Peggy@example.com',2);
INSERT INTO `users` VALUES (18,'Rupert','Rupert@example.com',3);
INSERT INTO `users` VALUES (19,'Shaquille','Shaquille@example.com',1);
INSERT INTO `users` VALUES (20,'Sybil','Sybil@example.com',2);
INSERT INTO `users` VALUES (21,'Trent','Trent@example.com',3);
INSERT INTO `users` VALUES (22,'Trudy','Trudy@example.com',1);
INSERT INTO `users` VALUES (23,'Victor','Victor@example.com',2);
INSERT INTO `users` VALUES (24,'Walter','Walter@example.com',3);
INSERT INTO `users` VALUES (25,'Wendy','Wendy@example.com',1);
INSERT INTO `users` VALUES (26,'0026','0026@example.com',2);
INSERT INTO `users` VALUES (27,'0027','0027@example.com',3);
INSERT INTO `users` VALUES (28,'0028','0028@example.com',1);
INSERT INTO `users` VALUES (29,'0029','0029@example.com',2);
INSERT INTO `users` VALUES (30,'0030','0030@example.com',3);
INSERT INTO `users` VALUES (31,'0031','0031@example.com',1);
INSERT INTO `users` VALUES (32,'0032','0032@example.com',2);
INSERT INTO `users` VALUES (33,'0033','0033@example.com',3);
INSERT INTO `users` VALUES (34,'0034','0034@example.com',1);
INSERT INTO `users` VALUES (35,'0035','0035@example.com',2);
INSERT INTO `users` VALUES (36,'0036','0036@example.com',3);
INSERT INTO `users` VALUES (37,'0037','0037@example.com',1);
INSERT INTO `users` VALUES (38,'0038','0038@example.com',2);
INSERT INTO `users` VALUES (39,'0039','0039@example.com',3);
INSERT INTO `users` VALUES (40,'0040','0040@example.com',1);
INSERT INTO `users` VALUES (41,'0041','0041@example.com',2);
INSERT INTO `users` VALUES (42,'0042','0042@example.com',3);
INSERT INTO `users` VALUES (43,'0043','0043@example.com',1);
INSERT INTO `users` VALUES (44,'0044','0044@example.com',2);
INSERT INTO `users` VALUES (45,'0045','0045@example.com',3);
INSERT INTO `users` VALUES (46,'0046','0046@example.com',1);
INSERT INTO `users` VALUES (47,'0047','0047@example.com',2);
INSERT INTO `users` VALUES (48,'0048','0048@example.com',3);
INSERT INTO `users` VALUES (49,'0049','0049@example.com',1);
INSERT INTO `users` VALUES (50,'0050','0050@example.com',2);
INSERT INTO `users` VALUES (51,'0051','0051@example.com',3);
INSERT INTO `users` VALUES (52,'0052','0052@example.com',1);
INSERT INTO `users` VALUES (53,'0053','0053@example.com',2);
INSERT INTO `users` VALUES (54,'0054','0054@example.com',3);
INSERT INTO `users` VALUES (55,'0055','0055@example.com',1);

/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : lab

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2019-05-13 22:59:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `article`
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL COMMENT '文章名',
  `content` longtext COMMENT '文章内容',
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `author` int(10) DEFAULT NULL COMMENT '作者的ID',
  `tag` varchar(255) DEFAULT NULL COMMENT '包含的tag,逗号隔开',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of article
-- ----------------------------
INSERT INTO `article` VALUES ('1', '测试', '<p>测试我们的系统能不能用！</p>', '2019-05-13 21:07:34', null, '13');
INSERT INTO `article` VALUES ('5', '测试', '<p><u>测试测测﻿</u></p><p><u>egwj dnaskbrgpw\'3ejgrb fsa </u></p><pre class=\"ql-syntax\" spellcheck=\"false\">fefw dsdffeb fadbsbgved\n\n</pre><p>ewbf<img src=\"http://localhost:5000/static/uploads/15577594209e007ee71b07bbfe54d2af648d7f5bc01610ef29.jpg\"></p>', '2019-05-13 22:57:03', null, '15');

-- ----------------------------
-- Table structure for `tag`
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `ID` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL COMMENT 'tag名',
  `father` int(5) DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES ('1', '编译器', null);
INSERT INTO `tag` VALUES ('2', '前端', null);
INSERT INTO `tag` VALUES ('3', '后端', null);
INSERT INTO `tag` VALUES ('4', '进阶', null);
INSERT INTO `tag` VALUES ('5', 'JQuery', '2');
INSERT INTO `tag` VALUES ('6', 'Vue', '2');
INSERT INTO `tag` VALUES ('7', 'VueCli', '6');
INSERT INTO `tag` VALUES ('8', 'VsCode', '1');
INSERT INTO `tag` VALUES ('15', '测试', null);

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `Snum` varchar(20) NOT NULL COMMENT '学号',
  `username` varchar(20) DEFAULT NULL COMMENT '账号',
  `password` varchar(255) DEFAULT NULL COMMENT '密码',
  `phone` varchar(20) DEFAULT NULL COMMENT '手机号',
  `group` int(2) DEFAULT NULL COMMENT '用户组',
  `token` varchar(40) NOT NULL DEFAULT '',
  `face` varchar(255) DEFAULT NULL COMMENT '人脸图片名',
  PRIMARY KEY (`ID`,`Snum`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '17H034160322', 'yuncn', 'e63d5a15d31234b160911313fa3bbb63ddcf67653afd66fd83c229222e7dbc03', null, '0', 'n0okrFhwA8xp1iT3ZLfRatMvK', 'JwQkipKR3FBD40u1jEUvX8S9M.bmp');
INSERT INTO `user` VALUES ('2', '17H034160234', 'hanerx', 'ec847003d2eadc9baf60853e8391e167a292c21f01892fcb8bad0f4af6cd74a7', null, '0', 'jyoxfq8s59H6RBb07POpYiSgw', 'duG2y8CkUVQA5SgnJi49qW0oR.bmp');

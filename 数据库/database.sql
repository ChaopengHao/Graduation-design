SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `DJ_HAO` DEFAULT CHARACTER SET utf8 ;
USE `DJ_HAO` ;

-- -----------------------------------------------------
-- Table `DJ_HAO`.`shop`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DJ_HAO`.`shop` (
  `shop_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `shop_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`shop_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DJ_HAO`.`jd_goods`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DJ_HAO`.`jd_goods` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(25) NOT NULL,
  `comment_num` INT ZEROFILL NULL DEFAULT NULL,
  `goods_id` VARCHAR(25) NOT NULL,
  `link` VARCHAR(50) NOT NULL,
  `commentVersion` VARCHAR(25) NULL DEFAULT NULL,
  `score1count` VARCHAR(25) NULL DEFAULT NULL,
  `score2count` VARCHAR(25) NULL DEFAULT NULL,
  `score3count` VARCHAR(25) NULL DEFAULT NULL,
  `score4count` VARCHAR(25) NULL DEFAULT NULL,
  `score5count` VARCHAR(25) NULL DEFAULT NULL,
  `price` VARCHAR(25) NOT NULL,
  `shop_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_jd_goods_shop1_idx` (`shop_id` ASC),
  CONSTRAINT `fk_jd_goods_shop1`
    FOREIGN KEY (`shop_id`)
    REFERENCES `DJ_HAO`.`shop` (`shop_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `DJ_HAO`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DJ_HAO`.`city` (
  `city_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `city` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`city_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DJ_HAO`.`address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DJ_HAO`.`address` (
  `idaddress` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(45) NOT NULL,
  `addresscol` VARCHAR(45) NULL,
  `city_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`idaddress`),
  INDEX `fk_address_city_idx` (`city_id` ASC),
  CONSTRAINT `fk_address_city`
    FOREIGN KEY (`city_id`)
    REFERENCES `DJ_HAO`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DJ_HAO`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DJ_HAO`.`user` (
  `user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(25) NOT NULL,
  `password` VARCHAR(25) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `age` INT ZEROFILL NOT NULL,
  `active` TINYINT(1) NOT NULL,
  `create_time` DATE NOT NULL,
  `address_id` INT UNSIGNED NOT NULL,
  `sex` VARCHAR(10) NOT NULL,
  `phone` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`),
  INDEX `fk_user_address1_idx` (`address_id` ASC),
  CONSTRAINT `fk_user_address1`
    FOREIGN KEY (`address_id`)
    REFERENCES `DJ_HAO`.`address` (`idaddress`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DJ_HAO`.`label`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DJ_HAO`.`label` (
  `label_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `jd_goods_id` INT UNSIGNED NOT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`label_id`),
  INDEX `fk_label_jd_goods1_idx` (`jd_goods_id` ASC),
  INDEX `fk_label_user1_idx` (`user_id` ASC),
  CONSTRAINT `fk_label_jd_goods1`
    FOREIGN KEY (`jd_goods_id`)
    REFERENCES `DJ_HAO`.`jd_goods` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_label_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `DJ_HAO`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DJ_HAO`.`order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DJ_HAO`.`order` (
  `order_id` INT NOT NULL,
  `number` INT NOT NULL,
  `total_price` VARCHAR(25) NOT NULL,
  `jd_goods_id` INT UNSIGNED NOT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`order_id`),
  INDEX `fk_order_jd_goods1_idx` (`jd_goods_id` ASC),
  INDEX `fk_order_user1_idx` (`user_id` ASC),
  CONSTRAINT `fk_order_jd_goods1`
    FOREIGN KEY (`jd_goods_id`)
    REFERENCES `DJ_HAO`.`jd_goods` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `DJ_HAO`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `DJ_HAO` ;

-- -----------------------------------------------------
-- Placeholder table for view `DJ_HAO`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DJ_HAO`.`view1` (`id` INT);

-- -----------------------------------------------------
-- View `DJ_HAO`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `DJ_HAO`.`view1`;
USE `DJ_HAO`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

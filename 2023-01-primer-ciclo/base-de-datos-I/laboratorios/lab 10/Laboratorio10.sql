delimiter //

DROP TRIGGER if exists InsertarArticulo//

CREATE TRIGGER InsertarArticulo
AFTER INSERT ON articulos
FOR EACH ROW
BEGIN
	DECLARE articulo INT DEFAULT 0;
    -- SET articulo := new.NoArticulos;
    SELECT NoArticulos INTO articulo FROM estudiante;
    SET articulo=articulo+1;
	UPDATE estudiante SET NoArticulos = articulo WHERE id=new.Estudiante_id;

END //

delimiter ;

delimiter //

DROP TRIGGER if exists Autorizaciones//

CREATE TRIGGER Autorizaciones
AFTER UPDATE ON articulos
FOR EACH ROW
BEGIN
	DECLARE autorizar INT DEFAULT 0;
	IF EXISTS (SELECT NEW.Estudiante_autorizaciones IS NOT NULL) THEN
    -- SET articulo := new.NoArticulos;
    SELECT NoAprobaciones INTO autorizar FROM estudiante WHERE id=new.Estudiante_autorizaciones;
    SET autorizar=autorizar+1;
	UPDATE estudiante SET NoAprobaciones = autorizar WHERE id=new.Estudiante_autorizaciones;
    END IF;

END // 

delimiter ;

delimiter //

DROP TRIGGER if exists ComentarioAumentar//

CREATE TRIGGER ComentarioAumentar
AFTER INSERT ON comentario
FOR EACH ROW
BEGIN
	DECLARE cmt INT DEFAULT 0;
    -- SET articulo := new.NoArticulos;
    SELECT NoComentarios INTO cmt FROM estudiante WHERE id=new.Estudiante_id;
    SET cmt=cmt+1;
	UPDATE estudiante SET NoComentarios = cmt WHERE id=new.Estudiante_id;

END //

delimiter ;

delimiter //

DROP TRIGGER if exists Fecha_articulo//

CREATE TRIGGER Fecha_articulo
BEFORE INSERT ON articulos
FOR EACH ROW
BEGIN
	SET new.Fecha = CURDATE();
	-- UPDATE comentario SET Fecha

END//
delimiter ;

delimiter //

DROP TRIGGER if exists Fecha_comentario//

CREATE TRIGGER Fecha_comentario
BEFORE INSERT ON comentario
FOR EACH ROW
BEGIN
	SET new.Fecha = CURDATE();
	-- UPDATE comentario SET Fecha

END//
delimiter ;

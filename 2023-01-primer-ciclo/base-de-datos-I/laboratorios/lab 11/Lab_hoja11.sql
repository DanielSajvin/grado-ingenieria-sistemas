delimiter //

drop trigger if exists EliminarEstudiante //

CREATE TRIGGER EliminarEstudiante 
BEFORE DELETE ON estudiante
FOR EACH ROW
BEGIN
  -- DELETE FROM comentario WHERE Articulos_id IN (SELECT id FROM articulos WHERE Estudiante_id = OLD.id);
  -- DELETE FROM articulos WHERE Estudiante_autorizaciones = OLD.id;
  
  -- UPDATE articulos SET EstudianteAutorizacion_id = NULL WHERE EstudianteAutorizacion_id = OLD.id;
  -- DELETE FROM articulos WHERE Estudiante_id = OLD.id;
SET FOREIGN_KEY_CHECKS=0;
DELETE FROM comentario WHERE Articulos_id IN (SELECT id FROM articulos WHERE Estudiante_id = OLD.id);
DELETE FROM articulos WHERE Estudiante_id = OLD.id;
SET FOREIGN_KEY_CHECKS=1;
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
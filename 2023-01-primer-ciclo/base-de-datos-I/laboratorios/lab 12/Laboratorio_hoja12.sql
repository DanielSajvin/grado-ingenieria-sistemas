delimiter //

-- DROP TRIGGER if exists DescontarFactura //

CREATE TRIGGER DescontarFactura
AFTER INSERT ON detallefactura
FOR EACH ROW
BEGIN
	DECLARE cantidad INT DEFAULT 0;
    DECLARE inventario INT DEFAULT 0;
    -- SELECT d.Cantidad INTO cantidad FROM detallefactura d WHERE id=new.Id;
    SELECT p.Existencias INTO inventario FROM producto p WHERE id=new.Producto_Id;
    
    SET cantidad = inventario - new.Cantidad;
    -- UPDATE estudiante SET NoComentarios = cmt WHERE id=new.Estudiante_id;
    UPDATE producto SET Existencias = cantidad WHERE id=new.Producto_Id;
    -- SELECT NoComentarios INTO cmt FROM estudiante WHERE id=new.Estudiante_id;
END //

delimiter ;

delimiter //

DROP TRIGGER if exists AnularFactura //

CREATE TRIGGER AnularFactura
AFTER UPDATE ON detallefactura
FOR EACH ROW
BEGIN
DECLARE exis INT DEFAULT 0;
DECLARE cant INT DEFAULT 0;
IF NEW.Anulado = 1 THEN
	SELECT p.Existencias INTO exis FROM producto p WHERE id=OLD.Producto_Id;
    SET exis = OLD.Cantidad + exis;
    UPDATE producto SET Existencias = exis WHERE id=OLD.Producto_Id;
END IF;

END //

delimiter ; 
-- EJERCICIO 1 -- 
delimiter //
-- DROP PROCEDURE CrearProducto
CREATE PROCEDURE CrearProducto(vId INT, vNombre VARCHAR(45), vPrecio FLOAT, vExistenciaTotal FLOAT, vAnulado boolean)
BEGIN
	INSERT INTO producto(Id, Nombre, Precio, ExistenciaTotal, Anulado) VALUES(vId, vNombre, vPrecio, vExistenciaTotal, Anulado);
END //
delimiter ;

call CrearProducto(1, "Producto1", 10.2, 100, 0);

-- EJERCICIO 2 inciso a--
delimiter //
-- DROP TRIGGER if exists CrearLote//
CREATE TRIGGER CrearLote
AFTER INSERT ON producto
FOR EACH ROW
BEGIN
	DECLARE vId INT DEFAULT 0;
    DECLARE vIdFin INT DEFAULT 0;
    DECLARE vExistencia INT DEFAULT 0;
    DECLARE vIdProducto INT DEFAULT 0;
    -- SELECT MAX(NoLote) INTO vId FROM lote;  
    SELECT IFNULL(MAX(NoLote), 0) INTO vId FROM Lote;
    SET vIdFin = vId+1;
    SELECT ExistenciaTotal INTO vExistencia FROM producto WHERE id=new.id;
    SELECT Id INTO vIdProducto FROM producto WHERE id=new.id;
    INSERT INTO lote(NoLote, Fecha, ExistenciaInicial, ExistenciaActual, Terminado, Producto_Id) 
		VALUES(vIdFin, curdate(), vExistencia, vExistencia, 0, vIdProducto);

END //
delimiter ;

-- EJERCICIO 2 inciso b--
delimiter //
-- DROP TRIGGER if exists CrearMovimiento//
CREATE TRIGGER CrearMovimiento
AFTER INSERT ON lote
FOR EACH ROW
BEGIN
	DECLARE vMovimiento VARCHAR(45);
    DECLARE vId INT DEFAULT 0;
    DECLARE vEntrada INT DEFAULT 0;
    SELECT id INTO vId FROM lote WHERE id=new.id;
    SET vMovimiento = CONCAT("Lote Nuevo ID: ", vId);
    SELECT ExistenciaInicial INTO vEntrada FROM lote WHERE id=new.id;
    INSERT INTO movimiento(Motivo, CantidadEntrada, CantidadSalida, Lote_id) 
    VALUES(vMovimiento, vEntrada, 0, vId);
    
END //
delimiter ; 

-- EJERCICIO 3 inciso a --
delimiter //
CREATE TRIGGER AnularProducto
AFTER UPDATE ON producto
FOR EACH ROW
BEGIN
	UPDATE lote SET ExistenciaInicial = 0 WHERE id=new.id; 
    UPDATE lote SET ExistenciaActual = 0 WHERE id=new.id;
    UPDATE lote SET Terminado = 1 WHERE id=new.id;

END //
delimiter ;

-- EJERCICIO 3 inciso b --
delimiter //
CREATE TRIGGER MovimientoAnular
AFTER UPDATE ON lote
FOR EACH ROW
BEGIN
	DECLARE vMovimiento VARCHAR(45);
    DECLARE vId INT DEFAULT 0;
    -- DECLARE vEntrada INT DEFAULT 0;
    SELECT id INTO vId FROM lote WHERE id=new.id;
    SET vMovimiento = CONCAT("Anulación de lote ID: ", vId);
    -- SELECT ExistenciaInicial INTO vEntrada FROM lote WHERE id=new.id;
    INSERT INTO movimiento(Motivo, CantidadEntrada, CantidadSalida, Lote_id) 
    VALUES(vMovimiento, 0, 0, vId);

END //
delimiter ;


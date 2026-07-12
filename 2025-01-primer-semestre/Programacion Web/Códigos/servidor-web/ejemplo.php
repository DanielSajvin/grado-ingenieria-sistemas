<?php
session_start();
if (!isset($_SESSION['contador'])) {
    $_SESSION['contador'] = 0;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $_SESSION['contador']++;
    if (isset($_POST['reset'])) {
        $_SESSION['contador'] = 0;
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contador de Clics</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Contador de Clics</h1>
    <p>Has hecho clic <strong><?php echo $_SESSION['contador']; ?></strong> veces.</p>

    <form method="post">
        <label for="valor1"></label>
        <input type="text" name="valor1">
        <br />
        <button type="submit" name='agregar'>Hacer Click</button>
    </form>

    <form method="post">
        <button type="submit" name="reset">Reiniciar</button>
    </form>

</body>
</html>
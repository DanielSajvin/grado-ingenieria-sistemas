const express = require("express");
const app = express();

app.use(express.json());

// sumar GET
app.get('/suma', (req, res) => {
    const a = parseFloat(req.query.a);
    const b = parseFloat(req.query.b);
    res.send({
        SumaGet: a+b,
    });
})

// sumar POST
app.post('/suma', (req, res) => {
    const {a, b} = (req.body);
    resultado = parseFloat(a) + parseFloat(b)
    res.send({
        SumaPost: resultado,
    })
})

// restar GET
app.get('/resta', (req, res) => {
    const a = parseFloat(req.query.a);
    const b = parseFloat(req.query.b);
    res.send({
        RestaGet: a-b,
    });
})

// restar POST
app.post('/resta', (req, res) => {
    const {a, b} = (req.body);
    resultado = parseFloat(a) - parseFloat(b)
    res.send({
        RestaPost: resultado,
    })
})

// multiplicacion GET
app.get('/multiplica', (req, res) => {
    const a = parseFloat(req.query.a);
    const b = parseFloat(req.query.b);
    res.send({
        MultiplicacionGet: a*b,
    });
})

// multiplicacion POST
app.post('/multiplica', (req, res) => {
    const {a, b} = (req.body);
    resultado = parseFloat(a) * parseFloat(b)
    res.send({
        MultiplicacionPost: resultado,
    })
})

// division GET
app.get('/dividir', (req, res) => {
    const a = parseFloat(req.query.a);
    const b = parseFloat(req.query.b);
    res.send({
        DivisionGet: a/b,
    });
})

// division POST
app.post('/dividir', (req, res) => {
    const {a, b} = (req.body);
    resultado = parseFloat(a) / parseFloat(b)
    res.send({
        DivisionPost: resultado,
    })
})

app.listen(3000, () => {
    console.log("Servidor corriendo en el puerto 3000");
  });
import express from 'express'
import cors  from 'cors'

const app = express()
const port = 3000

app.use(cors())
app.use(express.json())
app.use(express.static('./frontend')) // Está correto?

app.listen(port, ()=>{console.log(`Servidor ligando na porta: http://localhost:${port}`)})



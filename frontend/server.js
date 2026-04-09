import express from 'express'
import cors  from 'cors'
import path from 'path'
import { fileURLToPath } from 'url'

const app = express()
const port = 3000

// Dirname no ESmodules
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

app.use(cors({origin: `*`}))
app.use(express.json())
app.use(express.static('../frontend')) 

app.use('/', (req,res)=>{
    res.sendFile(path.join(__dirname,"index.html"))
});

app.use((req,res,next) => {
    console.log('Passou aqui')
    next()
    /* res.json([{nome: 'Luan'}]) */
})

app.listen(port, ()=>{console.log(`Servidor ligando na porta: http://localhost:${port}`)})



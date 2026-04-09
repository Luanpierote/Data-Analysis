//Objetivo: Usar este ambiente para coletar os dados do backend, e apartir deles gerar um gráfico de função(com apoio da biblioteca: Chart.js ou Plotly)
//criar um servidor frontend(port:5500)

fetch("http://127.0.0.1:5000/usuarios")
.then(res => res.json())
.then(data => {
    console.log(data)
});



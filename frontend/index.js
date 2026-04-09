//Objetivo: Usar este ambiente para coletar os dados do backend, e apartir deles gerar um gráfico de função(com apoio da biblioteca: Chart.js ou Plotly)
//criar um servidor frontend(port:5500)

const tbody = document.querySelector(".tabela tbody")


window.addEventListener("DOMContentLoaded", async () => {
    fetch("http://127.0.0.1:5000/usuarios")
        .then(res => {
            if (!res.ok) {
                throw new Error("Erro na resposta")
            }
            return res.json()
        })
        .then(data => {
            tbody.innerHTML = '' // Limpa uma vez

            data.forEach((item, index) => {
                const linha = document.createElement("tr")


                // Index temporário
                linha.innerHTML = `
                <td>${index + 1}</td>
                <td>${item[0]}</td>
                <td>${item[1]}</td>
                
                `

                tbody.appendChild(linha)
            })
        })
        .catch(err => {
            console.error("Erro:", err)
        });
});


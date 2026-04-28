//Objetivo: Usar este ambiente para coletar os dados do backend, e apartir deles gerar um gráfico de função(com apoio da biblioteca: Chart.js ou Plotly)
//criar um servidor frontend(port:5500)
// Obs: Chart.js: Pelo CDN é mais prático para testes, do que pelo import


const tbody = document.getElementById("table-user")
const tbody_csv = document.getElementById("table-imovel")
const ctx = document.getElementById('mychart').getContext("2d");
const template = /** @type {HTMLTemplateElement} */ (
    document.getElementById("tmplLinha")
)
const template_2 = /** @type {HTMLTemplateElement} */ (
    document.getElementById("tmplLinha_2")
)


window.addEventListener("DOMContentLoaded", async () => {
    buscarUsuarios();
    buscarImóveis();
})

async function buscarUsuarios() {

    try {
        const res = await fetch("http://127.0.0.1:5000/usuarios")
        if (!res.ok) {
            throw new Error(`Erro ${res.status}: ${res.statusText}`)
        }
        const data = await res.json()
        renderizarDados_alunos(data)

    } catch (err) {
        console.error("Erro:", err)
    }

}

async function buscarImóveis() {
    try {
        const res = await fetch("http://127.0.0.1:5000/imoveis")
        if (!res.ok) {
            throw new Error(`Erro ${res.status}: ${res.statusText}`)
        }
        const data = await res.json()
        renderizarGrafico_csv(data.grafico)
        renderizarDados_csv(data.tabela)
    } catch (err) {
        console.error("Erro:", err)
    }
}


function renderizarDados_alunos(dados) {
    tbody.innerHTML = '' // Limpa uma vez

    dados.forEach((item, index) => {
        // Index temporário
        const clone = template.content.cloneNode(true)

        clone.querySelector(".id").textContent = item[0]
        clone.querySelector(".nome").textContent = item[1]
        clone.querySelector(".nota").textContent = item[2]
        clone.querySelector(".aprovacao").textContent = item[3]

        tbody.appendChild(clone)
    })

}

// Substituir por uma função que pega as labels e os valores target da tabela census
// Criar um histograma com um objeto chart(usando canvas)
function renderizarDados_csv(dados) {
    tbody_csv.innerHTML = ""// Limpa uma vez

    //Limitar os dados aos primeiros 10 itens
    dados.forEach((item) => {
        const clone = template_2.content.cloneNode(true)

        clone.querySelector(".id").textContent = item.id;
        clone.querySelector(".date").textContent = item.date;
        clone.querySelector(".price").textContent = item.price;
        clone.querySelector(".bedrooms").textContent = item.bedrooms;
        clone.querySelector(".bathrooms").textContent = item.bathrooms;
        clone.querySelector(".sqft_living").textContent = item.sqft_living;
        clone.querySelector(".sqft_lot").textContent = item.sqft_lot;
        clone.querySelector(".floors").textContent = item.floors;

        tbody_csv.appendChild(clone)
    })

    // Organizar as datas por ordem cronológica
    dados.sort((a, b) => new Date(a.date) - new Date(b.date))


}


function renderizarGrafico_csv(dados) {
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: dados.map((item) => item.date),
            datasets: [{
                label: '# Property Price',
                data: dados.map((item) => item.price),
                backgroundColor: [
                    'rgb(67, 120, 136)'
                ],
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.5
            }],

        },
        options: {
            // Para respeitar as alterações CSS
            responsive: true,
            maintainAspectRatio: false,
            
            //O gráfico mantém a qualidade
            devicePixelRatio: 2,
            // Adicionando título
            plugins: {
                title: {
                    display: true,
                    text: 'Tendência do preço dos imóveis(média móvel)',
                    color: '#000000',
                    font: {
                        size: 18
                    }
                }
            },
            // Organizando a linha X em ordem cronológica
            scales: {
                x: {
                    type: "time",
                    time: {
                        unit: "month"
                    },
                    title:{
                        display:true,
                        text: "Período(mês)",
                        font: {
                            size: 15,
                            weight: 'bold'
                        }
                    }
                },
                y: {
                    beginAtZero: false,
                    title:{
                        display:true,
                        text: "Valor da propriedade",
                        font: {
                            size: 15,
                            weight: 'bold'
                        }
                    }
                }
            }
        }

    });
}





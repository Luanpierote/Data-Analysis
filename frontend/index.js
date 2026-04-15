//Objetivo: Usar este ambiente para coletar os dados do backend, e apartir deles gerar um gráfico de função(com apoio da biblioteca: Chart.js ou Plotly)
//criar um servidor frontend(port:5500)

const tbody = document.getElementById("table-user")
const tbody_csv = document.getElementById("table-imovel")

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
        renderizarDados(data)

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
        renderizarDados_csv(data)
    } catch (err) {
        console.error("Erro:", err)
    }
}


function renderizarDados(dados) {
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

function renderizarDados_csv(dados){
    tbody_csv.innerHTML = '' // Limpa uma vez

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
}

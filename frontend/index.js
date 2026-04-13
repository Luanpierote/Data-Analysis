//Objetivo: Usar este ambiente para coletar os dados do backend, e apartir deles gerar um gráfico de função(com apoio da biblioteca: Chart.js ou Plotly)
//criar um servidor frontend(port:5500)

const tbody = document.querySelector(".tabela tbody")
const template = /** @type {HTMLTemplateElement} */ (
document.getElementById("tmplLinha")
)

window.addEventListener("DOMContentLoaded", async () => {
    buscarUsuarios()
})

async function buscarUsuarios() {

    try {
        const res = await fetch("http://127.0.0.1:5000/usuarios")
        if (!res.ok) {
            throw new Error("Erro na resposta")
        }
        const data = await res.json()
        renderizarDados(data)

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


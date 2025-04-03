const apiUrl = "http://localhost:5000/products";

document.getElementById("productForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const supplier = document.getElementById("supplier").value;
    const cost = document.getElementById("cost").value;
    const price = document.getElementById("price").value;

    const response = await fetch(`${apiUrl}/create`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, supplier, cost, price })
    });
    
    if (response.ok) {
        loadProducts();
        document.getElementById("productForm").reset();
    }
});

async function loadProducts() {
    const response = await fetch(apiUrl);
    const data = await response.json();
    const list = document.getElementById("productList");
    list.innerHTML = "";
    
    if (data.products && Array.isArray(data.products)) {
        data.products.forEach(product => {
            const id = product.id ?? "N/A";
            const name = product.name ?? "Nome desconhecido";
            const supplier = product.supplier ?? "Fornecedor desconhecido";
            const cost = product.cost ?? "0.00";
            const price = product.price ?? "0.00";

            const item = document.createElement("li");
            item.textContent = `${id} - ${name} (Fornecedor: ${supplier}, Custo: R$${cost}, Preço: R$${price})`;
            list.appendChild(item);
        });
    } else {
        list.innerHTML = "<li>Nenhum produto encontrado.</li>";
    }
}

document.getElementById("loadProductsBtn").addEventListener("click", loadProducts);

let cart = []; 

function addToCart(itemName, itemPrice) {
    const existingItem = cart.find(item => item.name === itemName);
    if (existingItem) {
        existingItem.quantity += 1; // Tăng số lượng
    } else {
        cart.push({ name: itemName, price: itemPrice, quantity: 1 });
    }
    updateCartDisplay();
}

function updateCartDisplay() {
    const cartCount = document.getElementById('cart-count');
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');

    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    cartCount.textContent = totalItems;

    cartItems.innerHTML = '';
    let totalPrice = 0;
    cart.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `
            ${item.name} (x${item.quantity}) - 
            <span class="price">${(item.price * item.quantity).toLocaleString()} VND</span>
        `;
        cartItems.appendChild(li);
        totalPrice += item.price * item.quantity;
    });
    cartTotal.innerHTML = `<span class="price">${totalPrice.toLocaleString()} VND</span>`;
}

function toggleCart() {
    const cartModal = document.getElementById('cart-modal');
    cartModal.classList.toggle('visible');
}

// Thanh toán
function checkout() {
    alert('Thank you for your purchase!');
    cart = []; 
    updateCartDisplay();
    toggleCart();
}

function handleBuyNow(itemName, itemPrice) {
    addToCart(itemName, itemPrice);
    alert(`${itemName} has been added to your cart!`);
}
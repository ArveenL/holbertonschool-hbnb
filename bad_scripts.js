// Note: Static place cards(as per task 0.design), replaced with dynamic content
// fetched from API
// Also handles login link visibility and client-side price filtering


// Function to get a cookie value by name
function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
            return cookie.substring(name.length + 1);
        }
    }
    return null;
}

// Show/hide login link based on JWT token
function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.querySelector('.login-button');

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        fetchPlaces(token); // fetch places only if authenticated
    }
}

// Fetch places from API using Promises
function fetchPlaces(token) {
    fetch('/api/places', {
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    .then(response => response.json())
    .then(data => displayPlaces(data))
    .catch(error => console.error('Error fetching places:', error));
}

// Populate the places list dynamically
function displayPlaces(places) {
    const placesSection = document.getElementById('places-list');
    placesSection.innerHTML = '';

    places.forEach(place => {
        const div = document.createElement('div');
        div.className = 'place-card';
        div.innerHTML = `
            <h3>${place.name}</h3>
            <p>Price per night: $${place.price}</p>
            <a href="place.html" class="details-button">View Details</a>
        `;
        // store price as dataset for filtering
        div.dataset.price = place.price;
        placesSection.appendChild(div);
    });
}

// Client-side price filtering
const priceFilter = document.getElementById('price-filter');
priceFilter.addEventListener('change', function() {
    const selected = this.value;
    const placeCards = document.querySelectorAll('.place-card');

    placeCards.forEach(card => {
        const price = parseFloat(card.dataset.price);
        if (!selected || selected === '' || price <= parseFloat(selected)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
});

// Run on page load
checkAuthentication();
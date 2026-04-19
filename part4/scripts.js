async function loginUser(email, password) {
  const response = await fetch('http://127.0.0.1:5678/api/v1/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  if (response.ok) {
    const data = await response.json();
    window.localStorage.setItem("token", data.access_token)
    window.location.href = 'index.html';
  } else {
    alert('Login failed: ' + response.statusText);
  }
}

// Run on page load
document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const priceFilter = document.getElementById('price-filter');
  const reviewForm = document.getElementById('review-form');
  checkAuthentication();

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      let email = document.getElementById("email").value;
      let password = document.getElementById("password").value;
      loginUser(email, password);
    });
  }

  // Client-side price filtering
  if (priceFilter) {
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
  }

  if (reviewForm) {
    const token = getCookie('token');
    const place = getFromUrl("id");

    if (!token || !place) {
      window.location.href = 'index.html';
      return;
    }

    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const reviewText = document.getElementById('review').value;
      const rating = document.getElementById('rating')?.value;

      try {
        const response = await submitReview(token, place, reviewText, rating);

        if (response.ok) {
          alert('Review submitted successfully!');
          reviewForm.reset();
        } else {
          alert('Failed to submit review');
        }
      }
      catch {
        alert('Failed to submit review');
      }
    });
  }
});

// Show/hide login link based on JWT token
function checkAuthentication() {
  const token = window.localStorage.getItem('token');
  const loginLink = document.querySelector('.login-button');

  if (!loginLink) return;

  if (!token) {
    loginLink.style.display = 'block';
  } else {
    loginLink.style.display = 'none';
    fetchPlaces(token); // fetch places only if authenticated
  }
}

// Fetch places from API using Promises
function fetchPlaces(token) {
  fetch('http://127.0.0.1:5678/api/v1/places', {
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
  if (!placesSection) return;

  placesSection.innerHTML = '';

  places.forEach(place => {
    const div = document.createElement('div');
    div.className = 'place-card';
    div.innerHTML = `
      <h3>${place.name}</h3>
      <p>Price per night: $${place.price}</p>
      <a href="place.html?id=${place.id}" class="details-button">View Details</a>
    `;
    // store price as dataset for filtering
    div.dataset.price = place.price;
    placesSection.appendChild(div);
  });
}

function getFromUrl(name){
  let params = new URLSearchParams(document.location.search);
  return params.get(name);
}

async function submitReview(token, place, text, rating) {
    return fetch('http://127.0.0.1:5678/api/v1/reviews', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ` + token
        },
        body: JSON.stringify({
            place_id: place,
            review: text,
            rating: rating
        })
    });
}

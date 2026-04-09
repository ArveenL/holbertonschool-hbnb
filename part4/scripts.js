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

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      let email = document.getElementById("email").value;
      let password = document.getElementById("password").value;
      loginUser(email, password);
    });
  }
});
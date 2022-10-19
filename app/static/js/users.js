document.addEventListener('DOMContentLoaded', function() {
    var loginBtn = document.getElementById("user-login-btn");
    loginBtn.addEventListener("click", function(){
        login();
    });
});

function login(){
    var email = document.getElementById("user-email").value;
    var password = document.getElementById("user-password").value;
    return fetch(`/api/auth/users/login/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "email": email,
            "password": password,
        })
        })
        .then(response => response.json())
        .then(data => {
            localStorage.setItem("user", JSON.stringify(data.user));
            var user = JSON.parse(localStorage.getItem("user"));
            console.log(user.username);
            if (data.status === "success"){
            }
        })
}

document.addEventListener('DOMContentLoaded', function() {
    var loginBtn = document.getElementById("user-login-btn");
    if (loginBtn){
        loginBtn.addEventListener("click", function(){
            const email = document.getElementById("login-user-email").value;
            const password = document.getElementById("login-user-password").value;
            login(email, password);
        });
    }

    var signupBtn = document.getElementById("user-signup-btn");
    if (signupBtn){
        signupBtn.addEventListener("click", function(){
            signup();
        });
    }
});

async function login(email, password){
    
    const response = await fetch(`/api/auth/users/login/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "email": email,
            "password": password,
        })
        })
        if (!response.ok) {
            const data = await response.json();
            console.log(data);
            for (var key in data){
                document.getElementById("login-error-msg").innerHTML = data[key];
            }
            console.log(response)
            throw new Error(`HTTP error! status: ${data}`);
        }
        const data = await response.json();
        localStorage.setItem("user", JSON.stringify(data.user));
        localStorage.setItem("access_token", JSON.stringify(data.access_token));
        var user = JSON.parse(localStorage.getItem("user"));
        window.location.href = `/worldcup/qatar/profile/`;
        console.log(data);
        
}


async function signup(){
    var username = document.getElementById("signup-user-username").value;
    var email = document.getElementById("signup-user-email").value;
    var password = document.getElementById("signup-user-password").value;
    var password2 = document.getElementById("signup-user-password-confirmation").value;
    if (username === "" || email === "" || password === "" || password2 === ""){
        document.getElementById("signup-error-msg").innerHTML = "LLene todos los campos";
    } else if (password === password2){
        const response = await fetch(`/api/auth/users/signup/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                "username": username,
                "email": email,
                "password": password,
                "password_confirmation": password2,
            })
            })
            if (!response.ok) {
                const data = await response.json();
                console.log(data);
                for (var key in data){
                    document.getElementById("signup-error-msg").innerHTML = data[key];
                }
                throw new Error(`HTTP error! status: ${data}`);
            }
            const data = await response.json();
            login(email, password);
            
    } else {
        document.getElementById("signup-error-msg").innerHTML = "Las contraseñas no coinciden";
    }
}

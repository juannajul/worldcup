document.addEventListener('DOMContentLoaded', function() {
    var access_token = JSON.parse(localStorage.getItem("access_token"));
    if (access_token == null){
        window.location.href = "/worldcup/qatar/login/";
    }
    setProfileUsername();
    getProfileUserPool();
    const logoutBtn = document.getElementById("profile-logout-btn-container");
    if (logoutBtn != null){ 
    logoutBtn.addEventListener("click", function(){
        logout();
    });
    }
    getUserCredits();
});

function setProfileUsername(){
    var user = JSON.parse(localStorage.getItem("user"));
    var username = user.username
    var username = document.getElementById("profile-username-title");
    username.innerHTML = `Bievenido ${user.username}`;
}

async function getProfileUserPool(){
    var user = JSON.parse(localStorage.getItem("user"));
    var username = user.username

    const response = await fetch(
		`/api/worldcup/worldcup_pools/${username}/pool_by_username/`,
		{method: 'GET',}
	);
	if (!response.ok) {
		throw new Error(`HTTP error! status: ${response.status}`);
	}
	const data = await response.json();
    poolContainer = document.querySelector('#profile-user-pools-container');
    profilePool = '';
    poolNumber = 1;
    data.forEach(pool => {
        profilePool += `
        <a href="/worldcup/qatar/retrieve_pool/${pool.id}" class="profile-user-pool-container-link" id="profile-user-pool-link_${pool.id}">
            <div id="profile-user-pool-container_${pool.id}" class="profile-user-pool-container">
                <div class="profile-user-pool-number-container">
                    <h4 id="profile-user-pool-number-title-${pool.id}" class="profile-user-pool-number-title">${poolNumber}</h4>
                </div>
                <div class="profile-user-pool-user-container">
                    <h4 id="profile-user-pool-user-title-${pool.id}" class="profile-user-pool-user-title">${pool.user.username}</h4>
                </div>
                <div class="profile-user-pool-points-container">
                    <h4 id="profile-user-pool-points-title-${pool.id}" class="profile-user-pool-points-title">${pool.points} Pts</h4>
                </div>
            </div>
        </a>
        `
        poolNumber += 1;
    });
    poolContainer.innerHTML = profilePool
}

async function logout(){
    response = await fetch(`/api/auth/users/logout/`, {
        method: 'GET',
    })
    if (!response.ok) {
		throw new Error(`HTTP error! status: ${response.status}`);
	}
    localStorage.clear();
    window.location.reload();
}

function blockCreatePoolBtn(credits){
    const createPoolBtn = document.getElementById("profile-pool-creation-btn-link");
    
    if (credits <= 0 ){
        createPoolBtn.style.display = "none";
    } else {
        createPoolBtn.style.display = "block";
    }
    
}

async function getUserCredits(){
    var user = JSON.parse(localStorage.getItem("user"));
    var username = user.username

    const response = await fetch(
        `/api/auth/users/${username}/`,
        {method: 'GET',}
    );
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data)
    credits = data.credits
    blockCreatePoolBtn(credits);
    const creditsSel = document.querySelector('#profile-credits-title');
    creditsSel.innerHTML = `${credits} Credits`;
}
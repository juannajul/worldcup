document.addEventListener('DOMContentLoaded', function() {
    setProfileUsername();
    getProfileUserPool();
    const logoutBtn = document.getElementById("profile-logout-btn-container");
    if (logoutBtn != null){ 
    logoutBtn.addEventListener("click", function(){
        logout();
    });
    }
});

function setProfileUsername(){
    var user = JSON.parse(localStorage.getItem("user"));
    var username = user.username
    const credits = document.querySelector('#profile-credits-title');
    var username = document.getElementById("profile-username-title");
    username.innerHTML = `Bievenido ${user.username}`;
    credits.innerHTML = `${user.credits} Credits`;
    console.log(user)
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
    console.log(data)
    poolContainer = document.querySelector('#profile-user-pools-container');
    profilePool = '';
    poolNumber = 1;
    data.forEach(pool => {
        console.log(pool)
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
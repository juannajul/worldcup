document.addEventListener('DOMContentLoaded', function() {
    getUsersPools()
});

async function getUsersPools(){
    const response = await fetch(
		`/api/worldcup/worldcup_pools/`,
		{method: 'GET',}
	);
	if (!response.ok) {
		throw new Error(`HTTP error! status: ${response.status}`);
	}
	const data = await response.json();
    poolContainer = document.querySelector('#rankings-user-pools-container');
    profilePool = '';
    poolNumber = 1;
    data.forEach(pool => {
        profilePool += `
        <a href="/worldcup/qatar/retrieve_pool_ranking/${pool.id}" class="rankings-user-pool-container-link" id="rankings-user-pool-link_${pool.id}">
            <div id="rankings-user-pool-container_${pool.id}" class="rankings-user-pool-container">
                <div class="rankings-user-pool-number-container">
                    <h4 id="rankings-user-pool-number-title-${pool.id}" class="rankings-user-pool-number-title">${poolNumber}</h4>
                </div>
                <div class="rankings-user-pool-user-container">
                    <h4 id="rankings-user-pool-user-title-${pool.id}" class="rankings-user-pool-user-title">${pool.user.username}</h4>
                </div>
                <div class="rankings-user-pool-points-container">
                    <h4 id="rankings-user-pool-points-title-${pool.id}" class="rankings-user-pool-points-title">${pool.points} Pts</h4>
                </div>
            </div>
        </a>
        `
        poolNumber += 1;
    });
    poolContainer.innerHTML = profilePool
}
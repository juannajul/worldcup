document.addEventListener('DOMContentLoaded', function() {
    var path = window.location.pathname;
    var poolId = path.split('/')[4];
    getPool(poolId);
    
});

async function teamGroupPointsMatches(poolId){
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    response = await fetch(
        `/api/worldcup/pool_group_teams/${poolId}/analize_pool_group_matches/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        body: JSON.stringify({
           
        })
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
}

async function getPool(poolId){
    response = await fetch(
        `/api/worldcup/worldcup_pools/${poolId}/`, {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    pool = data;
    var groupIsAnalizer = pool.group_analized;
    if (groupIsAnalizer == false){
        teamGroupPointsMatches(poolId);
    }
}
document.addEventListener('DOMContentLoaded', function() {
    var access_token = JSON.parse(localStorage.getItem("access_token"));
    if (access_token == null){
        window.location.href = "/worldcup/qatar/login/";
    }
    const startMatchBtn = document.querySelector('#worldcup-manage-start-match-btn');
    startMatchBtn.addEventListener('click', startMatches);

    const startKeyMatchBtn = document.querySelector('#worldcup-manage-start-key-match-btn');
    startKeyMatchBtn.addEventListener('click', startKeyMatches);

    const finishMatchBtn = document.querySelector('#worldcup-manage-finish-match-btn');
    finishMatchBtn.addEventListener('click', finishMatches);

    const groupPointsBtn = document.querySelector('#worldcup-manage-points-group-classified-btn');
    groupPointsBtn.addEventListener('click', GroupPoints); 

    const finishKeyMatchBtn = document.querySelector('#worldcup-manage-finish-key-match-btn');
    finishKeyMatchBtn.addEventListener('click', finishKeyMatches);

    const setPoolGroupMatchesPointsBtn = document.querySelector('#worldcup-manage-points-group-match-btn');
    setPoolGroupMatchesPointsBtn.addEventListener('click', setPoolGroupMatchesPoints);

    const createRoundOf16Btn = document.querySelector('#worldcup-manage-create-roundOf16-btn');
    createRoundOf16Btn.addEventListener('click', createRoundOf16);

    const createRoundOf8Btn = document.querySelector('#worldcup-manage-create-roundOf8-btn');
    createRoundOf8Btn.addEventListener('click', createRoundOf8);

    const createSemifinalBtn = document.querySelector('#worldcup-manage-create-semifinal-btn');
    createSemifinalBtn.addEventListener('click', createSemifinal);

    const createFinalBtn = document.querySelector('#worldcup-manage-create-final-btn');
    createFinalBtn.addEventListener('click', createFinal);

    const setPoolKeyMatchesPointsBtn = document.querySelector('#worldcup-manage-points-key-match-btn');
    setPoolKeyMatchesPointsBtn.addEventListener('click', setPoolKeyMatchesPoints);

    const setPoolKeyMatchesWinnerBtn = document.querySelector('#worldcup-manage-winner-key-match-btn');
    setPoolKeyMatchesWinnerBtn.addEventListener('click', setPoolKeyMatchesWinner);

    const updateUserPasswordBtn = document.querySelector('#worldcup-update-password-btn');
    updateUserPasswordBtn.addEventListener('click', updateUserPassword);

    window.setTimeout(()=>{
        matchesPlayed();
    }, 300)
    window.setTimeout(()=>{
        keyMatchesPlayed();
    }, 1000)
    window.setTimeout(()=>{
        matchesAnalized();
    }, 300)
    window.setTimeout(()=>{
        keyMatchesAnalized();
    }, 1000)
});


async function startMatches() {
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const matchNumber = document.querySelector('#worldcup-manage-start-match-input').value;
    const response = await fetch(`/api/worldcup/worldcup_matches/${matchNumber}/start_match/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

async function startKeyMatches() {
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const matchNumber = document.querySelector('#worldcup-manage-start-key-match-input').value;
    const response = await fetch(`/api/worldcup/worldcup_key_matches/${matchNumber}/start_match/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

async function finishMatches() {
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const matchNumber = document.querySelector('#worldcup-manage-finish-match-input').value;
    const response = await fetch(`/api/worldcup/worldcup_matches/${matchNumber}/finish_match/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

async function finishKeyMatches() {
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const matchNumber = document.querySelector('#worldcup-manage-finish-key-match-input').value;
    const response = await fetch(`/api/worldcup/worldcup_key_matches/${matchNumber}/finish_key_match/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
            console.log(response);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

async function setPoolGroupMatchesPoints(){
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const response = await fetch(`/api/worldcup/pool_matches/set_pool_match_points/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        })
        if (!response.ok) {
            console.log(response);
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}


async function GroupPoints(){
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const response = await fetch(`/api/worldcup/pool_group_teams/set_group_places_points/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

async function matchesPlayed(){
    const response = await fetch(`/api/worldcup/worldcup_matches/get_played_matches/`, {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
        const matchesPlayed = document.querySelector('#worldcup-manage-info-matches-played');
        matchesPlayed.innerHTML = data.map(match => {
            return `
            <div class="worldcup-manage-info-match-played-container">
                <h4 class="worldcup-manage-info-match-played-info">Match: ${match.match_number} Group: ${match.group} - ${match.team_1.country} vs ${match.team_2.country}.</h4>
            </div>
            `
        }).join('');
}

async function keyMatchesPlayed(){
    const response = await fetch(`/api/worldcup/worldcup_key_matches/get_played_matches/`, {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
        const matchesPlayed = document.querySelector('#worldcup-manage-info-matches-played');
        matchesPlayed.innerHTML += data.map(match => {
            return `
            <div class="worldcup-manage-info-match-played-container">
                <h4 class="worldcup-manage-info-match-played-info">Match: ${match.match_number} Round: ${match.round} - ${match.team_1.country} vs ${match.team_2.country}.</h4>
            </div>
            `
        }).join('');
}

async function matchesAnalized(){
    const response = await fetch(`/api/worldcup/worldcup_matches/get_analized_matches/`, {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
        const matchesPlayed = document.querySelector('#worldcup-manage-info-matches-analized');
        matchesPlayed.innerHTML = data.map(match => {
            return `
            <div class="worldcup-manage-info-match-analized-container">
                <h4 class="worldcup-manage-info-match-analized-info">Match: ${match.match_number} Group: ${match.group} - ${match.team_1.country} vs ${match.team_2.country}.</h4>
            </div>
            `
        }).join('');
}

async function keyMatchesAnalized(){
    const response = await fetch(`/api/worldcup/worldcup_key_matches/get_analized_matches/`, {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
        const matchesPlayed = document.querySelector('#worldcup-manage-info-matches-analized');
        matchesPlayed.innerHTML += data.map(match => {
            return `
            <div class="worldcup-manage-info-match-analized-container">
                <h4 class="worldcup-manage-info-match-analized-info">Match: ${match.match_number} Round: ${match.round} - ${match.team_1.country} vs ${match.team_2.country}.</h4>
            </div>
            `
        }).join('');
}

async function createRoundOf16(){
    match_numbers = [49, 50, 51, 52, 53, 54, 55, 56];
    const create_match = await match_numbers.forEach(match_number => {
        createRoundOf16MatchesKeys(match_number);
    })
    console.log(create_match);
}

async function createRoundOf16MatchesKeys(match_number){
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const response = await fetch(`/api/worldcup/worldcup_key_matches/create_key_matches_roundOf16/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        body: JSON.stringify({
            match_number: match_number,
        })
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

async function createRoundOf8(){
    match_numbers = [57, 58, 59, 60];
    const create_match = await match_numbers.forEach(match_number => {
        createRoundOf8MatchesKeys(match_number);
    })
    console.log(create_match);
}

async function createRoundOf8MatchesKeys(match_number){
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const response = await fetch(`/api/worldcup/worldcup_key_matches/create_key_matches_quarter_finals/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        body: JSON.stringify({
            match_number: match_number,
        })
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

async function createSemifinal(){
    match_numbers = [61, 62];
    const create_match = await match_numbers.forEach(match_number => {
        createSemifinalKeys(match_number);
    })
    console.log(create_match);
}

async function createSemifinalKeys(match_number){
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const response = await fetch(`/api/worldcup/worldcup_key_matches/create_key_matches_semifinal/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        body: JSON.stringify({
            match_number: match_number,
        })
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

async function createFinal(){
    match_numbers = [63, 64];
    const create_match = await match_numbers.forEach(match_number => {
        createFinalKeys(match_number);
    })
    console.log(create_match);
}

async function createFinalKeys(match_number){
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const response = await fetch(`/api/worldcup/worldcup_key_matches/create_key_matches_final/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        body: JSON.stringify({
            match_number: match_number,
        })
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

async function setPoolKeyMatchesPoints(){
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const response = await fetch(`/api/worldcup/pool_key_matches/set_pool_key_match_points/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

async function setPoolKeyMatchesWinner(){
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const response = await fetch(`/api/worldcup/pool_key_matches/set_pool_key_match_winner/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

async function updateUserPassword(){
    var access_token = localStorage.getItem('access_token');
    var token = access_token.slice(1, -1)
    const email = document.querySelector('#worldcup-update-password-input-email').value;
    const password = document.querySelector('#worldcup-update-password-input-password').value;
    const password_confirmation = document.querySelector('#worldcup-update-password-input-password-confirmation').value;
    const response = await fetch(`/api/auth/users/update_password/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        },
        body: JSON.stringify({
            email: email,
            password: password,
            password_confirmation: password_confirmation,
        })
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        console.log(response);
}

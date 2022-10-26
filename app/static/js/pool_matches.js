document.addEventListener('DOMContentLoaded', function() {
  var matchesNumberList = [];
  const createPoolMatchesButton = document.querySelector('#worldcup-save-pool-matches-btn');
  getWorldcupMatches(matchesNumberList);
  createPoolMatchesButton.addEventListener('click', function() {
    createPool(matchesNumberList);
  });
  
});

async function getWorldcupMatches(matchesNumberList) {
    const response = await fetch(
		'/api/worldcup/worldcup_matches/',
		{
			method: 'GET',
		}
	);
	if (!response.ok) {
		throw new Error(`HTTP error! status: ${response.status}`);
	}
	const data = await response.json();
    console.log(data);
    for (let i = 0; i < data.length; i++) {
        matchesNumberList.push(data[i].match_number);
    }
    showWorldcupMatches(data);
}

function showWorldcupMatches(data) {
    const table = document.querySelector('#worldcup-matches-container');
    let poolMatches = '';
    for (let i = 0; i < data.length; i++) {
        date = data[i].match_date;
        date = date.split('-');
        date = date[2].split('T')[0]  + '/' + date[1] + '/' + date[0] + '   ' + date[2].split('T')[1].split('Z')[0];
        poolMatches += `
            <div id="worldcup-match-container">
                <form id="worldcup-match-form-${data[i].match_number}">
                    <div id="worldcup-match-number-container">
                        <h4 class="worldcup-match-number-container-title">Match: ${data[i].match_number} - Group: ${data[i].group} - Round ${data[i].round}</h4>
                    </div>
                    <label for="worldcup-match-number-${data[i].match_number}" id="worldcup-match-number-${data[i].match_number}" value="${data[i].match_number}" hidden>${data[i].match_number}</label>
                    <label for="worldcup-match-group-${data[i].match_number}" id="worldcup-match-group-${data[i].match_number}" value="${data[i].group}" hidden>${data[i].group}</label>
                    <label for="worldcup-match-round-${data[i].match_number}" id="worldcup-match-round-${data[i].match_number}" value="${data[i].round}" hidden>${data[i].round}</label>
                    <label for="worldcup-match-date-${data[i].match_number}" id="worldcup-match-date-${data[i].match_number}" value="${data[i].match_date}" hidden>${data[i].match_date}</label>
                    <div id="worldcup-match-team_1">
                        <label id="worldcup-match-team_1-code-${data[i].match_number}" class="worldcup-match-team_1-code" for="worldcup-match-team_1-code">${data[i].team_1.team_code}</label>
                        <div class="worldcup-match-team-flag">
                            <img src="${data[i].team_1.flag_image}" alt="">
                        </div>
                        <div id="worldcup-match-team_1-name">
                            <h4 id="worldcup-match-team_1-name-title">${data[i].team_1.country}</h4>
                        </div>
                        <div id="worldcup-match-team_1-goals-container">
                            <input type="" id="worldcup-match-team_1-goals-${data[i].match_number}" class="worldcup-match-team_1-goals" name="worldcup-match-team_1-goals" min="0" value="${data[i].team_1_goals}">
                        </div>   
                    </div>
                    <div id="worldcup-match-team_2">
                        <label id="worldcup-match-team_2-code-${data[i].match_number}" class="worldcup-match-team_2-code" for="worldcup-match-team_2-code">${data[i].team_2.team_code}</label>
                        <div class="worldcup-match-team-flag">
                            <img src="${data[i].team_2.flag_image}" alt="">
                        </div>
                        <div id="worldcup-match-team_2-name">
                            <h4 id="worldcup-match-team_2-name-title">${data[i].team_2.country}</h4>
                        </div>
                        <div id="worldcup-match-team_2-goals-container">
                            <input type="" id="worldcup-match-team_2-goals-${data[i].match_number}" class="worldcup-match-team_2-goals" name="worldcup-match-team_2-goals" min="0" value="${data[i].team_2_goals}">
                        </div> 
                    </div>
                    <div class="worldcup-match-date-container" id="worldcup-match-date-container-${data[i].match_number}">
                        <h4 id="worldcup-match-date-title">${date}</h4>
                    </div>
                </form>
            </div>
            </hr>
        `;
    }
    table.innerHTML = poolMatches;
}

async function getMatchInformation(matchesNumberList, poolId){
    matchesNumberList.forEach(matchNumber => {
        var matchData = {}
        let team_1 = document.getElementById(`worldcup-match-team_1-code-${matchNumber}`).innerHTML;
        let team_1_goals = document.getElementById(`worldcup-match-team_1-goals-${matchNumber}`).value;
        let team_2 = document.getElementById(`worldcup-match-team_2-code-${matchNumber}`).innerHTML;
        let team_2_goals = document.getElementById(`worldcup-match-team_2-goals-${matchNumber}`).value;
        let match_date = document.getElementById(`worldcup-match-date-${matchNumber}`).innerHTML;
        let group = document.getElementById(`worldcup-match-group-${matchNumber}`).innerHTML;
        let match_number = document.getElementById(`worldcup-match-number-${matchNumber}`).innerHTML;
        let round = document.getElementById(`worldcup-match-round-${matchNumber}`).innerHTML;
        let pool = 1
        matchData = {
            "team_1": team_1,
            "team_1_goals": team_1_goals,
            "team_2": team_2,
            "team_2_goals": team_2_goals,
            "match_date": match_date,
            "group": group,
            "match_number": match_number,
            "round": round,
            "pool": poolId
        }
        console.log(matchData);
        console.log("LISTO");
        createPoolMatches(matchData);
    });
}

async function createPool(matchesNumberList){
    response = await fetch(
        `/api/worldcup/worldcup_pools/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
           
        })
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        removeUserCredit();
        poolId = data.id;
        getMatchInformation(matchesNumberList, poolId);
        

}

async function removeUserCredit(){
    var user = JSON.parse(localStorage.getItem("user"));
    var user_username = user.username ;
    response = await fetch(
        `/api/auth/users/${user_username}/remove_credits/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
}

async function createPoolMatches(matchData) {
    console.log(matchData);
    response = await fetch(
        `/api/worldcup/pool_matches/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "team_1": matchData.team_1,
            "team_1_goals": matchData.team_1_goals,
            "team_2": matchData.team_2,
            "team_2_goals": matchData.team_2_goals,
            "match_date": matchData.match_date,
            "group": matchData.group,
            "match_number": matchData.match_number,
            "round": matchData.round,
            "pool": matchData.pool
        })
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
}


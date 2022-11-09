document.addEventListener('DOMContentLoaded', function () {
    var path = window.location.pathname;
    var poolId = path.split('/')[4];
    var roundOf16 = true;
    var quarterFinals = false;
    var semiFinals = false;
    var final = false;
    var thirdPlace = false;
    var finish = false;
    var url = '';
    if (roundOf16){
        url = '/api/worldcup/worldcup_key_matches/Round of 16/get_matches_by_round/';
    }
    var matchesNumberList = [];
    getWorldcupMatches(matchesNumberList, url);
    const savePoolKeyMatchesButton = document.querySelector('#worldcup-save-pool-key-matches-btn');
    savePoolKeyMatchesButton.addEventListener('click', function () {
        if (roundOf16){
            getMatchInformation(matchesNumberList, poolId);
        }
        //getWorldcupMatches(matchesNumberList, url);
        window.setTimeout(()=>{
            if (roundOf16) {
                roundOf16 = false;
                quarterFinals = true;
                semiFinals = false;
                final = false;
                thirdPlace = false;
                createQuarterFinals(poolId)
                url = '/api/worldcup/pool_key_matches/Quarter-finals/get_matches_by_round/';
                matchesNumberList = [];
                window.setTimeout(()=>{
                    getWorldcupMatches(matchesNumberList, url)
                }, 500) 
                ;
            } else if (quarterFinals) {
                getSaveMatchInformation(matchesNumberList, poolId);
                window.setTimeout(()=>{
                    roundOf16 = false;
                    quarterFinals = false;
                    semiFinals = true;
                    final = false;
                    thirdPlace = false;
                    createSemifinalFinals(poolId)
                }, 300)
                window.setTimeout(()=>{
                    url = '/api/worldcup/pool_key_matches/Semi-finals/get_matches_by_round/';
                    matchesNumberList = [];
                    getWorldcupMatches(matchesNumberList, url);
                }, 600)
            }
            else if (semiFinals) {
                getSaveMatchInformation(matchesNumberList, poolId);
                window.setTimeout(()=>{
                    roundOf16 = false;
                    quarterFinals = false;
                    semiFinals = false;
                    thirdPlace = true;
                    final = false;
                    create3rdPlace(poolId)
                }, 300)
                window.setTimeout(()=>{
                    url = '/api/worldcup/pool_key_matches/3rd-Place/get_matches_by_round/';
                    matchesNumberList = [];
                    getWorldcupMatches(matchesNumberList, url);
                }, 600)
            }
            else if (thirdPlace) {
                getSaveMatchInformation(matchesNumberList, poolId);
                window.setTimeout(()=>{
                    roundOf16 = false;
                    quarterFinals = false;
                    semiFinals = false;
                    thirdPlace = false;
                    final = true;
                    createFinal(poolId)
                }, 300)
                window.setTimeout(()=>{
                    url = '/api/worldcup/pool_key_matches/Final/get_matches_by_round/';
                    matchesNumberList = [];
                    getWorldcupMatches(matchesNumberList, url);
                }, 600) 
            }
            else if (final) {
                roundOf16 = false;
                quarterFinals = false;
                semiFinals = false;
                final = false;
                thirdPlace = false;
                finish = true;
                getSaveMatchInformation(matchesNumberList, poolId);
                window.setTimeout(()=>{
                    window.location.href = `/worldcup/qatar/retrieve_pool/${poolId}/`;;
                }, 500)
            }
        });
    }, 300) 
});


async function getWorldcupMatches(matchesNumberList, url) {
    
    const response = await fetch(
        `${url}`, 
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
    console.log(matchesNumberList);
    const show = await showWorldcupMatches(data);
}

async function algo(data){
    const table = document.querySelector('#worldcup-key-matches-container');
    let poolMatches = '';
    for (let i = 0; i < data.length; i++) {
        date = data[i].match_date;
        date = date.split('-');
        date = date[2].split('T')[0] + '/' + date[1] + '/' + date[0] + '   ' + date[2].split('T')[1].split('Z')[0];
        poolMatches += `
              <div id="worldcup-key-match-container">
                  <form id="worldcup-key-match-form-${data[i].match_number}">
                      <div id="worldcup-key-match-number-container">
                          <h4 class="worldcup-key-match-number-container-title">Match: ${data[i].match_number} -  ${data[i].round}</h4>
                      </div>
                      <label for="worldcup-key-match-number-${data[i].match_number}" id="worldcup-key-match-number-${data[i].match_number}" value="${data[i].match_number}" hidden>${data[i].match_number}</label>
                      <label for="worldcup-key-match-group-${data[i].match_number}" id="worldcup-key-match-group-${data[i].match_number}" value="${data[i].group}" hidden>${data[i].group}</label>
                      <label for="worldcup-key-match-round-${data[i].match_number}" id="worldcup-key-match-round-${data[i].match_number}" value="${data[i].round}" hidden>${data[i].round}</label>
                      <label for="worldcup-key-match-date-${data[i].match_number}" id="worldcup-key-match-date-${data[i].match_number}" value="${data[i].match_date}" hidden>${data[i].match_date}</label>
                      <label id="worldcup-key-match-team_1-code-${data[i].match_number}"  for="worldcup-match-team_1-code" hidden>${data[i].team_1.team_code}</label>
                      <label id="worldcup-key-match-team_2-code-${data[i].match_number}"  for="worldcup-match-team_2-code" hidden>${data[i].team_2.team_code}</label>

                      <div id="penalties-title-container">
                        <label id="penalties-title">Penales</label>
                      </div>
                      
                      <div id="worldcup-key-match-team_1">
                          <div class="worldcup-key-match-team-flag">
                              <img src="${data[i].team_1.flag_image}" alt="">
                          </div>
                          <div id="worldcup-key-match-team_1-name">
                              <h4 id="worldcup-key-match-team_1-name-title">${data[i].team_1.country}</h4>
                          </div>
                          <div id="worldcup-key-match-team_1-goals-container">
                              <input type="" id="worldcup-key-match-team_1-goals-${data[i].match_number}" class="worldcup-key-match-team_1-goals" name="worldcup-key-match-team_1-goals" min="0" value="${data[i].team_1_goals}">
                          </div>   
                          <div id="worldcup-key-match-team_1-penalties-container"> 
                            <input  type="" id="worldcup-key-match-team_1-penalties-${data[i].match_number}" class="worldcup-key-match-team_1-penalties" name="worldcup-key-match-team_1-penalties" min="0" value="${data[i].team_1_penalty_goals}">
                          </div>   
                      </div>
                      <div id="worldcup-key-match-team_2">
                          <div class="worldcup-key-match-team-flag">
                              <img src="${data[i].team_2.flag_image}" alt="">
                          </div>
                          <div id="worldcup-key-match-team_2-name">
                              <h4 id="worldcup-key-match-team_2-name-title">${data[i].team_2.country}</h4>
                          </div>
                          <div id="worldcup-key-match-team_2-goals-container">
                              <input type="" id="worldcup-key-match-team_2-goals-${data[i].match_number}" class="worldcup-key-match-team_2-goals" name="worldcup-key-match-team_2-goals" min="0" value="${data[i].team_2_goals}">
                          </div> 
                          <div id="worldcup-key-match-team_2-penalties-container">
                              <input type="" id="worldcup-key-match-team_2-penalties-${data[i].match_number}" class="worldcup-key-match-team_2-penalties" name="worldcup-key-match-team_1-penalties" min="0" value="${data[i].team_2_penalty_goals}">
                          </div>  
                      </div>
                      <div class="worldcup-key-match-date-container" id="worldcup-match-date-container-${data[i].match_number}">
                          <h4 id="worldcup-key-match-date-title">${date}</h4>
                      </div>
                  </form>
              </div>
              </hr>
          `;
    }
    table.innerHTML = poolMatches;
}

async function showWorldcupMatches(data) {
    const a = await algo(data);
}

async function getMatchInformation(matchesNumberList, poolId) {
    const a = await matchesNumberList.forEach(matchNumber => {
        var matchData = {}
        let team_1 = document.getElementById(`worldcup-key-match-team_1-code-${matchNumber}`).innerHTML;
        let team_1_goals = document.getElementById(`worldcup-key-match-team_1-goals-${matchNumber}`).value;
        let team_1_penalty_goals = document.getElementById(`worldcup-key-match-team_1-penalties-${matchNumber}`).value;
        let team_2 = document.getElementById(`worldcup-key-match-team_2-code-${matchNumber}`).innerHTML;
        let team_2_goals = document.getElementById(`worldcup-key-match-team_2-goals-${matchNumber}`).value;
        let team_2_penalty_goals = document.getElementById(`worldcup-key-match-team_2-penalties-${matchNumber}`).value;
        let match_date = document.getElementById(`worldcup-key-match-date-${matchNumber}`).innerHTML;
        let group = document.getElementById(`worldcup-key-match-group-${matchNumber}`).innerHTML;
        let match_number = document.getElementById(`worldcup-key-match-number-${matchNumber}`).innerHTML;
        let round = document.getElementById(`worldcup-key-match-round-${matchNumber}`).innerHTML;
        matchData = {
            "team_1": team_1,
            "team_1_goals": team_1_goals,
            "team_1_penalty_goals": team_1_penalty_goals,
            "team_2": team_2,
            "team_2_goals": team_2_goals,
            "team_2_penalty_goals": team_2_penalty_goals,
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

async function createPoolMatches(matchData) {
    console.log(matchData);
    response = await fetch(
        `/api/worldcup/pool_key_matches/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "team_1": matchData.team_1,
            "team_1_goals": matchData.team_1_goals,
            "team_1_penalty_goals": matchData.team_1_penalty_goals,
            "team_2": matchData.team_2,
            "team_2_goals": matchData.team_2_goals,
            "team_2_penalty_goals": matchData.team_2_penalty_goals,
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

async function getSaveMatchInformation(matchesNumberList, poolId) {
    const a = await matchesNumberList.forEach(matchNumber => {
        var matchData = {}
        let team_1 = document.getElementById(`worldcup-key-match-team_1-code-${matchNumber}`).innerHTML;
        let team_1_goals = document.getElementById(`worldcup-key-match-team_1-goals-${matchNumber}`).value;
        let team_1_penalty_goals = document.getElementById(`worldcup-key-match-team_1-penalties-${matchNumber}`).value;
        let team_2 = document.getElementById(`worldcup-key-match-team_2-code-${matchNumber}`).innerHTML;
        let team_2_goals = document.getElementById(`worldcup-key-match-team_2-goals-${matchNumber}`).value;
        let team_2_penalty_goals = document.getElementById(`worldcup-key-match-team_2-penalties-${matchNumber}`).value;
        matchData = {
            "match_number": matchNumber,
            "team_1_goals": team_1_goals,
            "team_1_penalty_goals": team_1_penalty_goals,
            "team_2_goals": team_2_goals,
            "team_2_penalty_goals": team_2_penalty_goals,
            "pool": poolId
        }
        console.log(matchData);
        console.log("LISTO");
        savePoolKeyMatchesResults(matchData, poolId);
    });
}

async function savePoolKeyMatchesResults(matchData, poolId){
    const match_number = matchData.match_number;
    response = await fetch(
        `/api/worldcup/pool_key_matches/${match_number}_${poolId}/save_pool_key_match_results/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "team_1_goals": matchData.team_1_goals,
            "team_1_penalty_goals": matchData.team_1_penalty_goals,
            "team_2_goals": matchData.team_2_goals,
            "team_2_penalty_goals": matchData.team_2_penalty_goals,
            "pool": matchData.pool
        })
    })
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
}

async function createQuarterRoundKeyMatches(matchNumber, poolId){
    response = await fetch(
        `/api/worldcup/pool_key_matches/create_pool_quarter_finals/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "pool": poolId,
            "match_number": matchNumber
        })
    })
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    } else {
        console.log(`LISTO ${poolId} ${matchNumber}`);
        const data = await response.json();
    }
}

async function createQuarterFinals(poolId){
    matchesNumberList = [57, 58, 59, 60];
    const create = await matchesNumberList.forEach(matchNumber => {
        createQuarterRoundKeyMatches(matchNumber, poolId);
    });
}

async function createSemifinalRoundKeyMatches(matchNumber, poolId){
    response = await fetch(
        `/api/worldcup/pool_key_matches/create_pool_semifinal_finals/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "pool": poolId,
            "match_number": matchNumber
        })
    })
    if (!response.ok) {
        console.log(response)
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    console.log(`LISTO ${poolId} ${matchNumber}`);
    const data = await response.json();
    console.log(data);
}

async function createSemifinalFinals(poolId){
    matchesNumberList = [61, 62];
    const create = await matchesNumberList.forEach(matchNumber => {
        createSemifinalRoundKeyMatches(matchNumber, poolId);
    });
}

async function create3rdPlaceRoundKeyMatches(matchNumber, poolId){
    response = await fetch(
        `/api/worldcup/pool_key_matches/create_pool_3rdPlace/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "pool": poolId,
            "match_number": matchNumber
        })
    })
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    console.log(`LISTO ${poolId} ${matchNumber}`);
    const data = await response.json();
    console.log(data);
}

async function create3rdPlace(poolId){
    matchesNumberList = [63];
    const create = await matchesNumberList.forEach(matchNumber => {
        create3rdPlaceRoundKeyMatches(matchNumber, poolId);
    });
}

async function createFinalRoundKeyMatch(matchNumber, poolId){
    response = await fetch(
        `/api/worldcup/pool_key_matches/create_pool_finals/`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "pool": poolId,
            "match_number": matchNumber
        })
    })
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    console.log(`LISTO ${poolId} ${matchNumber}`);
    const data = await response.json();
    console.log(data);
}

async function createFinal(poolId){
    matchesNumberList = [64];
    const create = await matchesNumberList.forEach(matchNumber => {
        createFinalRoundKeyMatch(matchNumber, poolId);
    });
}




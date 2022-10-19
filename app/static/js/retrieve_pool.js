document.addEventListener('DOMContentLoaded', function () {
    var path = window.location.pathname;
    var poolId = path.split('/')[4];
    getWorldcupMatches(poolId);



    /*
    createPoolMatchesButton.addEventListener('click', function() {
      createPool(matchesNumberList);
    });
    */
});

async function getWorldcupMatches(poolId) {
    const response = await fetch(
        `/api/worldcup/pool_matches/${poolId}/pool_matches_by_pool/`,
        {
            method: 'GET',
        }
    );
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    showWorldcupMatches(data);
}

function showWorldcupMatches(data) {
    const table = document.querySelector('#worldcup-matches-container');
    let poolMatches = '';
    for (let i = 0; i < data.length; i++) {
        date = data[i].match_date;
        date = date.split('-');
        date = date[2].split('T')[0] + '/' + date[1] + '/' + date[0] + '   ' + date[2].split('T')[1].split('Z')[0];
        poolMatches += `
              <div id="worldcup-match-container">
                  <form id="worldcup-match-form-${data[i].match_number}">
                      <div id="worldcup-match-number-container">
                          <h4 class="worldcup-match-number-container-title">Match: ${data[i].match_number} - Group: ${data[i].group} - Round ${data[i].round}
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
                              <input type="" id="worldcup-match-team_1-goals-${data[i].match_number}" class="worldcup-match-team_1-goals" name="worldcup-match-team_1-goals" min="0" value="${data[i].team_1_goals}" disabled>
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
                              <input type="" id="worldcup-match-team_2-goals-${data[i].match_number}" class="worldcup-match-team_2-goals" name="worldcup-match-team_2-goals" min="0" value="${data[i].team_2_goals}" disabled>
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
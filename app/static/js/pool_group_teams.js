document.addEventListener('DOMContentLoaded', function () {
    getGroupTeams();
});

async function getGroupTeams() {
    var path = window.location.pathname;
    var poolId = path.split('/')[4];
    var groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    for (let i = 0; i < groups.length; i++) {
        const response = await fetch(
            `/api/worldcup/pool_group_teams/${poolId}_${groups[i]}/teams_by_pool_and_group/`,
            {
                method: 'GET',
            }
        );
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const teams = await response.json();
        console.log(teams);
        //show Group Teams
        let group = groups[i];
        const groupTeamsTable = document.getElementById(`worldcup-group-teams-container_${group}`);
        groupTeamsTable.innerHTML = teams.map(team => {
            return `
              <div id="worldcup-group-data-container">
              <div class="worldcup-group-data-team-flag">
                  <img src="${team.team.flag_image}" alt="">
              </div>
              <div id="worldcup-group-data-team-title-container">
                 <h4 class="worldcup-group-data-stats-team-title">${team.team.country}</h4>
              </div>
              <div class="worldcup-group-data-stats-container">
                 <h4 class="worldcup-group-data-stats-title">${team.wins}</h4>
              </div>
              <div class="worldcup-group-data-stats-container">
                 <h4 class="worldcup-group-data-stats-title">${team.draws}</h4>
              </div>
              <div class="worldcup-group-data-stats-container">
                 <h4 class="worldcup-group-data-stats-title">${team.losses}</h4>
              </div>
              <div class="worldcup-group-data-stats-container">
                 <h4 class="worldcup-group-data-stats-title">${team.pool_team_goals_for}</h4>
              </div>
              <div class="worldcup-group-data-stats-container">
                 <h4 class="worldcup-group-data-stats-title">${team.pool_team_goals_against}</h4>
              </div>
              <div class="worldcup-group-data-stats-container">
                 <h4 class="worldcup-group-data-stats-title">${team.pool_team_goals_difference}</h4>
              </div>
              <div class="worldcup-group-data-stats-container">
                 <h4 class="worldcup-group-data-stats-title">${team.pool_team_points}</h4>
              </div>
              <div id="worldcup-group-teams-container_{{group}}"></div>
          </div>
              `;
        }).join('');

    }

}
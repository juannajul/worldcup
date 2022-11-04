document.addEventListener('DOMContentLoaded', function() {
  getGroupTeams();
});

async function getGroupTeams() {
    var groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    for (let i = 0; i < groups.length; i++) {
        const response = await fetch(
            `/api/worldcup/teams/${groups[i]}/team_by_group/`,
            {
                method: 'GET',
            }
        );
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const teams = await response.json();
        console.log(teams);
        //setTeamPlace(place);
        //show Group Teams
        let group = groups[i];
        console.log(group);
        const groupTeamsTable = document.getElementById(`worldcup-group-teams-container_${group}`);
        groupTeamsTable.innerHTML = teams.map(team => {
            return `
            <div id="worldcup-group-data-container">
            <div class="worldcup-group-data-team-flag">
                <img src="${team.flag_image}" alt="">
            </div>
            <div id="worldcup-group-data-team-title-container">
               <h4 class="worldcup-group-data-stats-team-title">${team.country}</h4>
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
               <h4 class="worldcup-group-data-stats-title">${team.goals_for}</h4>
            </div>
            <div class="worldcup-group-data-stats-container">
               <h4 class="worldcup-group-data-stats-title">${team.goals_against}</h4>
            </div>
            <div class="worldcup-group-data-stats-container">
               <h4 class="worldcup-group-data-stats-title">${team.goals_difference}</h4>
            </div>
            <div class="worldcup-group-data-stats-container">
               <h4 class="worldcup-group-data-stats-title">${team.points}</h4>
            </div>
            <div id="worldcup-group-teams-container_{{group}}"></div>
        </div>
            `;
        }).join('');
        
    }
    
}

                

async function setTeamPlace(place) {
    let first_place = false
    let second_place = false
    if (i == 0) {
            first_place = true
        }
    if (i == 1) {
            second_place = true
        }
    const response = await fetch(
        `/api/worldcup/teams/${place}/set_team_place/`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'first_place': first_place,
            'second_place': second_place
        })
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
      //  console.log(data);
}

document.addEventListener('DOMContentLoaded', function() {
  var matchesNumberList = [];
  getWorldcupMatches(matchesNumberList);
  var allForms = document.querySelectorAll('#worldcup-match-form');
  console.log(matchesNumberList);
});

async function getWorldcupMatches(matchesNumberList) {
    const response = await fetch(
		'/api/worldcup/worldcup_matches/',
		{
			method: 'GET',
			Authorization: `Token ${getCookie("access_token")}`,
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
        poolMatches += `
            <div id="worldcup-match-container">
                <form id="worldcup-match-form-${data[i].match_number}">
                    <div id="worldcup-match-number-container">Match: ${data[i].match_number} - Group: ${data[i].group}</div>
                    <div id="worldcup-match-team_1">
                        <label id="worldcup-match-team_1-code-${data[i].match_number}" class="worldcup-match-team_1-code" for="worldcup-match-team_1-code">${data[i].team_1.team_code}</label>
                        <div id="worldcup-match-team_1-name">
                            <h4 id="worldcup-match-team_1-name-title">${data[i].team_1.country}</h4>
                        </div>
                        <div id="worldcup-match-team_1-goals-container">
                            <input type="number" id="worldcup-match-team_1-goals-${data[i].match_number}" class="worldcup-match-team_1-goals" name="worldcup-match-team_1-goals" min="0" value="${data[i].team_1_goals}">
                        </div>   
                    </div>
                    <div id="worldcup-match-team_2">
                        <label id="worldcup-match-team_2-code-${data[i].match_number}" class="worldcup-match-team_2-code" for="worldcup-match-team_2-code">${data[i].team_2.team_code}</label>
                        <div id="worldcup-match-team_2-name">
                            <h4 id="worldcup-match-team_2-name-title">${data[i].team_2.country}</h4>
                        </div>
                        <div id="worldcup-match-team_2-goals-container">
                            <input type="number" id="worldcup-match-team_2-goals-${data[i].match_number}" class="worldcup-match-team_2-goals" name="worldcup-match-team_2-goals" min="0" value="${data[i].team_2_goals}">
                        </div> 
                    </div>
                    <div id="worldcup-match-date-${data[i].match_number}">${data[i].match_date}</div>
                </form>
            </div>
            </hr>
        `;
    }
    table.innerHTML = poolMatches;
}


function getCookie(name) {
    var cookieValue = null;

    if (document.cookie && document.cookie !== '') {

        var cookies = document.cookie.split(';');

        for (var i = 0; i < cookies.length; i++) {

            var cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
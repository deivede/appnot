var playactionfa = "playactionfa"
var deivede73 = "deivede73"

function update_ntws(usr) {

        function setid(user) {
        var visor = document.getElementById(user);
        return visor
}

var visornot = setid(usr);

        const data = (response) => {
            {
                if (response.ok) {
                    response.json().then( dt => {
                    novotweet = dt.nwtt;
                    console.log(novotweet);
                    visornot.innerHTML = novotweet;
                })
                } else {
                    console.log(error);
                }
            }
        }

        async function rendertt() {
            let reqtt = await fetch('', {
            method: "POST",
            credentials: "include",
            body: usr,
            cache: "no-cache",
            headers: new Headers({
              "content-type": "application/json"
            })

        });
            return data(reqtt);
        }

        rendertt();
    }


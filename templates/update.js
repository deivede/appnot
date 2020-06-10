function update_ntws() {

        const visor = document.getElementById("updt");


        const data = (response) => {
            {
                if (response.ok) {
                    response.json().then( dt => {
                    novotweet = dt.nwtt;
                    console.log(novotweet);
                    visor.innerHTML = novotweet;
                })
                } else {
                    console.log(error);
                }
            }
        }

        const rendertt = async () => {
            let reqtt = await fetch('', {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(visor),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "applicaton/json"
            })
        });
            return data(reqtt);
        }

        rendertt();
    }
 function update_ntws() {

        visor = document.getElementById("updt");

        fetch('', {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(visor),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        }).then(response => {
            if (response.ok) {
                response.json().then(data => {
            novotweet = data.nwtt;
            console.log(novotweet);
            visor.innerHTML = novotweet;
        })
            } else {
                console.log("fodase.")
            }
        });

}
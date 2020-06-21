class modulousr {
    constructor(pic, id, link) {
        this.pic = pic;
        this.id = id;
        this.link = link;
    }
}

var playactionfa = new modulousr("https://pbs.twimg.com/profile_images/617404992274698240/s1QyJMCT_400x400.jpg", "playactionfa", "http://twitter.com/playactionfa");
var deivede73 = new modulousr("https://pbs.twimg.com/profile_images/909549046020308992/iUwzkyXZ_400x400.jpg", "deivede73", "http://twitter.com/deivede73")

async function mdl() {

    const obj = await fetch('/dbusr', {method: "GET"})
    const user = await obj.json();

    const a = user.usr.deivede73.id
    console.log(a);

    class Modulo extends React.Component {
        constructor(props) {
            super(props);
            this.state = {nwtt: 0}
            this.ttstate = this.ttstate.bind(this);

        }

        ttstate() {
            var usr = this.props.id;
            const data = (response) => {
                {
                    if (response.ok) {
                        response.json().then(dt => {
                            var novotweet = parseInt(dt.nwtt);
                            console.log(novotweet);
                            this.setState({nwtt: this.state.nwtt + novotweet});
                        })
                    } else {
                        console.log("error");
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

        componentDidMount() {
            setInterval(() => this.ttstate(), 300000);
        }

        render() {
            return (
                <div className="box">
                    <div><a href={this.props.link}><img src={this.props.pict} className="clip"/></a></div>
                    <button className="dot2" onClick={this.ttstate}></button>
                    <div className="dot3">
                        <div className="not">{this.state.nwtt}</div>
                    </div>
                </div>
            )
        }
    }

    ReactDOM.render(
        <div>
            <Modulo pict={playactionfa.pic} link={playactionfa.link} id={playactionfa.id}/>
            <Modulo pict={deivede73.pic} link={deivede73.link} id={deivede73.id}/>
        </div>, document.getElementById("render"));

}

mdl();
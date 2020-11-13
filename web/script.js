function populate_table(name, data) {
    const tb = document.getElementById(name)
    for (o of data) {
        const r = tb.insertRow(-1)

        if ('name' in o.buyB){
            r.insertCell(-1).innerHTML = o.buyB.count + ' ' +o.buyB.name
        } else {
            r.insertCell(-1).innerHTML = ''
        }
        r.insertCell(-1).innerHTML = o.buy.count + ' ' +o.buy.name
        r.insertCell(-1).innerHTML = o.sell.count + ' ' +o.sell.name
        r.insertCell(-1).innerHTML = o.villager
    }
}

function setup() {
    fetch('data.json')
    .then((r) => r.json())
    .then((d) => {
        console.log(d.offers);
        populate_table('sell_body', d.sell);
        populate_table('buy_body', d.buy);
    })
}

window.onload = setup
